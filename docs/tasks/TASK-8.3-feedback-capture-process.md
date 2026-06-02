# Task 8.3 - Create feedback capture process

## Status

Upcoming

## Goal

Create a structured way for analysts to report misses, false positives, unsafe suggestions, and formatting issues.

## How it fits

The MLP improves through repeated real-world use and feedback converted into rules or tests.

## In scope

- Create a feedback template.
- Include run ID, client ID, input, issue type, expected behavior, actual behavior, severity, and suggested fix.
- Link feedback to fixtures or client runs.

## Out of scope

- Issue tracker integration.
- Public support workflow.
- Automated triage.
- Live GTM access.

## Definition of done for MLP

- [ ] Feedback template exists.
- [ ] Every MLP run has a `run_id`.
- [ ] Feedback can be linked to a specific fixture or client run.
- [ ] Issues can be converted into tests or rules.
