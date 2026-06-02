"""Normalize a GTM container export into a deterministic summary JSON."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


SUMMARY_SCHEMA_VERSION = "0.1.0"


class NormalizationError(Exception):
    """Raised when a GTM export cannot be normalized."""


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Read a Google Tag Manager container export JSON file and write a "
            "deterministic normalized summary JSON for audit and diff workflows."
        )
    )
    parser.add_argument(
        "--input",
        required=True,
        type=Path,
        help="Path to the source GTM container export JSON file.",
    )
    parser.add_argument(
        "--output",
        required=True,
        type=Path,
        help="Path where the normalized summary JSON should be written.",
    )
    return parser.parse_args(argv)


def load_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        raise NormalizationError(f"input file does not exist: {path}")
    if not path.is_file():
        raise NormalizationError(f"input path is not a file: {path}")

    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except UnicodeDecodeError as exc:
        raise NormalizationError(f"input file is not valid UTF-8: {path}") from exc
    except json.JSONDecodeError as exc:
        raise NormalizationError(
            f"invalid JSON in {path}: line {exc.lineno}, column {exc.colno}: {exc.msg}"
        ) from exc

    if not isinstance(data, dict):
        raise NormalizationError("GTM export JSON root must be an object")

    return data


def as_string(value: Any) -> str:
    if value is None:
        return ""
    return str(value).strip()


def first_string(source: dict[str, Any], keys: tuple[str, ...]) -> str:
    for key in keys:
        value = source.get(key)
        normalized = as_string(value)
        if normalized:
            return normalized
    return ""


def ensure_list(value: Any, section_name: str, warnings: list[str]) -> list[dict[str, Any]]:
    if value is None:
        warnings.append(f"Section `{section_name}` is missing; count set to 0.")
        return []
    if not isinstance(value, list):
        warnings.append(f"Section `{section_name}` is not an array; count set to 0.")
        return []

    items: list[dict[str, Any]] = []
    for index, item in enumerate(value):
        if isinstance(item, dict):
            items.append(item)
        else:
            warnings.append(
                f"Section `{section_name}` item {index} is not an object and was skipped."
            )
    return items


def as_string_list(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, list):
        return sorted(value for value in (as_string(item) for item in value) if value)
    normalized = as_string(value)
    return [normalized] if normalized else []


def get_container_version(export: dict[str, Any], warnings: list[str]) -> dict[str, Any]:
    container_version = export.get("containerVersion")
    if isinstance(container_version, dict):
        return container_version

    warnings.append(
        "Top-level `containerVersion` object is missing; treating root object as container version."
    )
    return export


def collect_templates(container_version: dict[str, Any], warnings: list[str]) -> list[dict[str, Any]]:
    templates: list[dict[str, Any]] = []
    custom_templates = container_version.get("customTemplate")
    legacy_templates = container_version.get("template")

    if custom_templates is None and legacy_templates is None:
        warnings.append("Sections `customTemplate` and `template` are missing; template count set to 0.")
        return templates

    if custom_templates is not None:
        templates.extend(ensure_list(custom_templates, "customTemplate", warnings))
    if legacy_templates is not None:
        templates.extend(ensure_list(legacy_templates, "template", warnings))
    return templates


def sort_entities(entities: list[dict[str, Any]], id_keys: tuple[str, ...]) -> list[dict[str, Any]]:
    return sorted(
        entities,
        key=lambda item: (
            first_string(item, id_keys),
            first_string(item, ("name", "displayName", "type")),
            json.dumps(item, sort_keys=True, separators=(",", ":")),
        ),
    )


def entity_summary(
    entity: dict[str, Any],
    id_keys: tuple[str, ...],
    include_triggers: bool = False,
) -> dict[str, Any]:
    summary: dict[str, Any] = {
        "id": first_string(entity, id_keys),
        "name": first_string(entity, ("name", "displayName")),
        "type": first_string(entity, ("type",)),
        "parent_folder_id": first_string(entity, ("parentFolderId", "parent_folder_id")),
        "fingerprint": first_string(entity, ("fingerprint",)),
    }

    if include_triggers:
        summary["firing_trigger_ids"] = as_string_list(entity.get("firingTriggerId"))
        summary["blocking_trigger_ids"] = as_string_list(entity.get("blockingTriggerId"))

    return summary


def build_entity_lookups(
    entities: list[dict[str, Any]],
    entity_label: str,
    id_keys: tuple[str, ...],
    warnings: list[str],
    include_triggers: bool = False,
) -> tuple[dict[str, dict[str, Any]], dict[str, list[str]]]:
    by_id: dict[str, dict[str, Any]] = {}
    by_name: dict[str, list[str]] = {}

    for entity in sort_entities(entities, id_keys):
        summary = entity_summary(entity, id_keys, include_triggers=include_triggers)
        entity_id = summary["id"]
        entity_name = summary["name"]

        if not entity_id:
            warnings.append(f"{entity_label} `{entity_name or '<unnamed>'}` is missing an ID.")
        elif entity_id in by_id:
            warnings.append(f"Duplicate {entity_label} ID `{entity_id}` detected.")
        else:
            by_id[entity_id] = summary

        if entity_name:
            by_name.setdefault(entity_name, [])
            if entity_id:
                by_name[entity_name].append(entity_id)

    sorted_by_id = {key: by_id[key] for key in sorted(by_id)}
    sorted_by_name = {
        key: sorted(value) for key, value in sorted(by_name.items(), key=lambda item: item[0])
    }
    return sorted_by_id, sorted_by_name


def normalize_gtm_export(export: dict[str, Any], source_file: str) -> dict[str, Any]:
    warnings: list[str] = []
    container_version = get_container_version(export, warnings)
    container = container_version.get("container")
    if not isinstance(container, dict):
        warnings.append("Container metadata object is missing; using available containerVersion metadata.")
        container = container_version

    tags = ensure_list(container_version.get("tag"), "tag", warnings)
    triggers = ensure_list(container_version.get("trigger"), "trigger", warnings)
    variables = ensure_list(container_version.get("variable"), "variable", warnings)
    folders = ensure_list(container_version.get("folder"), "folder", warnings)
    built_in_variables = ensure_list(
        container_version.get("builtInVariable"), "builtInVariable", warnings
    )
    templates = collect_templates(container_version, warnings)

    tags_by_id, tags_by_name = build_entity_lookups(
        tags, "tag", ("tagId", "tag_id", "id"), warnings, include_triggers=True
    )
    triggers_by_id, triggers_by_name = build_entity_lookups(
        triggers, "trigger", ("triggerId", "trigger_id", "id"), warnings
    )
    variables_by_id, variables_by_name = build_entity_lookups(
        variables, "variable", ("variableId", "variable_id", "id"), warnings
    )
    folders_by_id, folders_by_name = build_entity_lookups(
        folders, "folder", ("folderId", "folder_id", "id"), warnings
    )
    templates_by_id, templates_by_name = build_entity_lookups(
        templates, "template", ("templateId", "template_id", "id"), warnings
    )

    built_ins_by_type = {
        first_string(item, ("type", "name")): entity_summary(item, ("type", "name"))
        for item in sort_entities(built_in_variables, ("type", "name"))
        if first_string(item, ("type", "name"))
    }

    return {
        "artifact_type": "gtm_normalized_summary",
        "schema_version": SUMMARY_SCHEMA_VERSION,
        "source_file": source_file,
        "container": {
            "name": first_string(container, ("name",)),
            "public_id": first_string(container, ("publicId", "public_id")),
            "container_id": first_string(container, ("containerId", "container_id")),
            "account_id": first_string(container, ("accountId", "account_id")),
        },
        "export": {
            "export_format_version": first_string(export, ("exportFormatVersion",)),
            "export_time": first_string(export, ("exportTime",)),
        },
        "counts": {
            "tags": len(tags),
            "triggers": len(triggers),
            "variables": len(variables),
            "folders": len(folders),
            "built_in_variables": len(built_in_variables),
            "templates": len(templates),
        },
        "lookups": {
            "tags_by_id": tags_by_id,
            "tags_by_name": tags_by_name,
            "triggers_by_id": triggers_by_id,
            "triggers_by_name": triggers_by_name,
            "variables_by_id": variables_by_id,
            "variables_by_name": variables_by_name,
            "folders_by_id": folders_by_id,
            "folders_by_name": folders_by_name,
            "built_in_variables_by_type": built_ins_by_type,
            "templates_by_id": templates_by_id,
            "templates_by_name": templates_by_name,
        },
        "entities": {
            "tags": sort_entities(tags, ("tagId", "tag_id", "id")),
            "triggers": sort_entities(triggers, ("triggerId", "trigger_id", "id")),
            "variables": sort_entities(variables, ("variableId", "variable_id", "id")),
            "folders": sort_entities(folders, ("folderId", "folder_id", "id")),
            "built_in_variables": sort_entities(built_in_variables, ("type", "name")),
            "templates": sort_entities(templates, ("templateId", "template_id", "id")),
        },
        "safety": {
            "human_review_required_before_import_or_publish": True,
            "normalization_modifies_live_gtm": False,
            "normalization_certifies_tracking_correctness": False,
        },
        "warnings": sorted(warnings),
    }


def write_json(data: dict[str, Any], path: Path) -> None:
    if path.exists() and path.is_dir():
        raise NormalizationError(f"output path is a directory: {path}")

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(data, indent=2, sort_keys=True, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)

    try:
        export = load_json(args.input)
        summary = normalize_gtm_export(export, args.input.name)
        write_json(summary, args.output)
    except NormalizationError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
