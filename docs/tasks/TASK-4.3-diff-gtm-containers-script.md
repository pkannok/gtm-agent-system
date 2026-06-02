# Task 4.3 - Build `diff_gtm_containers.py`

## Status

Upcoming

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

- [ ] Script detects entity-level differences.
- [ ] Script outputs a deterministic machine-readable diff.
- [ ] Diff can support change log validation.
- [ ] Deletions are visible and not hidden.
