# Task 7.2 Mechanical Validation Evidence

## Scope

On 2026-10-16, `scripts/validate_output_package.py` was run against all six captured GPT-generated packages in `outputs/phase-7-fixture-gpt-tests/runs/`. The historical outputs were not edited. The validator was run with the deterministic timestamp `2026-10-16T00:00:00Z`.

## Results

| Package | Exit | Result | Failed checks |
| --- | ---: | --- | --- |
| `synthetic-naming-001` | 1 | fail | `schema-audit_report.json`, `schema-change_log.json`, `schema-validation_report.json`, `run-metadata`, `safety-flags` |
| `synthetic-reference-001` | 1 | fail | `schema-audit_report.json`, `schema-change_log.json`, `schema-validation_report.json`, `run-metadata`, `consistency-finding-change-links`, `safety-flags` |
| `synthetic-duplicate-001` | 1 | fail | `schema-audit_report.json`, `schema-change_log.json`, `schema-validation_report.json`, `run-metadata`, `consistency-summary-counts`, `safety-flags` |
| `synthetic-unused-001` | 1 | fail | `schema-audit_report.json`, `schema-change_log.json`, `schema-validation_report.json`, `run-metadata`, `consistency-summary-counts`, `safety-flags` |
| `synthetic-ecommerce-001` | 1 | fail | `schema-audit_report.json`, `schema-change_log.json`, `schema-validation_report.json`, `run-metadata`, `consistency-summary-counts`, `safety-flags` |
| `synthetic-consent-001` | 1 | fail | `schema-audit_report.json`, `schema-change_log.json`, `schema-validation_report.json`, `run-metadata`, `safety-flags` |

## Failure matrix by mismatch type

| Package | Missing fields / metadata | Wrong field names / schema drift | Invalid IDs or unresolved links | Inconsistent counts | Missing safety flags |
| --- | --- | --- | --- | --- | --- |
| `synthetic-naming-001` | `created_at`/`timestamp`, `input_files`, `tool_version`/`gpt_version` | Audit, change-log, and validation-report contracts use alternate names/shapes | None reported | None reported | Finding review flags; change-log approval/no-publish flags |
| `synthetic-reference-001` | `tool_version`/`gpt_version` | Audit, change-log, and validation-report contracts use alternate names/shapes | `F-REF-001`..`003` reference missing `CHG-REC-001`..`003` | None reported | Finding review flags; change-log and validation-report safety flags |
| `synthetic-duplicate-001` | `created_at`/`timestamp`, `input_files`, `tool_version`/`gpt_version` | Audit, change-log, and validation-report contracts use alternate names/shapes | None reported | Change-log summary counts do not match `changes` | Finding review flags; change-log safety flags |
| `synthetic-unused-001` | `created_at`/`timestamp`, `input_files`, `tool_version`/`gpt_version` | Audit, change-log, and validation-report contracts use alternate names/shapes | None reported | Change-log summary counts do not match `changes` | Finding review flags; change-log safety flags |
| `synthetic-ecommerce-001` | `input_files`, `tool_version`/`gpt_version` | Audit, change-log, and validation-report contracts use alternate names/shapes | None reported | Change-log summary counts do not match `changes` | Finding review flags; change-log safety flags |
| `synthetic-consent-001` | `created_at`/`timestamp`, `input_files`, `tool_version`/`gpt_version` | Audit, change-log, and validation-report contracts use alternate names/shapes | None reported | None reported | Finding review flags; change-log safety flags |

No separate invalid-ID format violation was reported by the validator. The reference run's ID failure is an unresolved cross-artifact link, not an ID-pattern failure.

Common human-readable failure themes:

- `audit_report.json`, `change_log.json`, and `validation_report.json` use older or alternate field names instead of the current schema contracts.
- `run_metadata.json` is missing one or more required run context fields, especially `input_files`, `created_at`/`timestamp`, or `tool_version`/`gpt_version`.
- Findings and changes are not always linked consistently, or summary counts do not match the arrays.
- Human-review and no-publish safety flags are missing or false where the contract requires them.
- The optimized containers themselves passed the basic GTM export-shape check in these runs.

## Known-bad package

`examples/script-smoke-tests/bad-output-package` failed as expected with exit code 1. The errors were understandable and specific: a change referenced missing finding `finding-missing`, and `optimized_container.json` lacked array-valued `containerVersion.tag`, `containerVersion.trigger`, and `containerVersion.variable` fields.

As a control, `examples/script-smoke-tests/valid-output-package` passed with exit code 0.

## Instruction update

`custom-gpt/instructions.md` now includes a mechanical validation checklist covering exact schema field names, required artifact fields, link and count consistency, full GTM export shape, run metadata, and mandatory draft/no-publish safety flags. This addresses the recurring failures without rewriting historical GPT outputs.

`outputs/_template/README.md` now repeats the per-artifact contract and validator command. `scripts/validate_phase_7_outputs.ps1` discovers every direct child package directory under the Phase 7 runs directory, then adds the known-good and known-bad smoke controls and reports whether each result matches its expected status.

## Status against definition of done

- [x] At least two captured GPT-generated packages pass: the fresh duplicate and naming reruns pass with exit code 0.
- [x] Known-bad package fails: yes.
- [x] Validation errors are understandable to a human analyst: yes; check IDs and messages identify the failing contract area.
- [x] GPT instructions are updated based on recurring validation failures: yes.

Task 7.2 is complete against its definition of done. Older failed run directories remain preserved for regression evidence; the dynamic wrapper still returns exit code 1 when those historical failures are included.

## Final re-run

The repeatable command was run after the repository updates:

```powershell
.\scripts\validate_phase_7_outputs.ps1
```

Result: exit code `1`, because older discovered GPT package directories still fail their expected `pass` status. The fresh packages `synthetic-duplicate-001-task-7.2-rerun-20261016T225022Z` and `synthetic-naming-001-task-7.2-rerun-20261017T002153Z` each returned `pass` with exit code `0`. The known-good smoke fixture returned `pass`; the known-bad smoke fixture returned `fail`, matching its expected failure. The wrapper continues to act as a regression check over all discovered runs.
