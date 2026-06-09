# GTM Agent System

This repository defines a portable Custom GPT + Skill system for technical marketing analytics workflows.

## Project status

Phase 0 status: complete.

Phase 1 status: complete.

Phase 1 schema contracts are defined in `schemas/`, with matching sample files in `examples/schema-validation/` that validate against each schema.

Phase 2 status: complete.

Phase 2 standards are defined in `standards/agency/` and `skills/gtm-container-auditor/references/`.

Phase 3 status: complete.

Phase 3 Skill package files are defined in `skills/gtm-container-auditor/`, including the Skill entrypoint, UI metadata, references, mirrored schema contracts, and initial recipe files.

Phase 4 status: complete.

Task 4.1 status: complete. `scripts/normalize_gtm_export.py` produces deterministic GTM container export summary JSON for audit and diff workflows.

Task 4.2 status: complete. `scripts/validate_gtm_container.py` validates JSON parsing, expected GTM sections, and detectable tag trigger, folder, and variable references.

Task 4.3 status: complete. `scripts/diff_gtm_containers.py` compares original and optimized GTM exports and outputs a machine-readable proposed change log.

Task 4.4 status: complete. `scripts/validate_output_package.py` validates full GTM Container Audit & Patch Package directories for required artifacts, schema-backed JSON artifacts, consistency, safety flags, and validation-report-compatible output.

Phase 5 status: in progress.

Task 5.1 status: complete. `examples/synthetic-gtm-containers/` contains six small synthetic GTM container export fixtures with documented expected issues and no real client data.

Task 5.2 status: complete. `examples/golden-expected-outputs/` contains schema-aligned expected package shapes for the synthetic fixtures.

Next recommended task: Task 5.3 - Create manual evaluation rubric.

The next task brief is `docs/tasks/TASK-5.3-manual-evaluation-rubric.md`.

Task 0.3 status: complete. Project terminology is defined in `docs/glossary.md`.

Task 0.2 status: complete. The portable project repository structure is established.

Task 0.1 status: complete. The canonical MLP deliverable is defined in ADR-0001.

## Canonical MLP deliverable

The first MLP deliverable is:

**GTM Container Audit & Patch Package**

It is produced from a Google Tag Manager container export JSON and optional client standards.

## Required MLP output files

A complete package includes:

1. `optimized_container.json`
2. `audit_report.md`
3. `audit_report.json`
4. `change_log.json`
5. `validation_report.json`
6. `qa_checklist.md`
7. `run_metadata.json`

## Key product decision

The MLP will not produce optimized GTM JSON as the only deliverable.

The optimized JSON must be accompanied by audit findings, change log, validation report, QA checklist, and run metadata.

## Current schema contracts

- `schemas/gtm_patch_package.schema.json` with `examples/schema-validation/gtm_patch_package.sample.json`
- `schemas/gtm_audit_report.schema.json` with `examples/schema-validation/gtm_audit_report.sample.json`
- `schemas/gtm_change_log.schema.json` with `examples/schema-validation/gtm_change_log.sample.json`
- `schemas/validation_report.schema.json` with `examples/schema-validation/validation_report.sample.json`
- `schemas/client_profile.schema.json` with `examples/schema-validation/client_profile.sample.json`

## Current standards and references

- `standards/agency/naming-conventions.md`
- `standards/agency/consent-standard.md`
- `standards/agency/qa-standard.md`
- `skills/gtm-container-auditor/references/workflow.md`
- `skills/gtm-container-auditor/references/deliverable-contract.md`
- `skills/gtm-container-auditor/references/audit-rules.md`
- `skills/gtm-container-auditor/references/gtm-object-model.md`
- `skills/gtm-container-auditor/references/client-overrides.md`
- `skills/gtm-container-auditor/references/output-standards.md`

## Current Skill package

- `skills/gtm-container-auditor/SKILL.md`
- `skills/gtm-container-auditor/agents/openai.yaml`
- `skills/gtm-container-auditor/references/`
- `skills/gtm-container-auditor/schemas/`
- `skills/gtm-container-auditor/recipes/ga4-basic-cleanup.yaml`
- `skills/gtm-container-auditor/recipes/google-ads-conversion-basic.yaml`

The Skill is portable and file-in/file-out. It does not publish GTM changes, call live APIs, or replace analyst QA.

## Current deterministic scripts

- `scripts/normalize_gtm_export.py` - Reads a GTM container export JSON file and writes a deterministic normalized summary JSON with metadata, counts, lookup maps, preserved entities, warnings, and safety flags.
- `scripts/validate_gtm_container.py` - Validates JSON parsing, expected GTM sections, and detectable tag trigger, folder, and variable references.
- `scripts/diff_gtm_containers.py` - Compares original and optimized GTM exports and writes a deterministic proposed change log.
- `scripts/validate_output_package.py` - Validates a GTM Container Audit & Patch Package directory and writes a `validation_report.json`-compatible report.

The script layer is local and file-in/file-out. It does not call live APIs, publish GTM changes, or replace analyst QA.

## Current script smoke-test inputs

- `examples/script-smoke-tests/valid-basic-container.json` - Valid GTM container smoke-test input.
- `examples/script-smoke-tests/broken-reference-container.json` - Failure fixture for missing trigger, folder, and variable references.
- `examples/script-smoke-tests/missing-sections-container.json` - Failure fixture for missing expected GTM sections.
- `examples/script-smoke-tests/invalid-json-container.json` - Failure fixture for JSON parsing errors.
- `examples/script-smoke-tests/valid-basic-container-renamed.json` - Optimized smoke-test input for deterministic diff checks.
- `examples/script-smoke-tests/valid-output-package/` - Passing GTM Container Audit & Patch Package smoke-test fixture.
- `examples/script-smoke-tests/bad-output-package/` - Failure fixture for broken finding-to-change references.
- `examples/script-smoke-tests/missing-files-output-package/` - Failure fixture for missing required package artifacts.

## Current synthetic GTM fixtures

- `examples/synthetic-gtm-containers/synthetic-naming-issues.json` - Fixture for naming-standard findings.
- `examples/synthetic-gtm-containers/synthetic-broken-references.json` - Fixture for missing trigger, folder, and variable references.
- `examples/synthetic-gtm-containers/synthetic-duplicate-purchase-tags.json` - Fixture for duplicate GA4 purchase tracking findings.
- `examples/synthetic-gtm-containers/synthetic-unused-legacy-entities.json` - Fixture for unused or orphaned legacy-entity findings.
- `examples/synthetic-gtm-containers/synthetic-ecommerce-missing-fields.json` - Fixture for ecommerce purchase-field review findings.
- `examples/synthetic-gtm-containers/synthetic-consent-risk-remarketing.json` - Fixture for consent-sensitive remarketing and Custom HTML findings.

## Current golden expected outputs

- `examples/golden-expected-outputs/` - Schema-aligned expected GTM Container Audit & Patch Package shapes for the six synthetic fixtures.

## Repository structure

- `docs/` - Product decisions, MLP deliverable documentation, architecture notes, glossary, and roadmap.
- `docs/tasks/` - Detailed task scope and acceptance criteria.
- `schemas/` - Phase 1 JSON Schema contracts for the GTM Container Audit & Patch Package.
- `examples/schema-validation/` - Minimal sample files that validate against the Phase 1 schemas.
- `examples/script-smoke-tests/` - Minimal smoke-test inputs for deterministic scripts.
- `examples/synthetic-gtm-containers/` - Controlled synthetic GTM container fixtures with documented expected issues.
- `examples/golden-expected-outputs/` - Expected output package shapes for future fixture-based regression tests.
- `standards/agency/` - Agency standards for naming, consent/privacy review, and QA.
- `scripts/` - Deterministic local scripts for Phase 4 container and package checks.
- `custom-gpt/` - Custom GPT draft instructions, description, conversation starters, and test prompts.
- `skills/gtm-container-auditor/` - Reusable Skill package with entrypoint, UI metadata, references, mirrored schemas, and initial recipes.
- `outputs/_template/` - Expected output folder shape for the GTM Container Audit & Patch Package.

Some future-phase files may remain scaffolds until their corresponding implementation tasks are started.
