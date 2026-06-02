# Task 4.4 - Build `validate_output_package.py`

## Status

Upcoming

## Goal

Build a deterministic script that validates a full GTM Container Audit & Patch Package.

## How it fits

Package validation ensures required artifacts exist, JSON artifacts parse, schemas are respected, and package safety flags are present.

## In scope

- Check required output artifacts.
- Validate JSON artifacts against schemas.
- Check package references and consistency.
- Produce `validation_report.json`-compatible output.

## Out of scope

- Creating package artifacts.
- Live GTM validation.
- Publishing.
- API connectors.

## Definition of done for MLP

- [ ] Valid package passes.
- [ ] Known-bad package fails.
- [ ] Missing required files fail.
- [ ] Errors are understandable to a human analyst.
