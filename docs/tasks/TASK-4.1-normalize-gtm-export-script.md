# Task 4.1 - Build `normalize_gtm_export.py`

## Status

Complete

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

- [x] Script accepts input path and output path.
- [x] Script parses valid GTM exports.
- [x] Script produces deterministic normalized output.
- [x] Script outputs counts and lookup maps.
- [x] Script preserves source data needed for audit and diff workflows.
- [x] Script works on at least one minimal smoke-test GTM export.
- [x] Invalid JSON produces an understandable error.
- [x] Script does not claim the container is publish-ready.
