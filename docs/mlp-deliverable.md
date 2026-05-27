# GTM Container Audit & Patch Package

## Summary

The GTM Container Audit & Patch Package is the canonical MLP deliverable for this project.

It is produced from a Google Tag Manager container export JSON and optional client standards. It gives a technical marketing analyst enough information to understand the container, review proposed improvements, inspect the optimized JSON, validate the output, and perform manual QA.

## Primary input

Required:

- A GTM container export JSON file.

Optional:

- Client profile or client standards.
- Agency standards.
- User task intent, such as "audit for duplicate tags" or "prepare cleanup recommendations."

## Required outputs

### 1. `optimized_container.json`

A complete GTM container export JSON containing proposed reviewable optimizations.

This file is not considered publish-ready by default. It must be reviewed by a human analyst.

### 2. `audit_report.md`

A human-readable audit report.

It should explain:

- Container summary.
- High-priority findings.
- Proposed changes.
- Risks and assumptions.
- Manual review items.
- QA recommendations.

### 3. `audit_report.json`

A machine-readable version of the audit findings.

It should be suitable for future agents, validators, dashboards, or tests.

### 4. `change_log.json`

A machine-readable list of changes between the source container and `optimized_container.json`.

Each change should explain:

- What changed.
- Which GTM entity was affected.
- Why the change was proposed.
- Whether the change is low, medium, or high risk.
- How to roll it back conceptually.

### 5. `validation_report.json`

A machine-readable validation summary.

It should report whether required artifacts exist, whether JSON files parse, and whether obvious structural problems were detected.

### 6. `qa_checklist.md`

A human-readable checklist for analyst review and GTM preview/testing.

### 7. `run_metadata.json`

A machine-readable file describing the run.

It should include:

- Run ID.
- Timestamp.
- Input filenames.
- Client ID, if provided.
- Standards applied.
- MLP version.
- Tool or GPT version, if available.

## Required package behavior

The package must:

- Include both human-readable and machine-readable artifacts.
- Preserve traceability from finding to proposed change.
- Distinguish observed facts from assumptions.
- Flag manual review items.
- Avoid implying that changes are safe to publish.
- Treat optimized JSON as one part of the package, not the entire deliverable.

## Out of scope for the MLP

The MLP does not:

- Publish GTM versions.
- Create GTM workspaces.
- Call GTM, GA4, or Google Ads APIs.
- Replace human QA.
- Certify privacy or legal compliance.
- Guarantee that the optimized container is production-safe.
