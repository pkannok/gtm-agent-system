# Task 10.1 - Add Responses API structured-output runner

## Status

Future

## Goal

Create a code-based runner that uses the same repository assets and returns schema-valid GTM Container Audit & Patch Package artifacts through an API workflow.

## How it fits

This future task turns the file-in/file-out prototype into a repeatable application workflow while preserving the repository-defined output contracts.

## In scope

- Build an API runner that accepts a GTM export and client profile.
- Use Phase 1 schemas as structured output contracts.
- Save all input and output files by `run_id`.
- Support testing without the ChatGPT UI.

## Out of scope

- Changing the canonical deliverable name.
- Replacing the repository as the system of record.
- Live GTM, GA4, or Google Ads API writes.
- Publishing GTM changes.

## Definition of done for future phase

- [ ] API runner accepts GTM export and client profile inputs.
- [ ] API runner returns schema-valid artifacts.
- [ ] Runner saves all input and output files by `run_id`.
- [ ] Runner can be tested without the ChatGPT UI.
