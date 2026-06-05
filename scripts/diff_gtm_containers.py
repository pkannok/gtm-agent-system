"""Diff two GTM container exports and write a proposed change log JSON."""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


CHANGE_LOG_SCHEMA_VERSION = "1.0.0"


class ContainerDiffError(Exception):
    """Raised when the diff command cannot read inputs or write output."""


@dataclass(frozen=True)
class EntityConfig:
    entity_type: str
    section_names: tuple[str, ...]
    id_keys: tuple[str, ...]


ENTITY_CONFIGS = (
    EntityConfig("tag", ("tag",), ("tagId", "tag_id", "id")),
    EntityConfig("trigger", ("trigger",), ("triggerId", "trigger_id", "id")),
    EntityConfig("variable", ("variable",), ("variableId", "variable_id", "id")),
    EntityConfig("folder", ("folder",), ("folderId", "folder_id", "id")),
    EntityConfig("template", ("customTemplate", "template"), ("templateId", "template_id", "id")),
)

IGNORED_UPDATE_FIELDS = {
    "fingerprint",
    "tagFingerprint",
    "triggerFingerprint",
    "variableFingerprint",
    "folderFingerprint",
}

CLASSIFIED_FIELDS = {
    "name",
    "displayName",
    "parentFolderId",
    "parent_folder_id",
    "paused",
}


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Compare an original GTM container export and an optimized GTM "
            "container export, then write a deterministic machine-readable change log."
        )
    )
    parser.add_argument(
        "--original",
        required=True,
        type=Path,
        help="Path to the original GTM container export JSON file.",
    )
    parser.add_argument(
        "--optimized",
        required=True,
        type=Path,
        help="Path to the optimized GTM container export JSON file.",
    )
    parser.add_argument(
        "--output",
        required=True,
        type=Path,
        help="Path where the generated change_log JSON should be written.",
    )
    parser.add_argument(
        "--expected-change-log",
        type=Path,
        help=(
            "Optional model-generated change log to compare against detected changes. "
            "Detected changes missing from this file are reported as warnings."
        ),
    )
    return parser.parse_args(argv)


def load_json(path: Path, label: str) -> dict[str, Any]:
    if not path.exists():
        raise ContainerDiffError(f"{label} file does not exist: {path}")
    if not path.is_file():
        raise ContainerDiffError(f"{label} path is not a file: {path}")

    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except UnicodeDecodeError as exc:
        raise ContainerDiffError(f"{label} file is not valid UTF-8: {path}") from exc
    except json.JSONDecodeError as exc:
        raise ContainerDiffError(
            f"invalid JSON in {label} file {path}: line {exc.lineno}, "
            f"column {exc.colno}: {exc.msg}"
        ) from exc

    if not isinstance(data, dict):
        raise ContainerDiffError(f"{label} GTM export JSON root must be an object")

    return data


def as_string(value: Any) -> str:
    if value is None:
        return ""
    return str(value).strip()


def first_string(source: dict[str, Any], keys: tuple[str, ...]) -> str:
    for key in keys:
        normalized = as_string(source.get(key))
        if normalized:
            return normalized
    return ""


def boolish(value: Any) -> bool:
    if isinstance(value, bool):
        return value
    if isinstance(value, str):
        return value.strip().lower() in {"1", "true", "yes"}
    if isinstance(value, int):
        return value != 0
    return False


def get_container_version(export: dict[str, Any], label: str) -> dict[str, Any]:
    container_version = export.get("containerVersion")
    if not isinstance(container_version, dict):
        raise ContainerDiffError(f"{label} export is missing top-level `containerVersion` object")
    return container_version


def collect_entities(
    container_version: dict[str, Any],
    config: EntityConfig,
    warnings: list[str],
    label: str,
) -> dict[str, dict[str, Any]]:
    entities_by_id: dict[str, dict[str, Any]] = {}

    for section_name in config.section_names:
        value = container_version.get(section_name)
        if value is None:
            continue
        if not isinstance(value, list):
            warnings.append(f"{label} section `{section_name}` is not an array and was skipped.")
            continue
        for index, entity in enumerate(value):
            if not isinstance(entity, dict):
                warnings.append(
                    f"{label} section `{section_name}` item {index} is not an object and was skipped."
                )
                continue
            entity_id = first_string(entity, config.id_keys)
            entity_name = first_string(entity, ("name", "displayName"))
            if not entity_id:
                warnings.append(
                    f"{label} {config.entity_type} `{entity_name or '<unnamed>'}` is missing an ID."
                )
                continue
            if entity_id in entities_by_id:
                warnings.append(
                    f"{label} {config.entity_type} ID `{entity_id}` appears more than once."
                )
                continue
            entities_by_id[entity_id] = entity

    return entities_by_id


def canonical_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def filtered_for_update(entity: dict[str, Any]) -> dict[str, Any]:
    ignored = IGNORED_UPDATE_FIELDS | CLASSIFIED_FIELDS
    return {key: value for key, value in entity.items() if key not in ignored}


def changed_fields(before: dict[str, Any], after: dict[str, Any]) -> list[str]:
    ignored = IGNORED_UPDATE_FIELDS | CLASSIFIED_FIELDS
    fields = set(before) | set(after)
    changed: list[str] = []
    for field in sorted(fields):
        if field in ignored:
            continue
        if canonical_json(before.get(field)) != canonical_json(after.get(field)):
            changed.append(field)
    return changed


def entity_summary(entity: dict[str, Any] | None, config: EntityConfig) -> dict[str, Any] | None:
    if entity is None:
        return None
    return {
        "entity_id": first_string(entity, config.id_keys),
        "entity_name": first_string(entity, ("name", "displayName")),
        "entity_type": config.entity_type,
        "gtm_type": first_string(entity, ("type",)),
        "parent_folder_id": first_string(entity, ("parentFolderId", "parent_folder_id")),
        "paused": boolish(entity.get("paused")),
    }


def risk_for_change(change_type: str) -> str:
    if change_type == "deleted":
        return "high"
    if change_type in {"created", "updated", "disabled"}:
        return "medium"
    return "low"


def rollback_note(change_type: str) -> str:
    if change_type == "created":
        return "Remove the created entity from the proposed optimized container if human review rejects it."
    if change_type == "deleted":
        return "Restore the deleted entity from the original container export before import or use."
    if change_type == "renamed":
        return "Restore the original entity name from the source export."
    if change_type == "moved":
        return "Restore the original folder assignment from the source export."
    if change_type == "disabled":
        return "Restore the original paused/enabled state from the source export."
    return "Restore the original entity configuration from the source export."


def make_change(
    change_type: str,
    config: EntityConfig,
    entity_id: str,
    before: dict[str, Any] | None,
    after: dict[str, Any] | None,
    fields: list[str] | None = None,
) -> dict[str, Any]:
    after_summary = entity_summary(after, config)
    before_summary = entity_summary(before, config)
    summary_source = after_summary or before_summary or {
        "entity_id": entity_id,
        "entity_name": "",
        "entity_type": config.entity_type,
    }
    risk_level = risk_for_change(change_type)

    return {
        "change_type": change_type,
        "entity_type": config.entity_type,
        "entity_id": entity_id,
        "entity_name": summary_source.get("entity_name", ""),
        "risk_level": risk_level,
        "manual_review_required": True,
        "human_approval_required": True,
        "reason": "Detected by deterministic comparison of original and optimized GTM exports.",
        "changed_fields": fields or [],
        "before_summary": before_summary,
        "after_summary": after_summary,
        "rollback_note": rollback_note(change_type),
    }


def diff_entity(
    config: EntityConfig,
    entity_id: str,
    before: dict[str, Any],
    after: dict[str, Any],
) -> list[dict[str, Any]]:
    changes: list[dict[str, Any]] = []

    before_name = first_string(before, ("name", "displayName"))
    after_name = first_string(after, ("name", "displayName"))
    if before_name != after_name:
        changes.append(make_change("renamed", config, entity_id, before, after, ["name"]))

    before_folder = first_string(before, ("parentFolderId", "parent_folder_id"))
    after_folder = first_string(after, ("parentFolderId", "parent_folder_id"))
    if before_folder != after_folder:
        changes.append(
            make_change("moved", config, entity_id, before, after, ["parentFolderId"])
        )

    before_paused = boolish(before.get("paused"))
    after_paused = boolish(after.get("paused"))
    if before_paused != after_paused and after_paused:
        changes.append(make_change("disabled", config, entity_id, before, after, ["paused"]))

    fields = changed_fields(before, after)
    if fields and canonical_json(filtered_for_update(before)) != canonical_json(filtered_for_update(after)):
        changes.append(make_change("updated", config, entity_id, before, after, fields))

    return changes


def sort_change_key(change: dict[str, Any]) -> tuple[str, str, str]:
    return (
        as_string(change.get("entity_type")),
        as_string(change.get("entity_id")),
        as_string(change.get("change_type")),
    )


def add_change_ids(changes: list[dict[str, Any]]) -> list[dict[str, Any]]:
    sorted_changes = sorted(changes, key=sort_change_key)
    numbered: list[dict[str, Any]] = []
    for index, change in enumerate(sorted_changes, start=1):
        numbered_change = {"change_id": f"CHG-{index:04d}", **change}
        numbered.append(numbered_change)
    return numbered


def diff_containers(
    original: dict[str, Any],
    optimized: dict[str, Any],
) -> tuple[list[dict[str, Any]], dict[str, dict[str, int]], list[str]]:
    warnings: list[str] = []
    changes: list[dict[str, Any]] = []
    unchanged: dict[str, dict[str, int]] = {}

    original_version = get_container_version(original, "original")
    optimized_version = get_container_version(optimized, "optimized")

    for config in ENTITY_CONFIGS:
        original_entities = collect_entities(original_version, config, warnings, "original")
        optimized_entities = collect_entities(optimized_version, config, warnings, "optimized")
        original_ids = set(original_entities)
        optimized_ids = set(optimized_entities)

        for entity_id in sorted(optimized_ids - original_ids):
            changes.append(
                make_change("created", config, entity_id, None, optimized_entities[entity_id])
            )

        for entity_id in sorted(original_ids - optimized_ids):
            changes.append(
                make_change("deleted", config, entity_id, original_entities[entity_id], None)
            )

        unchanged_count = 0
        for entity_id in sorted(original_ids & optimized_ids):
            detected = diff_entity(
                config, entity_id, original_entities[entity_id], optimized_entities[entity_id]
            )
            if detected:
                changes.extend(detected)
            else:
                unchanged_count += 1

        unchanged[config.entity_type] = {
            "original_count": len(original_entities),
            "optimized_count": len(optimized_entities),
            "unchanged_count": unchanged_count,
        }

    return add_change_ids(changes), unchanged, sorted(warnings)


def summarize_changes(
    changes: list[dict[str, Any]], unchanged: dict[str, dict[str, int]]
) -> dict[str, Any]:
    by_change_type: dict[str, int] = {}
    by_entity_type: dict[str, int] = {}
    high_risk_changes: list[str] = []

    for change in changes:
        change_type = as_string(change.get("change_type"))
        entity_type = as_string(change.get("entity_type"))
        by_change_type[change_type] = by_change_type.get(change_type, 0) + 1
        by_entity_type[entity_type] = by_entity_type.get(entity_type, 0) + 1
        if change.get("risk_level") == "high":
            high_risk_changes.append(as_string(change.get("change_id")))

    return {
        "total_changes": len(changes),
        "by_change_type": {key: by_change_type[key] for key in sorted(by_change_type)},
        "by_entity_type": {key: by_entity_type[key] for key in sorted(by_entity_type)},
        "high_risk_change_ids": sorted(high_risk_changes),
        "unchanged_entities": unchanged,
    }


def change_signature(change: dict[str, Any]) -> tuple[str, str, str]:
    return (
        as_string(change.get("entity_type")),
        as_string(change.get("entity_id")),
        as_string(change.get("change_type")),
    )


def expected_change_signatures(path: Path | None) -> set[tuple[str, str, str]]:
    if path is None:
        return set()
    data = load_json(path, "expected change log")
    raw_changes = data.get("changes", [])
    if not isinstance(raw_changes, list):
        raise ContainerDiffError("expected change log `changes` field must be an array")
    return {
        change_signature(change)
        for change in raw_changes
        if isinstance(change, dict)
        and as_string(change.get("entity_type"))
        and as_string(change.get("entity_id"))
        and as_string(change.get("change_type"))
    }


def build_change_log(
    original_path: Path,
    optimized_path: Path,
    changes: list[dict[str, Any]],
    unchanged: dict[str, dict[str, int]],
    warnings: list[str],
    expected_signatures: set[tuple[str, str, str]],
) -> dict[str, Any]:
    detected_signatures = {change_signature(change) for change in changes}
    missing_from_expected = sorted(detected_signatures - expected_signatures) if expected_signatures else []
    consistency_warnings = [
        f"Detected change is missing from expected change log: {entity_type} {entity_id} {change_type}."
        for entity_type, entity_id, change_type in missing_from_expected
    ]

    return {
        "artifact_type": "gtm_change_log",
        "schema_version": CHANGE_LOG_SCHEMA_VERSION,
        "source_file": original_path.name,
        "optimized_file": optimized_path.name,
        "generated_by": "scripts/diff_gtm_containers.py",
        "summary": summarize_changes(changes, unchanged),
        "changes": changes,
        "warnings": sorted(warnings + consistency_warnings),
        "manual_review_required": True,
        "human_approval_required": True,
        "safety": {
            "diff_modifies_live_gtm": False,
            "diff_publishes_gtm_changes": False,
            "human_review_required_before_import_or_publish": True,
            "deletions_are_high_risk": True,
        },
    }


def write_json(data: dict[str, Any], path: Path) -> None:
    if path.exists() and path.is_dir():
        raise ContainerDiffError(f"output path is a directory: {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(data, indent=2, sort_keys=True, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)

    try:
        original = load_json(args.original, "original")
        optimized = load_json(args.optimized, "optimized")
        expected_signatures = expected_change_signatures(args.expected_change_log)
        changes, unchanged, warnings = diff_containers(original, optimized)
        change_log = build_change_log(
            args.original,
            args.optimized,
            changes,
            unchanged,
            warnings,
            expected_signatures,
        )
        write_json(change_log, args.output)
    except ContainerDiffError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
