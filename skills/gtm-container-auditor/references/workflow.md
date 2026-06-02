# Skill Workflow Reference

## Purpose

This reference defines the end-to-end workflow for using the `gtm-container-auditor` Skill to produce a **GTM Container Audit & Patch Package** from a GTM container export JSON.

The workflow is file-in/file-out. It does not call GTM, GA4, Google Ads, or other live APIs. All generated GTM artifacts are draft proposals that require human review before import, workspace creation, publishing, or production use.

## Contents

- Workflow inputs
- Execution workflow
- Output assembly rules
- Validation and QA boundaries
- Stopping conditions

## Workflow Inputs

Required input:

- GTM container export JSON.

Optional inputs:

- Client profile.
- Client standards or client override notes.
- Agency standards.
- User task intent, such as audit, cleanup, naming review, ecommerce review, consent/risk review, or QA preparation.

Do not proceed as if a live GTM account is available. If the user provides a URL, account ID, or workspace name without a container export file, ask for the export or explain that live API access is out of scope for the MLP.

## Execution Workflow

1. Confirm the input is a GTM container export JSON.
2. Identify the source filename and create or preserve a run ID.
3. Load the deliverable contract from `references/deliverable-contract.md`.
4. Load the audit rule catalog from `references/audit-rules.md`.
5. Load output writing rules from `references/output-standards.md`.
6. Load agency standards and optional client profile or overrides when available.
7. Parse container metadata and summarize account ID, container ID, container name, export format version, and entity counts.
8. Build a working inventory of tags, triggers, variables, folders, templates, zones, and other exported sections when present.
9. Map references between entities using `references/gtm-object-model.md`.
10. Apply audit rules to produce findings with evidence.
11. Separate detected facts, inferred issues, recommendations, assumptions, and manual-verification items.
12. Identify proposed file-based changes only when the evidence and standards allow them.
13. Keep risky changes manual-review only by default.
14. Create `optimized_container.json` as a proposed artifact when changes are included.
15. Create `change_log.json` with proposed change IDs, affected entities, risk levels, rollback notes, related findings, and approval requirements.
16. Create `audit_report.json` with machine-readable findings and manual-review items.
17. Create `audit_report.md` using the fixed report structure.
18. Create `validation_report.json` with structural checks, warnings, errors, and publish-safety fields.
19. Create `qa_checklist.md` with manual GTM Preview and analyst review steps.
20. Create `run_metadata.json` with run ID, input filename, standards applied, and version notes.
21. Return the full GTM Container Audit & Patch Package.

## Output Assembly Rules

The package is incomplete unless all seven artifacts are represented:

1. `optimized_container.json`
2. `audit_report.md`
3. `audit_report.json`
4. `change_log.json`
5. `validation_report.json`
6. `qa_checklist.md`
7. `run_metadata.json`

`optimized_container.json` is one artifact in the package. It is a proposed GTM container export JSON, not the whole deliverable and not a publish-ready guarantee.

Every finding should connect to:

- A rule ID when a rule applies.
- Evidence from the exported file.
- A severity.
- A recommendation.
- A manual-review flag when needed.
- A related change ID if a proposed change is included.

Every proposed change should connect to:

- The affected GTM entity.
- The finding or reason behind the change.
- Risk level.
- Rollback notes.
- Human approval requirement.
- Whether the change is reflected in `optimized_container.json`.

## Validation and QA Boundaries

Validation may check package completeness, JSON parseability, schema alignment when schemas are available, and obvious structural problems in the exported GTM-like JSON.

Validation does not prove tracking correctness, live consent behavior, legal compliance, privacy compliance, production readiness, or publish safety.

QA guidance must remain human-readable and actionable. Use `qa_checklist.md` for GTM Preview scenarios, consent-sensitive checks, ecommerce checks, rollback checks, and manual analyst review steps.

## Stopping Conditions

Stop and ask for user guidance when:

- The input is not a GTM container export JSON.
- Required source data is missing or malformed enough that audit confidence is low.
- A client override conflicts with a safety rule or required package artifact.
- A requested action would require live GTM, GA4, Google Ads, or other API access.
- A requested action would publish, deploy, create a workspace, or make production changes.
- A recommendation would weaken human review requirements.
- The user asks to treat `optimized_container.json` as the only output.
