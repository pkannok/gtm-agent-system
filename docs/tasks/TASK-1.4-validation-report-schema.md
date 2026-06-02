# Task 1.4 - Create `validation_report.schema.json`

## Status

Complete

## Goal

Define the machine-readable validation report contract for the GTM Container Audit & Patch Package.

## How it fits

Future validators use this artifact to communicate package consistency, warnings, errors, and manual-review requirements.

## In scope

- Create `schemas/validation_report.schema.json`.
- Create `examples/schema-validation/validation_report.sample.json`.
- Define validation status, checks, warnings, errors, and publish-safety fields.
- Validate the sample against the schema.

## Out of scope

- Building validators.
- Running package validation beyond schema/sample validation.
- Live GTM access.
- Claiming production safety.

## Definition of done for MLP

- [x] Validation report has validation status, warnings, errors, and manual-review-related fields.
- [x] Schema can represent a package with a broken reference as failed.
- [x] Schema can represent custom HTML risk warnings or failures.
- [x] Schema can represent missing output file failures.
