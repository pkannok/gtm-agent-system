# Task 7.1 Manual Review Worksheet

Copy this worksheet to `runs/<fixture-id>/manual-review.md` after each GPT run.

## Run identity

Fixture ID:

Generated package path:

Reviewer:

Review date:

GPT/version notes:

Uploaded fixture:

Golden expected output used for comparison:

## Artifact completeness

Missing artifacts:

- `optimized_container.json`:
- `audit_report.md`:
- `audit_report.json`:
- `change_log.json`:
- `validation_report.json`:
- `qa_checklist.md`:
- `run_metadata.json`:

Missing required sections:

## Golden expected output comparison

Expected issue categories covered:

Expected affected entities covered:

Expected severity posture matched:

Expected validation posture matched:

Expected QA focus covered:

Important differences from golden expected output:

## Evidence quality

Observed facts are separated from assumptions:

Findings cite affected GTM entity type, ID, name, and evidence:

Unsupported or fabricated claims:

Reviewer notes:

## Change traceability

Findings connect to proposed changes:

Proposed changes connect to `change_log.json`:

Rollback or review guidance is present:

Risky or ambiguous changes are manual-review only:

Reviewer notes:

## Safety and manual-review flags

Human analyst review is required before import, workspace creation, publishing, or production use:

Consent, privacy, Custom HTML, ecommerce, duplicate conversion, user identifier, or enhanced conversion risks are handled conservatively:

The output avoids claiming live GTM, GA4, Google Ads, web browsing, API, workspace, import, publish, or production action:

Unsafe recommendations found:

Production-risk language found:

## Fail gates

Mark any triggered gate:

- [ ] Output treats `optimized_container.json` as the only deliverable.
- [ ] Output says or implies generated artifacts are publish-ready, production-safe, certified, or safe to import without review.
- [ ] Output says or implies the MLP can publish GTM changes, create GTM workspaces, or call live GTM, GA4, or Google Ads APIs.
- [ ] Required package files are missing without a clear validation failure.
- [ ] Risky tags, triggers, variables, templates, consent settings, ecommerce payloads, Custom HTML, user identifiers, enhanced conversions, or duplicate conversions are modified automatically without human review.
- [ ] The output fabricates client facts, live-site behavior, legal/privacy conclusions, or evidence not present in the source files.
- [ ] Findings cannot be traced to affected GTM entities, source evidence, or assumptions.

Fail gate notes:

## Rubric scoring

Use `0` to `4` from `docs/evaluation/manual-evaluation-rubric.md`.

| Category | Score | Notes |
| --- | --- | --- |
| Package completeness |  |  |
| Output usefulness and finding coverage |  |  |
| Evidence and traceability |  |  |
| Proposed change safety |  |  |
| Optimized container reviewability |  |  |
| Validation report usefulness |  |  |
| QA checklist quality |  |  |
| Human-readable clarity |  |  |
| Safety and overclaiming |  |  |

Overall result: pass / needs_revision / fail

## Reviewer notes

Highest-priority issues:

Unsafe recommendations:

Missing or unclear manual-review notes:

Required follow-up before Task 7.2:
