# Task 1.3 - Create `gtm_change_log.schema.json`

## Status

Complete

## Goal

Define how proposed changes to the GTM container are recorded.

## How it fits

The change log bridges the source container and `optimized_container.json` so humans and future agents can review exactly what changed and why.

## In scope

- Create `schemas/gtm_change_log.schema.json`.
- Create `examples/schema-validation/gtm_change_log.sample.json`.
- Define change IDs, change type, GTM entity fields, reasons, finding links, risk levels, rollback notes, and human approval fields.
- Validate the sample against the schema.

## Out of scope

- Applying changes to live GTM.
- Publishing GTM changes.
- Diff script implementation.
- Automated deletion policies.

## Definition of done for MLP

- [x] Every modification can have a corresponding change log entry.
- [x] Change entries can point back to finding IDs.
- [x] Each change has rollback notes.
- [x] Deletions can be clearly represented as high-risk/manual-review when used.
