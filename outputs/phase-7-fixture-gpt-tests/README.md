# Phase 7 Fixture GPT Tests

## Purpose

This folder is the manual Task 7.1 workspace for testing the internal `GTM Container Analyst` Custom GPT against the six synthetic GTM container fixtures.

The goal is to verify that the GPT can produce a draft **GTM Container Audit & Patch Package** from each fixture, with all seven required artifacts, useful findings, traceable evidence, conservative proposed changes, and safe human-review language.

This is a manual testing framework. It does not replace Task 7.2 validator or structured evaluation work.

## Required package artifacts

Each run should capture the full **GTM Container Audit & Patch Package**:

1. `optimized_container.json`
2. `audit_report.md`
3. `audit_report.json`
4. `change_log.json`
5. `validation_report.json`
6. `qa_checklist.md`
7. `run_metadata.json`

Generated artifacts are draft proposals only. Do not import, publish, create GTM workspaces, call live APIs, or use them in production without separate human analyst review and approval.

## Fixture runs

| Fixture ID                | Fixture file                                                                | Golden expected output                                                           | Prompt file                                 | Run folder                      |
| ------------------------- | --------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | ------------------------------------------- | ------------------------------- |
| `synthetic-naming-001`    | `examples/synthetic-gtm-containers/synthetic-naming-issues.json`            | `examples/golden-expected-outputs/synthetic-naming-001.expected-package.json`    | `prompts/synthetic-naming-001.prompt.md`    | `runs/synthetic-naming-001/`    |
| `synthetic-reference-001` | `examples/synthetic-gtm-containers/synthetic-broken-references.json`        | `examples/golden-expected-outputs/synthetic-reference-001.expected-package.json` | `prompts/synthetic-reference-001.prompt.md` | `runs/synthetic-reference-001/` |
| `synthetic-duplicate-001` | `examples/synthetic-gtm-containers/synthetic-duplicate-purchase-tags.json`  | `examples/golden-expected-outputs/synthetic-duplicate-001.expected-package.json` | `prompts/synthetic-duplicate-001.prompt.md` | `runs/synthetic-duplicate-001/` |
| `synthetic-unused-001`    | `examples/synthetic-gtm-containers/synthetic-unused-legacy-entities.json`   | `examples/golden-expected-outputs/synthetic-unused-001.expected-package.json`    | `prompts/synthetic-unused-001.prompt.md`    | `runs/synthetic-unused-001/`    |
| `synthetic-ecommerce-001` | `examples/synthetic-gtm-containers/synthetic-ecommerce-missing-fields.json` | `examples/golden-expected-outputs/synthetic-ecommerce-001.expected-package.json` | `prompts/synthetic-ecommerce-001.prompt.md` | `runs/synthetic-ecommerce-001/` |
| `synthetic-consent-001`   | `examples/synthetic-gtm-containers/synthetic-consent-risk-remarketing.json` | `examples/golden-expected-outputs/synthetic-consent-001.expected-package.json`   | `prompts/synthetic-consent-001.prompt.md`   | `runs/synthetic-consent-001/`   |

## Manual workflow

1. Open the internal Custom GPT named `GTM Container Analyst`.
2. Confirm the GPT configuration still matches `custom-gpt/configuration.md`.
3. Confirm the approved knowledge files from `custom-gpt/knowledge-files.md` are still uploaded.
4. Confirm file upload and data-analysis capability are available.
5. Confirm no GPT Actions or live API connectors are configured.
6. Confirm no live GTM, GA4, Google Ads, web browsing, publishing, workspace creation, or external platform access is configured.
7. For each fixture, start a new GPT conversation.
8. Upload only the matching synthetic fixture JSON file.
9. Paste the matching prompt from `outputs/phase-7-fixture-gpt-tests/prompts/`.
10. Save the GPT response as `gpt-response.md` in the matching run folder.
11. Save or copy the seven generated artifacts into the matching run folder.
12. Compare the generated artifacts against the matching golden expected output.
13. Complete `manual-review.md` in the run folder, using `manual-review-worksheet.md` as the template.
14. Record the result in `run-log.md`.
15. Flag any unsafe recommendation, production-risk language, missing artifact, or missing manual-review warning.
16. Do not import the generated `optimized_container.json` into GTM.
17. Do not publish, create workspaces, call live APIs, or use real client data.

## Comparing to golden expected outputs

Use the golden expected output as reviewer evidence, not as prompt input.

Compare generated outputs against:

- Expected finding categories and rule IDs.
- Expected severity posture.
- Affected entity IDs, names, and evidence.
- Whether proposed changes are conservative and reviewable.
- Whether validation catches expected structure or reference issues.
- Whether QA checklist items cover the fixture risk type.
- Whether safety language preserves human approval before import, workspace creation, publishing, or production use.

## Manual scoring

Apply `docs/evaluation/manual-evaluation-rubric.md` to each run.

Record:

- Pass/fail gates.
- Category scores.
- Overall result: `pass`, `needs_revision`, or `fail`.
- Unsafe recommendations.
- Production-risk language.
- Follow-up required before Task 7.2.

## Evidence required before Task 7.1 can receive a clean pass

Task 7.1 should not receive a clean pass until:

- All six fixture runs have GPT output captured.
- Each run folder contains `gpt-response.md`.
- Each run folder contains all seven required package artifacts or a documented failure.
- Each run has a completed manual review.
- `run-log.md` records pass, needs-revision, or fail for every fixture.
- Unsafe recommendations are fixed or explicitly recorded as blockers.
- At least four of six runs meet the manual quality threshold.

Task 7.1 status is `Needs revision` due to GTM JSON package-level blocker.
