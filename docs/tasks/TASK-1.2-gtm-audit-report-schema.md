# Task 1.2 - Create `gtm_audit_report.schema.json`

## Status

Complete

## Goal

Define the machine-readable audit report contract for the GTM Container Audit & Patch Package.

## How it fits

The audit report JSON is for future agents, validators, dashboards, and tests. The markdown audit report is for humans.

## In scope

- Create `schemas/gtm_audit_report.schema.json`.
- Create `examples/schema-validation/gtm_audit_report.sample.json`.
- Define container summary, findings, affected entities, evidence, recommended actions, and manual-review fields.
- Validate the sample against the schema.

## Out of scope

- Running audits.
- Creating audit intelligence.
- Validators or test harnesses.
- Live GTM, GA4, or Google Ads API access.

## Definition of done for MLP

- [x] Findings have severity, category, evidence, affected entities, and recommended action.
- [x] Schema distinguishes automated change availability from manual review requirements.
- [x] A sample audit report validates successfully.
