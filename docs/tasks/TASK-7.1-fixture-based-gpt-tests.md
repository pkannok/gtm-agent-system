# Task 7.1 - Run fixture-based GPT tests

## Status

Complete

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

Task 7.1 is complete. The human GPT fixture runs, generated artifacts, manual reviews, run-log results, and post-review GTM export-shape remediation are recorded.

## Post-review remediation

The initial manual review flagged a possible malformed `optimized_container.json` blocker. Follow-up investigation found:

- The Phase 7 generated `optimized_container.json` files are valid JSON and use the expected GTM export wrapper and core arrays.
- The synthetic fixture containers are valid GTM export-shaped JSON; the broken-reference fixture intentionally retains invalid references for reference-integrity coverage.
- The script smoke-test valid output package already had a valid `optimized_container.json`.
- The actual defect was metadata-only `optimized_container.container` stubs in the golden expected outputs, combined with schema and package-validator checks that were too permissive.

Remediation replaced the golden expected stubs with complete GTM export-shaped objects while preserving fixture intent and expected rule coverage. The top-level package schema and `validate_output_package.py` now require `exportFormatVersion`, `containerVersion`, and the core `tag`, `trigger`, and `variable` arrays to prevent recurrence.

## Definition of done for MLP

- [x] GPT tested against at least six fixtures.
- [x] Each run produces all required output sections.
- [x] At least four of six runs meet manual quality threshold.
- [x] Unsafe recommendations are fixed before release.
