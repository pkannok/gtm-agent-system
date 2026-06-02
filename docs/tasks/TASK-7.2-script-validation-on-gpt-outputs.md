# Task 7.2 - Run script validation on GPT outputs

## Status

Upcoming

## Goal

Run deterministic validators against GPT-generated output packages.

## How it fits

Script validation catches formatting and reference errors that manual review may miss.

## In scope

- Validate at least two full GPT-generated packages.
- Confirm known-bad packages fail.
- Record validation errors.
- Update GPT instructions for recurring validation failures.

## Out of scope

- Building validators unless already complete.
- Live GTM access.
- Publishing.
- Public rollout.

## Definition of done for MLP

- [ ] `validate_output_package.py` passes on at least two full GPT-generated packages.
- [ ] Known-bad packages fail.
- [ ] Validation errors are understandable to a human analyst.
- [ ] GPT instructions are updated based on recurring validation failures.
