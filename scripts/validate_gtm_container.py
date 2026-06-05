"""Validate basic GTM container export structure and references."""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


REPORT_SCHEMA_VERSION = "0.1.0"
VARIABLE_TOKEN_PATTERN = re.compile(r"\{\{\s*([^{}]+?)\s*\}\}")


class ContainerValidationError(Exception):
    """Raised when validation cannot read the input or write the report."""


@dataclass(frozen=True)
class CheckResult:
    check_id: str
    status: str
    message: str


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Validate a Google Tag Manager container export JSON file for "
            "basic structure and detectable reference issues."
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
        type=Path,
        help=(
            "Path where the validation report JSON should be written. "
            "Prints to stdout if omitted."
        ),
    )
    return parser.parse_args(argv)


def make_check(check_id: str, status: str, message: str) -> CheckResult:
    return CheckResult(check_id=check_id, status=status, message=message)


def load_json(path: Path, checks: list[CheckResult]) -> dict[str, Any] | None:
    if not path.exists():
        checks.append(make_check("input-file", "fail", f"Input file does not exist: {path}"))
        return None
    if not path.is_file():
        checks.append(make_check("input-file", "fail", f"Input path is not a file: {path}"))
        return None

    checks.append(make_check("input-file", "pass", f"Input file exists: {path}"))

    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except UnicodeDecodeError:
        checks.append(make_check("json-parse", "fail", f"Input file is not valid UTF-8: {path}"))
        return None
    except json.JSONDecodeError as exc:
        checks.append(
            make_check(
                "json-parse",
                "fail",
                f"Invalid JSON at line {exc.lineno}, column {exc.colno}: {exc.msg}.",
            )
        )
        return None

    if not isinstance(data, dict):
        checks.append(make_check("json-root", "fail", "GTM export JSON root must be an object."))
        return None

    checks.append(make_check("json-parse", "pass", "Input parses as JSON."))
    checks.append(make_check("json-root", "pass", "GTM export JSON root is an object."))
    return data


def as_string(value: Any) -> str:
    if value is None:
        return ""
    return str(value).strip()


def as_string_list(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, list):
        return sorted(
            normalized for normalized in (as_string(item) for item in value) if normalized
        )
    normalized = as_string(value)
    return [normalized] if normalized else []


def first_string(source: dict[str, Any], keys: tuple[str, ...]) -> str:
    for key in keys:
        normalized = as_string(source.get(key))
        if normalized:
            return normalized
    return ""


def entity_label(entity: dict[str, Any], id_keys: tuple[str, ...]) -> str:
    entity_id = first_string(entity, id_keys)
    entity_name = first_string(entity, ("name", "displayName"))
    if entity_name and entity_id:
        return f"{entity_name} ({entity_id})"
    return entity_name or entity_id or "<unnamed>"


def ensure_array(
    container_version: dict[str, Any],
    section_name: str,
    checks: list[CheckResult],
    required: bool,
) -> list[dict[str, Any]]:
    value = container_version.get(section_name)

    if value is None:
        status = "fail" if required else "warn"
        noun = "required" if required else "optional"
        checks.append(
            make_check(
                f"section-{section_name}",
                status,
                f"{noun.title()} section `{section_name}` is missing.",
            )
        )
        return []

    if not isinstance(value, list):
        checks.append(
            make_check(
                f"section-{section_name}",
                "fail",
                f"Section `{section_name}` must be an array.",
            )
        )
        return []

    invalid_indexes = [str(index) for index, item in enumerate(value) if not isinstance(item, dict)]
    if invalid_indexes:
        checks.append(
            make_check(
                f"section-{section_name}",
                "fail",
                f"Section `{section_name}` contains non-object item(s) at index(es): "
                + ", ".join(invalid_indexes)
                + ".",
            )
        )
        return [item for item in value if isinstance(item, dict)]

    checks.append(
        make_check(
            f"section-{section_name}",
            "pass",
            f"Section `{section_name}` is an array with {len(value)} item(s).",
        )
    )
    return value


def collect_templates(
    container_version: dict[str, Any], checks: list[CheckResult]
) -> list[dict[str, Any]]:
    templates: list[dict[str, Any]] = []
    for section_name in ("customTemplate", "template"):
        if section_name in container_version:
            templates.extend(ensure_array(container_version, section_name, checks, required=False))
    if "customTemplate" not in container_version and "template" not in container_version:
        checks.append(make_check("section-templates", "warn", "Optional template sections are missing."))
    return templates


def validate_top_level(export: dict[str, Any], checks: list[CheckResult]) -> dict[str, Any] | None:
    if "exportFormatVersion" not in export:
        checks.append(
            make_check(
                "top-level-export-format-version",
                "fail",
                "Top-level `exportFormatVersion` is missing.",
            )
        )
    elif not isinstance(export.get("exportFormatVersion"), int):
        checks.append(
            make_check(
                "top-level-export-format-version",
                "fail",
                "Top-level `exportFormatVersion` must be an integer.",
            )
        )
    else:
        checks.append(
            make_check(
                "top-level-export-format-version",
                "pass",
                "Top-level `exportFormatVersion` is present.",
            )
        )

    container_version = export.get("containerVersion")
    if not isinstance(container_version, dict):
        checks.append(
            make_check(
                "top-level-container-version",
                "fail",
                "Top-level `containerVersion` object is missing.",
            )
        )
        return None

    checks.append(
        make_check(
            "top-level-container-version",
            "pass",
            "Top-level `containerVersion` object is present.",
        )
    )

    container = container_version.get("container")
    if isinstance(container, dict):
        checks.append(
            make_check(
                "container-metadata",
                "pass",
                "`containerVersion.container` metadata object is present.",
            )
        )
    else:
        metadata_keys = ("accountId", "containerId", "name")
        present_keys = [key for key in metadata_keys if as_string(container_version.get(key))]
        if present_keys:
            checks.append(
                make_check(
                    "container-metadata",
                    "warn",
                    "`containerVersion.container` metadata object is missing, but "
                    "containerVersion metadata fields are present.",
                )
            )
        else:
            checks.append(
                make_check(
                    "container-metadata",
                    "fail",
                    "Container metadata is missing from `containerVersion.container` "
                    "and containerVersion fields.",
                )
            )

    return container_version


def build_id_map(
    entities: list[dict[str, Any]],
    entity_type: str,
    id_keys: tuple[str, ...],
    checks: list[CheckResult],
) -> dict[str, dict[str, Any]]:
    by_id: dict[str, dict[str, Any]] = {}
    errors: list[str] = []

    for entity in entities:
        entity_id = first_string(entity, id_keys)
        if not entity_id:
            errors.append(f"{entity_type} `{entity_label(entity, id_keys)}` is missing an ID")
        elif entity_id in by_id:
            errors.append(f"Duplicate {entity_type} ID `{entity_id}`")
        else:
            by_id[entity_id] = entity

    if errors:
        checks.append(make_check(f"{entity_type}-ids", "fail", "; ".join(sorted(errors)) + "."))
    else:
        checks.append(
            make_check(
                f"{entity_type}-ids",
                "pass",
                f"{entity_type.title()} IDs are present and unique.",
            )
        )

    return by_id


def collect_variable_names(variables: list[dict[str, Any]], built_ins: list[dict[str, Any]]) -> set[str]:
    names: set[str] = set()

    for variable in variables:
        name = first_string(variable, ("name", "displayName"))
        if name:
            names.add(name)

    for built_in in built_ins:
        for key in ("name", "displayName", "type"):
            name = as_string(built_in.get(key))
            if name:
                names.add(name)

    return names


def iter_strings(value: Any) -> list[str]:
    strings: list[str] = []
    if isinstance(value, str):
        strings.append(value)
    elif isinstance(value, list):
        for item in value:
            strings.extend(iter_strings(item))
    elif isinstance(value, dict):
        for item in value.values():
            strings.extend(iter_strings(item))
    return strings


def find_variable_tokens(entity: dict[str, Any]) -> set[str]:
    tokens: set[str] = set()
    for value in iter_strings(entity):
        tokens.update(token.strip() for token in VARIABLE_TOKEN_PATTERN.findall(value) if token.strip())
    return tokens


def validate_tag_trigger_references(
    tags: list[dict[str, Any]],
    trigger_ids: set[str],
    checks: list[CheckResult],
) -> None:
    errors: list[str] = []

    for tag in tags:
        label = entity_label(tag, ("tagId", "tag_id", "id"))
        for field_name in ("firingTriggerId", "blockingTriggerId"):
            for trigger_id in as_string_list(tag.get(field_name)):
                if trigger_id not in trigger_ids:
                    errors.append(
                        f"tag `{label}` references missing trigger ID `{trigger_id}` "
                        f"in `{field_name}`"
                    )

    if errors:
        checks.append(make_check("tag-trigger-references", "fail", "; ".join(sorted(errors)) + "."))
    else:
        checks.append(
            make_check(
                "tag-trigger-references",
                "pass",
                "Tag trigger references resolve to existing triggers.",
            )
        )


def validate_folder_references(
    grouped_entities: tuple[tuple[str, list[dict[str, Any]], tuple[str, ...]], ...],
    folder_ids: set[str],
    checks: list[CheckResult],
) -> None:
    errors: list[str] = []

    for entity_type, entities, id_keys in grouped_entities:
        for entity in entities:
            folder_id = first_string(entity, ("parentFolderId", "parent_folder_id"))
            if folder_id and folder_id not in folder_ids:
                errors.append(
                    f"{entity_type} `{entity_label(entity, id_keys)}` "
                    f"references missing folder ID `{folder_id}`"
                )

    if errors:
        checks.append(make_check("folder-references", "fail", "; ".join(sorted(errors)) + "."))
    else:
        checks.append(
            make_check(
                "folder-references",
                "pass",
                "Detectable folder references resolve to existing folders.",
            )
        )


def validate_variable_references(
    grouped_entities: tuple[tuple[str, list[dict[str, Any]], tuple[str, ...]], ...],
    variable_names: set[str],
    checks: list[CheckResult],
) -> None:
    errors: list[str] = []

    for entity_type, entities, id_keys in grouped_entities:
        for entity in entities:
            label = entity_label(entity, id_keys)
            for token in sorted(find_variable_tokens(entity)):
                if token not in variable_names:
                    errors.append(f"{entity_type} `{label}` references missing variable `{{{{{token}}}}}`")

    if errors:
        checks.append(make_check("variable-references", "fail", "; ".join(sorted(errors)) + "."))
    else:
        checks.append(
            make_check(
                "variable-references",
                "pass",
                "Detectable variable references resolve to defined or enabled variables.",
            )
        )


def infer_validation_status(checks: list[CheckResult]) -> str:
    if any(check.status == "fail" for check in checks):
        return "fail"
    if any(check.status == "warn" for check in checks):
        return "warn"
    return "pass"


def build_report(source_file: str, checks: list[CheckResult], counts: dict[str, int]) -> dict[str, Any]:
    return {
        "artifact_type": "gtm_container_validation_report",
        "schema_version": REPORT_SCHEMA_VERSION,
        "source_file": source_file,
        "validation_status": infer_validation_status(checks),
        "counts": counts,
        "checks": [
            {
                "check_id": check.check_id,
                "status": check.status,
                "message": check.message,
            }
            for check in checks
        ],
        "errors": sorted(check.message for check in checks if check.status == "fail"),
        "warnings": sorted(check.message for check in checks if check.status == "warn"),
        "safety": {
            "validator_modifies_live_gtm": False,
            "validator_publishes_gtm_changes": False,
            "human_review_required_before_import_or_publish": True,
        },
    }


def validate_container(
    export: dict[str, Any] | None, source_file: str, checks: list[CheckResult]
) -> dict[str, Any]:
    counts = {
        "tags": 0,
        "triggers": 0,
        "variables": 0,
        "folders": 0,
        "built_in_variables": 0,
        "templates": 0,
    }

    if export is None:
        return build_report(source_file, checks, counts)

    container_version = validate_top_level(export, checks)
    if container_version is None:
        return build_report(source_file, checks, counts)

    tags = ensure_array(container_version, "tag", checks, required=True)
    triggers = ensure_array(container_version, "trigger", checks, required=True)
    variables = ensure_array(container_version, "variable", checks, required=True)
    folders = ensure_array(container_version, "folder", checks, required=False)
    built_ins = ensure_array(container_version, "builtInVariable", checks, required=False)
    templates = collect_templates(container_version, checks)

    counts.update(
        {
            "tags": len(tags),
            "triggers": len(triggers),
            "variables": len(variables),
            "folders": len(folders),
            "built_in_variables": len(built_ins),
            "templates": len(templates),
        }
    )

    tag_ids = build_id_map(tags, "tag", ("tagId", "tag_id", "id"), checks)
    trigger_ids = build_id_map(triggers, "trigger", ("triggerId", "trigger_id", "id"), checks)
    variable_ids = build_id_map(variables, "variable", ("variableId", "variable_id", "id"), checks)
    folder_ids = build_id_map(folders, "folder", ("folderId", "folder_id", "id"), checks)
    build_id_map(templates, "template", ("templateId", "template_id", "id"), checks)

    entity_groups = (
        ("tag", tags, ("tagId", "tag_id", "id")),
        ("trigger", triggers, ("triggerId", "trigger_id", "id")),
        ("variable", variables, ("variableId", "variable_id", "id")),
    )

    validate_tag_trigger_references(tags, set(trigger_ids), checks)
    validate_folder_references(entity_groups, set(folder_ids), checks)
    validate_variable_references(entity_groups, collect_variable_names(variables, built_ins), checks)

    if tag_ids or trigger_ids or variable_ids:
        checks.append(
            make_check(
                "entity-inventory",
                "pass",
                "At least one tag, trigger, or variable entity was detected.",
            )
        )
    else:
        checks.append(
            make_check(
                "entity-inventory",
                "warn",
                "No tag, trigger, or variable entities were detected.",
            )
        )

    return build_report(source_file, checks, counts)


def write_json(data: dict[str, Any], path: Path | None) -> None:
    serialized = json.dumps(data, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
    if path is None:
        print(serialized, end="")
        return

    if path.exists() and path.is_dir():
        raise ContainerValidationError(f"output path is a directory: {path}")

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(serialized, encoding="utf-8")


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    checks: list[CheckResult] = []

    try:
        export = load_json(args.input, checks)
        report = validate_container(export, args.input.name, checks)
        write_json(report, args.output)
    except ContainerValidationError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    return 1 if report["validation_status"] == "fail" else 0


if __name__ == "__main__":
    raise SystemExit(main())
