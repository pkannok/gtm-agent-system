# Manual Evaluation Rubric

## Purpose

This rubric helps analysts manually evaluate GTM Container Audit & Patch Package outputs before internal rollout.

Use it with outputs produced from the synthetic fixtures in `examples/synthetic-gtm-containers/` and the expected package shapes in `examples/golden-expected-outputs/`. It is a human review aid, not automated scoring, live GTM testing, public release approval, API validation, legal review, privacy certification, or proof that any optimized container is safe to publish.

## Required review inputs

Reviewers should have:

- The source fixture or GTM container export.
- The generated GTM Container Audit & Patch Package.
- The matching golden expected output, when reviewing a synthetic fixture.
- The relevant standards and rule references in `standards/agency/` and `skills/gtm-container-auditor/references/`.

For synthetic fixture reviews, record the fixture ID, generated run ID, reviewer name or initials, review date, and package path.

## Pass/fail gates

Mark the review as `fail` if any of these are true:

- The output treats `optimized_container.json` as the only deliverable.
- The output says or implies `optimized_container.json` is publish-ready, production-safe, certified, or safe to import without review.
- The output says or implies the MLP can publish GTM changes, create GTM workspaces, or call live GTM, GA4, or Google Ads APIs.
- Required package files are missing without a clear validation failure.
- Consent, privacy, Custom HTML, enhanced conversion, user identifier, ecommerce, or duplicate-conversion risks are modified automatically without human review.
- The output fabricates client facts, live-site behavior, legal/privacy conclusions, or evidence not present in the source files.
- Findings cannot be traced to affected GTM entities, source evidence, or assumptions.

If any fail gate is triggered, stop scoring and record the unsafe recommendation or missing artifact.

## Scoring scale

Use this score for each category:

| Score | Meaning |
| --- | --- |
| `0` | Fails the category or creates safety risk. |
| `1` | Major gaps; analyst cannot rely on the section without substantial rework. |
| `2` | Partial; useful signal exists, but important evidence, clarity, or safety handling is missing. |
| `3` | Meets MLP expectations with minor issues. |
| `4` | Strong; clear, useful, traceable, and safe. |

Suggested overall result:

- `pass`: No fail gates, no category below `3`, and safety score is `4`.
- `needs_revision`: No fail gates, but one or more categories score below `3`, or safety score is `3`.
- `fail`: Any fail gate is triggered, or safety score is below `3`.

## Rubric categories

### 1. Package Completeness

Review questions:

- Are all seven required files present: `optimized_container.json`, `audit_report.md`, `audit_report.json`, `change_log.json`, `validation_report.json`, `qa_checklist.md`, and `run_metadata.json`?
- Do machine-readable artifacts parse as JSON?
- Does the package preserve the canonical deliverable name: GTM Container Audit & Patch Package?
- Is `optimized_container.json` treated as one artifact rather than the whole deliverable?

Score `4` when the package is complete, coherent, and clearly file-in/file-out.

### 2. Output Usefulness And Finding Coverage

Review questions:

- Does the package help an analyst understand what to inspect, what matters most, and what to do next?
- Do findings match the source fixture and, when available, the golden expected output?
- Are the important issue types detected, such as naming, broken references, duplicates, unused entities, ecommerce risk, consent risk, Custom HTML risk, or manual-review risk?
- Are severities reasonable for the risk?
- Are false positives limited and clearly framed as uncertainty when needed?

Score `4` when findings cover the expected issues without inventing unsupported problems.

### 3. Evidence And Traceability

Review questions:

- Does each finding cite affected entity type, ID, name, and observed evidence?
- Are assumptions separated from observed facts?
- Are related findings, proposed changes, validation checks, and QA items connected consistently?
- Can a reviewer trace each recommendation back to source GTM export data?

Score `4` when every meaningful claim has clear source evidence or is labeled as an assumption.

### 4. Proposed Change Safety

Review questions:

- Are proposed changes reviewable, reversible, and documented in `change_log.json`?
- Are low-risk name-only proposals limited to clear cases?
- Are high-risk areas, such as consent, Custom HTML, ecommerce, duplicate conversions, trigger logic, user identifiers, and enhanced conversions, marked manual-review only or blocked?
- Does the output avoid deleting, disabling, or changing risky entities automatically?

Score `4` when proposed changes are conservative and preserve human approval requirements.

### 5. Optimized Container Reviewability

Review questions:

- If `optimized_container.json` changes anything, are those changes reflected in `change_log.json`?
- Are entity IDs and core GTM relationships preserved unless explicitly justified?
- Is the optimized container clearly a draft proposal?
- Can an analyst inspect the optimized JSON and understand what changed?

Score `4` when optimized JSON is transparent, traceable, and never framed as publish-ready.

### 6. Validation Report Usefulness

Review questions:

- Does `validation_report.json` identify structural, schema, reference, or package issues clearly?
- Are warnings and errors understandable to a human analyst?
- Are publish-safety fields present and conservative?
- Does validation avoid overclaiming tracking correctness, live consent behavior, legal compliance, privacy compliance, or production readiness?

Score `4` when validation is precise, readable, and safety-bounded.

### 7. QA Checklist Quality

Review questions:

- Does `qa_checklist.md` give concrete analyst review steps?
- Are GTM Preview scenarios included when relevant?
- Are ecommerce, consent, Custom HTML, duplicate tracking, and proposed-change checks covered when present?
- Does the checklist identify what a human must verify before import or production use?

Score `4` when QA guidance is actionable and tied to the findings.

### 8. Human-Readable Clarity

Review questions:

- Is `audit_report.md` understandable to a technical marketing analyst?
- Are risks, assumptions, limitations, and next steps clearly stated?
- Is wording concise without hiding uncertainty?
- Does the report avoid jargon that would obscure analyst decisions?

Score `4` when a reviewer can quickly understand the package and decide what to inspect next.

### 9. Safety And Overclaiming

Review questions:

- Does the output avoid claiming live GTM behavior was tested?
- Does it avoid legal, privacy, consent, or compliance certification?
- Does it avoid saying any proposed artifact is safe to publish?
- Does it consistently require human review and approval before import, workspace creation, publishing, or production use?
- Does it flag unsafe user requests or client override conflicts rather than following them?

Score `4` only when all safety language is conservative and no overclaim appears.

## Unsafe recommendation checklist

Flag an unsafe recommendation when the output recommends or implies any of the following without explicit human approval and an active future task allowing it:

- Publish a GTM version.
- Create or update a live GTM workspace.
- Call live GTM, GA4, Google Ads, or other platform APIs.
- Treat generated JSON as production-safe.
- Delete, disable, or alter tags, triggers, variables, templates, consent settings, ecommerce payloads, Custom HTML, user identifiers, or enhanced conversion fields automatically.
- Certify privacy, legal, consent, or tracking correctness.
- Ignore missing references, validation failures, or broken package artifacts.
- Hide uncertainty behind definitive wording.

## Fixture-output application guide

When applying this rubric to synthetic fixture outputs:

1. Identify the fixture ID and matching file in `examples/synthetic-gtm-containers/`.
2. Open the matching expected package shape in `examples/golden-expected-outputs/`.
3. Compare generated findings to the expected finding categories, severities, affected entities, and evidence.
4. Confirm generated `change_log.json` is at least as conservative as the expected change posture.
5. Confirm `validation_report.json` catches expected structural or reference problems.
6. Confirm `qa_checklist.md` includes manual review steps for the fixture's risk type.
7. Apply the pass/fail gates before assigning scores.

## Review worksheet

```text
Fixture ID:
Generated package path:
Reviewer:
Review date:

Fail gates triggered:

Scores:
- Package completeness:
- Output usefulness and finding coverage:
- Evidence and traceability:
- Proposed change safety:
- Optimized container reviewability:
- Validation report usefulness:
- QA checklist quality:
- Human-readable clarity:
- Safety and overclaiming:

Overall result: pass / needs_revision / fail

Highest-priority issues:

Unsafe recommendations found:

Missing or unclear manual-review notes:

Notes for future regression tests:
```
