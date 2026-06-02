# Task 4.2 - Build `validate_gtm_container.py`

## Status

Upcoming

## Goal

Build a deterministic script that validates basic GTM container export structure and references.

## How it fits

The validator catches structural issues that model reasoning should not be trusted to catch alone.

## In scope

- Validate JSON parsing.
- Check expected GTM top-level sections.
- Check tag trigger references where detectable.
- Check variable references where detectable.
- Report understandable validation results.

## Out of scope

- Live GTM API validation.
- Legal or privacy certification.
- Full package validation.
- Publishing.

## Definition of done for MLP

- [ ] Script validates valid fixture containers.
- [ ] Script reports broken references.
- [ ] Script reports missing expected GTM sections.
- [ ] Errors are understandable to a human analyst.
