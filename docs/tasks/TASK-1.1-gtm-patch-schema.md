# Task 1.1 - Create `gtm_patch_package.schema.json`

## Status

Complete

## Phase

Phase 1 - Output contracts and schemas

## Goal

Define the top-level JSON Schema for the full **GTM Container Audit & Patch Package** deliverable.

## Background

Phase 1 defines artifact contracts before building intelligence, validators, scripts, or agent workflows.

The Task 1.1 schema becomes the standard handoff format for future agents and API-based workflows. For example, a HAR analyzer could later add evidence into the same package format.

The schema must describe the whole package, not only `optimized_container.json`.

## In scope

- Create `gtm_patch_package.schema.json`.
- Define the top-level package object for the GTM Container Audit & Patch Package.
- Use JSON Schema-compatible patterns suitable for future structured outputs.
- Require package-level metadata such as artifact type, schema version, run ID, and human approval status.
- Represent all required MLP package artifacts from `docs/mlp-deliverable.md`.
- Include a minimal sample package only as needed to show the schema can validate a package.

## Recommended top-level fields

The schema should support this package shape:

```json
{
  "artifact_type": "gtm_patch_package",
  "schema_version": "1.0.0",
  "run_id": "",
  "client_id": "",
  "source_container_summary": {},
  "standards_applied": [],
  "audit_report": {},
  "change_log": [],
  "validation_report": {},
  "risk_summary": {},
  "qa_checklist": [],
  "human_approval_required": true
}
```

## Required MLP artifact coverage

The schema must account for the required GTM Container Audit & Patch Package outputs:

- `optimized_container.json`
- `audit_report.md`
- `audit_report.json`
- `change_log.json`
- `validation_report.json`
- `qa_checklist.md`
- `run_metadata.json`

## Safety requirements

- The schema must not imply that `optimized_container.json` is publish-ready.
- The schema must not imply that the MLP publishes GTM changes.
- The schema must preserve human approval as a required package-level concept.
- Generated GTM artifacts remain draft proposals for human analyst review.

## Structured output guidance

Use JSON Schema-compatible patterns because later API-based versions should be able to use structured outputs. OpenAI Structured Outputs are intended to make model responses adhere to a supplied JSON Schema rather than merely producing valid JSON.

## Expected files changed

```text
docs/tasks/TASK-1.1-gtm-patch-schema.md
docs/tasks/CURRENT.md
gtm_patch_package.schema.json
gtm_patch_package.sample.json
```

If validation requires a sample package, add the smallest sample package needed for Task 1.1. Do not create a fixture catalog.

## Out of scope

- Validators.
- Python scripts.
- Test harnesses.
- Fixture catalog.
- Recipe catalog.
- API connectors.
- GitHub Actions.
- Full Custom GPT setup.
- Full Skill implementation.
- Live GTM, GA4, or Google Ads API access.
- Publishing GTM changes.

## Definition of done for MLP

- [x] Schema includes all required package solutions.
- [x] Schema has `schema_version`.
- [x] Schema validates a sample package.
- [x] Human approval field is required and defaults conceptually to `true`.
