"""Validate a GTM Container Audit & Patch Package directory."""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any

try:  # Prefer the full JSON Schema implementation when it is available.
    from jsonschema import Draft7Validator, FormatChecker
except ImportError:  # pragma: no cover - exercised only in dependency-light environments.
    Draft7Validator = None  # type: ignore[assignment]
    FormatChecker = None  # type: ignore[assignment]


VALIDATION_REPORT_SCHEMA_VERSION = "1.0.0"
DEFAULT_CHECKED_AT = "1970-01-01T00:00:00Z"

REQUIRED_FILES: tuple[str, ...] = (
    "optimized_container.json",
    "audit_report.md",
    "audit_report.json",
    "change_log.json",
    "validation_report.json",
    "qa_checklist.md",
    "run_metadata.json",
)

JSON_FILES: tuple[str, ...] = (
    "optimized_container.json",
    "audit_report.json",
    "change_log.json",
    "validation_report.json",
    "run_metadata.json",
)

MARKDOWN_FILES: tuple[str, ...] = (
    "audit_report.md",
    "qa_checklist.md",
)

SCHEMA_FILES: dict[str, str] = {
    "audit_report.json": "gtm_audit_report.schema.json",
    "change_log.json": "gtm_change_log.schema.json",
    "validation_report.json": "validation_report.schema.json",
}


class OutputPackageValidationError(Exception):
    """Raised when validation cannot run or the report cannot be written."""


@dataclass(frozen=True)
class CheckResult:
    check_id: str
    status: str
    message: str


def default_schemas_dir() -> Path:
    return Path(__file__).resolve().parents[1] / "schemas"


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Validate a GTM Container Audit & Patch Package directory and write "
            "a validation_report.json-compatible report."
        )
    )
    parser.add_argument(
        "--package-dir",
        required=True,
        type=Path,
        help="Path to the package directory containing the required output artifacts.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        help=(
            "Path where the validation report should be written. If omitted, "
            "the report is printed to stdout."
        ),
    )
    parser.add_argument(
        "--schemas-dir",
        type=Path,
        default=default_schemas_dir(),
        help="Directory containing the repo JSON Schemas.",
    )
    parser.add_argument(
        "--checked-at",
        default=DEFAULT_CHECKED_AT,
        help=(
            "RFC 3339 timestamp to use for every check. The default is a "
            "deterministic placeholder for repeatable smoke tests."
        ),
    )
    return parser.parse_args(argv)


def is_date_time(value: str) -> bool:
    try:
        datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return False
    return True


def read_json(path: Path) -> tuple[dict[str, Any] | None, str | None]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except UnicodeDecodeError:
        return None, f"{path.name} is not valid UTF-8."
    except json.JSONDecodeError as exc:
        return None, (
            f"{path.name} contains invalid JSON at line {exc.lineno}, "
            f"column {exc.colno}: {exc.msg}."
        )

    if not isinstance(data, dict):
        return None, f"{path.name} JSON root must be an object."

    return data, None


def load_schema(path: Path) -> tuple[dict[str, Any] | None, str | None]:
    if not path.exists():
        return None, f"schema file is missing: {path}"
    if not path.is_file():
        return None, f"schema path is not a file: {path}"
    return read_json(path)


def make_check(check_id: str, status: str, message: str) -> CheckResult:
    return CheckResult(check_id=check_id, status=status, message=message)


def format_json_path(parts: list[Any]) -> str:
    if not parts:
        return "<root>"

    path = ""
    for part in parts:
        if isinstance(part, int):
            path += f"[{part}]"
        else:
            path += f".{part}" if path else str(part)
    return path


def format_schema_errors(label: str, errors: list[str], limit: int = 8) -> str:
    visible = errors[:limit]
    message = f"{label} schema validation failed: " + "; ".join(visible)
    if len(errors) > limit:
        message += f"; and {len(errors) - limit} more error(s)"
    return message


def validate_with_jsonschema(
    instance: dict[str, Any], schema: dict[str, Any], label: str
) -> list[str]:
    if Draft7Validator is None or FormatChecker is None:
        return []

    validator = Draft7Validator(schema, format_checker=FormatChecker())
    sorted_errors = sorted(
        validator.iter_errors(instance),
        key=lambda error: (list(error.absolute_path), error.message),
    )
    return [
        f"{label} at {format_json_path(list(error.absolute_path))}: {error.message}"
        for error in sorted_errors
    ]


def resolve_ref(root_schema: dict[str, Any], ref: str) -> dict[str, Any]:
    if not ref.startswith("#/"):
        raise OutputPackageValidationError(f"unsupported schema reference: {ref}")

    current: Any = root_schema
    for raw_part in ref[2:].split("/"):
        part = raw_part.replace("~1", "/").replace("~0", "~")
        if not isinstance(current, dict) or part not in current:
            raise OutputPackageValidationError(f"unresolvable schema reference: {ref}")
        current = current[part]

    if not isinstance(current, dict):
        raise OutputPackageValidationError(f"schema reference does not point to an object: {ref}")

    return current


def instance_matches_type(instance: Any, expected_type: str) -> bool:
    if expected_type == "object":
        return isinstance(instance, dict)
    if expected_type == "array":
        return isinstance(instance, list)
    if expected_type == "string":
        return isinstance(instance, str)
    if expected_type == "integer":
        return isinstance(instance, int) and not isinstance(instance, bool)
    if expected_type == "number":
        return isinstance(instance, (int, float)) and not isinstance(instance, bool)
    if expected_type == "boolean":
        return isinstance(instance, bool)
    if expected_type == "null":
        return instance is None
    return True


def validate_schema_builtin(
    instance: Any,
    schema: dict[str, Any],
    root_schema: dict[str, Any],
    path: list[Any] | None = None,
) -> list[str]:
    path = [] if path is None else path
    errors: list[str] = []

    if "$ref" in schema:
        return validate_schema_builtin(instance, resolve_ref(root_schema, schema["$ref"]), root_schema, path)

    for subschema in schema.get("allOf", []):
        if isinstance(subschema, dict):
            errors.extend(validate_schema_builtin(instance, subschema, root_schema, path))

    if "const" in schema and instance != schema["const"]:
        errors.append(
            f"at {format_json_path(path)}: expected constant {schema['const']!r}, got {instance!r}"
        )

    if "enum" in schema and instance not in schema["enum"]:
        errors.append(f"at {format_json_path(path)}: {instance!r} is not one of {schema['enum']!r}")

    expected_type = schema.get("type")
    if expected_type is not None:
        expected_types = expected_type if isinstance(expected_type, list) else [expected_type]
        if not any(instance_matches_type(instance, item) for item in expected_types):
            errors.append(
                f"at {format_json_path(path)}: expected type {expected_types!r}, "
                f"got {type(instance).__name__}"
            )
            return errors

    if isinstance(instance, dict):
        required = schema.get("required", [])
        for key in required:
            if key not in instance:
                errors.append(f"at {format_json_path(path)}: missing required property {key!r}")

        properties = schema.get("properties", {})
        if isinstance(properties, dict):
            for key, value in instance.items():
                if key in properties and isinstance(properties[key], dict):
                    errors.extend(
                        validate_schema_builtin(value, properties[key], root_schema, path + [key])
                    )

            if schema.get("additionalProperties") is False:
                extra_keys = sorted(key for key in instance if key not in properties)
                for key in extra_keys:
                    errors.append(
                        f"at {format_json_path(path)}: additional property {key!r} is not allowed"
                    )

    if isinstance(instance, list):
        items_schema = schema.get("items")
        if isinstance(items_schema, dict):
            for index, item in enumerate(instance):
                errors.extend(validate_schema_builtin(item, items_schema, root_schema, path + [index]))

    if isinstance(instance, str):
        min_length = schema.get("minLength")
        if isinstance(min_length, int) and len(instance) < min_length:
            errors.append(
                f"at {format_json_path(path)}: string is shorter than {min_length} character(s)"
            )

        pattern = schema.get("pattern")
        if isinstance(pattern, str) and re.search(pattern, instance) is None:
            errors.append(f"at {format_json_path(path)}: string does not match pattern {pattern!r}")

        if schema.get("format") == "date-time" and not is_date_time(instance):
            errors.append(f"at {format_json_path(path)}: value is not a valid date-time")

    if isinstance(instance, (int, float)) and not isinstance(instance, bool):
        minimum = schema.get("minimum")
        if isinstance(minimum, (int, float)) and instance < minimum:
            errors.append(f"at {format_json_path(path)}: value is less than minimum {minimum}")

    return errors


def validate_schema(instance: dict[str, Any], schema: dict[str, Any], label: str) -> list[str]:
    if Draft7Validator is not None and FormatChecker is not None:
        return validate_with_jsonschema(instance, schema, label)

    return validate_schema_builtin(instance, schema, schema)


def validate_required_files(package_dir: Path, checks: list[CheckResult]) -> None:
    if not package_dir.exists():
        checks.append(make_check("package-dir", "fail", f"Package directory does not exist: {package_dir}"))
        return
    if not package_dir.is_dir():
        checks.append(make_check("package-dir", "fail", f"Package path is not a directory: {package_dir}"))
        return

    checks.append(make_check("package-dir", "pass", f"Package directory exists: {package_dir}"))

    missing = [file_name for file_name in REQUIRED_FILES if not (package_dir / file_name).exists()]
    if missing:
        checks.append(
            make_check("required-files", "fail", "Missing required file(s): " + ", ".join(missing))
        )
    else:
        checks.append(make_check("required-files", "pass", "All required package files are present."))

    bad_paths: list[str] = []
    for file_name in REQUIRED_FILES:
        path = package_dir / file_name
        if not path.exists():
            continue
        if not path.is_file():
            bad_paths.append(f"{file_name} is not a file")
        elif path.stat().st_size == 0:
            bad_paths.append(f"{file_name} is empty")

    if bad_paths:
        checks.append(make_check("required-files-readable", "fail", "; ".join(bad_paths) + "."))
    else:
        checks.append(
            make_check(
                "required-files-readable",
                "pass",
                "Present required files are readable and non-empty.",
            )
        )


def load_package_json(
    package_dir: Path, checks: list[CheckResult]
) -> dict[str, dict[str, Any]]:
    artifacts: dict[str, dict[str, Any]] = {}

    for file_name in JSON_FILES:
        path = package_dir / file_name
        if not path.exists() or not path.is_file():
            checks.append(
                make_check(
                    f"json-parse-{file_name}",
                    "not_run",
                    f"{file_name} was not parsed because the file is missing or unreadable.",
                )
            )
            continue

        data, error = read_json(path)
        if error:
            checks.append(make_check(f"json-parse-{file_name}", "fail", error))
            continue

        artifacts[file_name] = data if data is not None else {}
        checks.append(make_check(f"json-parse-{file_name}", "pass", f"{file_name} parses as JSON."))

    return artifacts


def validate_markdown_files(package_dir: Path, checks: list[CheckResult]) -> None:
    missing_or_empty: list[str] = []
    for file_name in MARKDOWN_FILES:
        path = package_dir / file_name
        if not path.exists() or not path.is_file():
            missing_or_empty.append(f"{file_name} is missing")
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            missing_or_empty.append(f"{file_name} is not valid UTF-8")
            continue
        if not text.strip():
            missing_or_empty.append(f"{file_name} is empty")

    if missing_or_empty:
        checks.append(make_check("markdown-artifacts", "fail", "; ".join(missing_or_empty) + "."))
    else:
        checks.append(make_check("markdown-artifacts", "pass", "Markdown artifacts are present and non-empty."))


def validate_schema_backed_artifacts(
    artifacts: dict[str, dict[str, Any]], schemas_dir: Path, checks: list[CheckResult]
) -> None:
    for artifact_file, schema_file in SCHEMA_FILES.items():
        artifact = artifacts.get(artifact_file)
        if artifact is None:
            checks.append(
                make_check(
                    f"schema-{artifact_file}",
                    "not_run",
                    f"{artifact_file} schema validation was skipped because the artifact was not parsed.",
                )
            )
            continue

        schema, schema_error = load_schema(schemas_dir / schema_file)
        if schema_error:
            checks.append(make_check(f"schema-{artifact_file}", "fail", schema_error))
            continue

        schema_errors = validate_schema(artifact, schema or {}, artifact_file)
        if schema_errors:
            checks.append(
                make_check(
                    f"schema-{artifact_file}",
                    "fail",
                    format_schema_errors(artifact_file, schema_errors),
                )
            )
        else:
            checks.append(
                make_check(
                    f"schema-{artifact_file}",
                    "pass",
                    f"{artifact_file} matches {schema_file}.",
                )
            )


def validate_optimized_container(
    artifacts: dict[str, dict[str, Any]], checks: list[CheckResult]
) -> None:
    optimized_container = artifacts.get("optimized_container.json")
    if optimized_container is None:
        checks.append(
            make_check(
                "optimized-container-basic",
                "not_run",
                "optimized_container.json was not checked because it was not parsed.",
            )
        )
        return

    if "containerVersion" in optimized_container or "exportFormatVersion" in optimized_container:
        checks.append(
            make_check(
                "optimized-container-basic",
                "pass",
                "optimized_container.json has GTM export-like top-level fields.",
            )
        )
    else:
        checks.append(
            make_check(
                "optimized-container-basic",
                "warn",
                "optimized_container.json parses, but no GTM export-like top-level fields were found.",
            )
        )


def validate_run_metadata(
    artifacts: dict[str, dict[str, Any]], checks: list[CheckResult]
) -> None:
    metadata = artifacts.get("run_metadata.json")
    if metadata is None:
        checks.append(
            make_check(
                "run-metadata",
                "not_run",
                "run_metadata.json was not checked because it was not parsed.",
            )
        )
        return

    errors: list[str] = []
    warnings: list[str] = []

    if not isinstance(metadata.get("run_id"), str) or not metadata.get("run_id", "").strip():
        errors.append("run_metadata.json must include a non-empty run_id")

    timestamp = metadata.get("created_at", metadata.get("timestamp"))
    if not isinstance(timestamp, str) or not timestamp.strip():
        errors.append("run_metadata.json must include created_at or timestamp")
    elif not is_date_time(timestamp):
        errors.append("run_metadata.json created_at/timestamp must be a valid date-time")

    input_files = metadata.get("input_files")
    if not isinstance(input_files, list) or not all(isinstance(item, str) and item for item in input_files):
        errors.append("run_metadata.json input_files must be a non-empty string array")

    if not isinstance(metadata.get("mlp_version"), str) or not metadata.get("mlp_version", "").strip():
        errors.append("run_metadata.json must include a non-empty mlp_version")

    if "tool_version" not in metadata and "gpt_version" not in metadata:
        errors.append("run_metadata.json must include tool_version or gpt_version")

    if "standards_applied" not in metadata:
        warnings.append("run_metadata.json does not list standards_applied")

    if errors:
        checks.append(make_check("run-metadata", "fail", "; ".join(errors) + "."))
    elif warnings:
        checks.append(make_check("run-metadata", "warn", "; ".join(warnings) + "."))
    else:
        checks.append(make_check("run-metadata", "pass", "run_metadata.json includes required run context."))


def collect_ids(items: Any, id_key: str) -> set[str]:
    if not isinstance(items, list):
        return set()
    return {item[id_key] for item in items if isinstance(item, dict) and isinstance(item.get(id_key), str)}


def validate_run_id_consistency(
    artifacts: dict[str, dict[str, Any]], package_dir: Path, checks: list[CheckResult]
) -> str:
    run_ids: dict[str, str] = {}
    for file_name in ("run_metadata.json", "audit_report.json", "change_log.json", "validation_report.json"):
        artifact = artifacts.get(file_name)
        if isinstance(artifact, dict):
            run_id = artifact.get("run_id")
            if isinstance(run_id, str) and run_id.strip():
                run_ids[file_name] = run_id.strip()

    if not run_ids:
        checks.append(
            make_check(
                "consistency-run-id",
                "fail",
                "No non-empty run_id was found in package JSON artifacts.",
            )
        )
        return package_dir.name or "unknown-package"

    unique_run_ids = sorted(set(run_ids.values()))
    if len(unique_run_ids) > 1:
        details = ", ".join(f"{name}={value}" for name, value in sorted(run_ids.items()))
        checks.append(
            make_check(
                "consistency-run-id",
                "fail",
                f"run_id values do not match across artifacts: {details}.",
            )
        )
    else:
        checks.append(
            make_check(
                "consistency-run-id",
                "pass",
                f"run_id is consistent across parsed artifacts: {unique_run_ids[0]}.",
            )
        )

    return run_ids.get("run_metadata.json") or unique_run_ids[0]


def validate_client_id_consistency(
    artifacts: dict[str, dict[str, Any]], checks: list[CheckResult]
) -> None:
    client_ids: dict[str, str | None] = {}
    for file_name in ("run_metadata.json", "audit_report.json", "change_log.json"):
        artifact = artifacts.get(file_name)
        if isinstance(artifact, dict) and "client_id" in artifact:
            value = artifact.get("client_id")
            if value is None or isinstance(value, str):
                client_ids[file_name] = value

    non_null_values = sorted({value for value in client_ids.values() if value is not None})
    if len(non_null_values) > 1:
        details = ", ".join(f"{name}={value!r}" for name, value in sorted(client_ids.items()))
        checks.append(
            make_check(
                "consistency-client-id",
                "fail",
                f"client_id values do not match across artifacts: {details}.",
            )
        )
    elif client_ids:
        checks.append(
            make_check(
                "consistency-client-id",
                "pass",
                "client_id values are consistent across parsed artifacts.",
            )
        )
    else:
        checks.append(
            make_check(
                "consistency-client-id",
                "pass",
                "No client_id was provided; client_id consistency check passed.",
            )
        )


def validate_summary_counts(
    artifacts: dict[str, dict[str, Any]], checks: list[CheckResult]
) -> None:
    if "audit_report.json" not in artifacts or "change_log.json" not in artifacts:
        checks.append(
            make_check(
                "consistency-summary-counts",
                "not_run",
                "Summary count consistency was skipped because audit_report.json or change_log.json was not parsed.",
            )
        )
        return

    errors: list[str] = []

    audit_report = artifacts.get("audit_report.json", {})
    audit_summary = audit_report.get("audit_summary") if isinstance(audit_report, dict) else None
    findings = audit_report.get("findings") if isinstance(audit_report, dict) else None
    if isinstance(audit_summary, dict) and isinstance(findings, list):
        expected = len(findings)
        actual = audit_summary.get("finding_count")
        if actual != expected:
            errors.append(f"audit_summary.finding_count is {actual!r}; expected {expected}")

    change_log = artifacts.get("change_log.json", {})
    changes = change_log.get("changes") if isinstance(change_log, dict) else None
    summary = change_log.get("summary") if isinstance(change_log, dict) else None
    if isinstance(summary, dict) and isinstance(changes, list):
        expected_changes = len(changes)
        expected_high_risk = sum(
            1 for change in changes if isinstance(change, dict) and change.get("risk_level") == "high"
        )
        if summary.get("change_count") != expected_changes:
            errors.append(
                f"change_log.summary.change_count is {summary.get('change_count')!r}; "
                f"expected {expected_changes}"
            )
        if summary.get("high_risk_change_count") != expected_high_risk:
            errors.append(
                "change_log.summary.high_risk_change_count is "
                f"{summary.get('high_risk_change_count')!r}; expected {expected_high_risk}"
            )

    if errors:
        checks.append(make_check("consistency-summary-counts", "fail", "; ".join(errors) + "."))
    else:
        checks.append(
            make_check(
                "consistency-summary-counts",
                "pass",
                "Audit and change log summary counts match parsed arrays.",
            )
        )


def validate_finding_change_links(
    artifacts: dict[str, dict[str, Any]], checks: list[CheckResult]
) -> None:
    if "audit_report.json" not in artifacts or "change_log.json" not in artifacts:
        checks.append(
            make_check(
                "consistency-finding-change-links",
                "not_run",
                "Finding/change reference checks were skipped because audit_report.json or change_log.json was not parsed.",
            )
        )
        return

    audit_report = artifacts.get("audit_report.json", {})
    change_log = artifacts.get("change_log.json", {})
    findings = audit_report.get("findings") if isinstance(audit_report, dict) else []
    changes = change_log.get("changes") if isinstance(change_log, dict) else []

    finding_ids = collect_ids(findings, "finding_id")
    change_ids = collect_ids(changes, "change_id")
    errors: list[str] = []
    warnings: list[str] = []

    if isinstance(findings, list):
        for finding in findings:
            if not isinstance(finding, dict):
                continue
            finding_id = finding.get("finding_id", "<unknown finding>")
            for change_id in finding.get("related_change_ids", []):
                if change_id not in change_ids:
                    errors.append(f"finding {finding_id!r} references missing change_id {change_id!r}")

    if isinstance(changes, list):
        for change in changes:
            if not isinstance(change, dict):
                continue
            change_id = change.get("change_id", "<unknown change>")
            related_finding_ids = change.get("related_finding_ids", [])
            if not related_finding_ids and finding_ids:
                warnings.append(f"change {change_id!r} has no related_finding_ids")
            for finding_id in related_finding_ids:
                if finding_id not in finding_ids:
                    errors.append(f"change {change_id!r} references missing finding_id {finding_id!r}")

    if errors:
        checks.append(make_check("consistency-finding-change-links", "fail", "; ".join(errors) + "."))
    elif warnings:
        checks.append(make_check("consistency-finding-change-links", "warn", "; ".join(warnings) + "."))
    else:
        checks.append(
            make_check(
                "consistency-finding-change-links",
                "pass",
                "Finding and change log references are consistent.",
            )
        )


def validate_safety_flags(artifacts: dict[str, dict[str, Any]], checks: list[CheckResult]) -> None:
    needed = ("audit_report.json", "change_log.json", "validation_report.json")
    if any(file_name not in artifacts for file_name in needed):
        checks.append(
            make_check(
                "safety-flags",
                "not_run",
                "Safety flag checks were skipped because one or more safety-bearing JSON artifacts were not parsed.",
            )
        )
        return

    errors: list[str] = []

    audit_report = artifacts.get("audit_report.json", {})
    audit_summary = audit_report.get("audit_summary") if isinstance(audit_report, dict) else None
    if isinstance(audit_summary, dict) and audit_summary.get("human_review_required") is not True:
        errors.append("audit_report.audit_summary.human_review_required must be true")

    findings = audit_report.get("findings") if isinstance(audit_report, dict) else []
    if isinstance(findings, list):
        for finding in findings:
            if isinstance(finding, dict) and finding.get("human_review_required") is not True:
                errors.append(
                    f"audit finding {finding.get('finding_id', '<unknown>')!r} must require human review"
                )

    change_log = artifacts.get("change_log.json", {})
    if isinstance(change_log, dict):
        if change_log.get("human_approval_required") is not True:
            errors.append("change_log.human_approval_required must be true")
        if change_log.get("publishes_gtm_changes") is not False:
            errors.append("change_log.publishes_gtm_changes must be false")

        changes = change_log.get("changes", [])
        if isinstance(changes, list):
            for change in changes:
                if isinstance(change, dict) and change.get("human_approval_required") is not True:
                    errors.append(
                        f"change {change.get('change_id', '<unknown>')!r} must require human approval"
                    )

    validation_report = artifacts.get("validation_report.json", {})
    publish_safety = (
        validation_report.get("publish_safety") if isinstance(validation_report, dict) else None
    )
    if isinstance(publish_safety, dict):
        if publish_safety.get("optimized_container_publish_ready") is not False:
            errors.append("validation_report.publish_safety.optimized_container_publish_ready must be false")
        if publish_safety.get("mlp_publishes_gtm_changes") is not False:
            errors.append("validation_report.publish_safety.mlp_publishes_gtm_changes must be false")
        if publish_safety.get("human_approval_required") is not True:
            errors.append("validation_report.publish_safety.human_approval_required must be true")

    if errors:
        checks.append(make_check("safety-flags", "fail", "; ".join(errors) + "."))
    else:
        checks.append(
            make_check(
                "safety-flags",
                "pass",
                "Package safety flags preserve human approval and no-publish requirements.",
            )
        )


def validate_package(package_dir: Path, schemas_dir: Path) -> tuple[list[CheckResult], str]:
    checks: list[CheckResult] = []

    validate_required_files(package_dir, checks)
    if any(check.check_id == "package-dir" and check.status == "fail" for check in checks):
        return checks, package_dir.name or "unknown-package"

    artifacts = load_package_json(package_dir, checks)
    validate_markdown_files(package_dir, checks)
    validate_schema_backed_artifacts(artifacts, schemas_dir, checks)
    validate_optimized_container(artifacts, checks)
    validate_run_metadata(artifacts, checks)
    run_id = validate_run_id_consistency(artifacts, package_dir, checks)
    validate_client_id_consistency(artifacts, checks)
    validate_summary_counts(artifacts, checks)
    validate_finding_change_links(artifacts, checks)
    validate_safety_flags(artifacts, checks)

    return checks, run_id


def infer_validation_status(checks: list[CheckResult]) -> str:
    if any(check.status == "fail" for check in checks):
        return "fail"
    if any(check.status == "warn" for check in checks):
        return "warn"
    return "pass"


def package_schema_version(schemas_dir: Path) -> str:
    schema, error = load_schema(schemas_dir / "gtm_patch_package.schema.json")
    if error or schema is None:
        return "1.0.0"

    schema_version = (
        schema.get("properties", {})
        .get("schema_version", {})
        .get("default")
    )
    if isinstance(schema_version, str) and schema_version:
        return schema_version
    return "1.0.0"


def build_report(
    checks: list[CheckResult], run_id: str, schemas_dir: Path, checked_at: str
) -> dict[str, Any]:
    errors = sorted(check.message for check in checks if check.status == "fail")
    warnings = sorted(check.message for check in checks if check.status == "warn")

    return {
        "artifact_type": "validation_report",
        "schema_version": VALIDATION_REPORT_SCHEMA_VERSION,
        "run_id": run_id,
        "package_schema_version": package_schema_version(schemas_dir),
        "validation_status": infer_validation_status(checks),
        "checks": [
            {
                "check_id": check.check_id,
                "status": check.status,
                "message": check.message,
                "checked_at": checked_at,
            }
            for check in checks
        ],
        "errors": errors,
        "warnings": warnings,
        "publish_safety": {
            "optimized_container_publish_ready": False,
            "mlp_publishes_gtm_changes": False,
            "human_approval_required": True,
        },
    }


def write_report(report: dict[str, Any], output_path: Path | None) -> None:
    serialized = json.dumps(report, indent=2, sort_keys=True, ensure_ascii=False) + "\n"

    if output_path is None:
        print(serialized, end="")
        return

    if output_path.exists() and output_path.is_dir():
        raise OutputPackageValidationError(f"output path is a directory: {output_path}")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(serialized, encoding="utf-8")


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)

    if not is_date_time(args.checked_at):
        print(f"ERROR: --checked-at must be a valid RFC 3339 date-time: {args.checked_at}", file=sys.stderr)
        return 2

    try:
        checks, run_id = validate_package(args.package_dir, args.schemas_dir)
        report = build_report(checks, run_id, args.schemas_dir, args.checked_at)
        write_report(report, args.output)
    except OutputPackageValidationError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    return 1 if report["validation_status"] == "fail" else 0


if __name__ == "__main__":
    raise SystemExit(main())
