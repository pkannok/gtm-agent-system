# Task 7.1 - Run fixture-based GPT tests

## Status

Manual review complete - needs revision

## Goal

Upload each synthetic fixture to the Custom GPT and capture outputs.

## How it fits

Fixture-based GPT tests verify the end-to-end user experience and package completeness.

## In scope

- Run GPT tests against fixtures.
- Save prompts, outputs, generated files, manual scores, and errors.
- Check each run for required output sections.
- Use `outputs/phase-7-fixture-gpt-tests/` as the manual test-run workspace.

## Out of scope

- Live GTM API access.
- Public release.
- Automated validator implementation.
- Real client data.
- Fake or placeholder GPT run outputs.

## Manual test framework

The Task 7.1 manual test framework is prepared in:

- `outputs/phase-7-fixture-gpt-tests/README.md`
- `outputs/phase-7-fixture-gpt-tests/run-log.md`
- `outputs/phase-7-fixture-gpt-tests/manual-review-worksheet.md`
- `outputs/phase-7-fixture-gpt-tests/prompts/`
- `outputs/phase-7-fixture-gpt-tests/runs/`

Task 7.1 remains incomplete until the human GPT fixture runs, generated artifacts, manual reviews, and run-log results are recorded.

## Definition of done for MLP

- [x] GPT tested against at least six fixtures.
- [x] Each run produces all required output sections.
- [x] At least four of six runs meet manual quality threshold.
- [x] Unsafe recommendations are fixed before release.
