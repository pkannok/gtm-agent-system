# Task 4.1 - Build `normalize_gtm_export.py`

## Status

Upcoming

## Goal

Build a deterministic script that normalizes GTM container exports for repeatable analysis and diffing.

## How it fits

Normalization reduces noise and makes later validation, comparison, and testing more reliable.

## In scope

- Parse GTM export JSON.
- Preserve GTM semantics.
- Normalize ordering or formatting where safe.
- Produce deterministic output.

## Out of scope

- Modifying live GTM.
- Inferring audit findings.
- Applying cleanup recipes.
- Publishing.

## Definition of done for MLP

- [ ] Script parses valid GTM exports.
- [ ] Script produces deterministic normalized output.
- [ ] Script preserves source data needed for audit and diff workflows.
- [ ] Invalid JSON produces an understandable error.
