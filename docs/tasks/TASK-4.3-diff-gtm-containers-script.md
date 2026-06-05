# Task 4.3 - Build `diff_gtm_containers.py`

## Status

Complete

## Goal

Build a deterministic script that compares a source GTM export and `optimized_container.json`.

## How it fits

The diff script supports change log verification and helps analysts confirm proposed changes are traceable.

## In scope

- Compare source and optimized container exports.
- Identify added, modified, renamed, disabled, or removed entities.
- Produce machine-readable diff data suitable for change log checks.

## Out of scope

- Applying changes to GTM.
- Deciding whether changes are safe.
- Publishing.
- Full report generation.

## Definition of done for MLP

- [x] Script accepts original and optimized JSON paths.
- [x] Script outputs `change_log.json`.
- [x] Every detected modification has entity type, entity ID/name, change type, and before/after summary.
- [x] Each change can include or support a rollback note.
- [x] Deletions are clearly flagged as high-risk/manual-review when detected.
- [x] Script detects entity-level differences.
- [x] Script outputs a deterministic machine-readable diff.
- [x] Diff can support change log validation.
- [x] Deletions are visible and not hidden.
- [x] Script does not imply detected changes are approved for import, workspace creation, publishing, or production use.
