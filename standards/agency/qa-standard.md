# QA Standard

## Purpose

This agency standard defines how `qa_checklist.md` should guide human QA for the GTM Container Audit & Patch Package.

The QA checklist is a human-readable artifact for analyst review and GTM Preview/testing. It is not a Python validator, golden test, live QA runner, legal review, privacy review, or proof that generated GTM JSON is safe to publish.

## Core Safety Rules

- Every package requires human review before import, workspace creation, publishing, or production use.
- QA checklist items should be concrete enough for an analyst to perform manually.
- The MLP must not claim that QA has passed unless a human or later approved tool supplies that evidence.
- The MLP must not claim legal compliance, privacy compliance, consent certification, or production readiness.
- Risky changes remain manual-review by default.

## QA Item Format

Each checklist item should include:

- QA item ID.
- Related finding ID, if available.
- Related rule ID, if available.
- Related change ID, if available.
- Affected GTM entity.
- Scenario to test.
- Manual steps.
- Expected result.
- Evidence to capture.
- Reviewer or role when known.
- Status, such as `todo`, `blocked`, `done`, or `not_applicable`.

## Required QA Categories

### Package completeness

Check that the seven required artifacts are present:

- `optimized_container.json`
- `audit_report.md`
- `audit_report.json`
- `change_log.json`
- `validation_report.json`
- `qa_checklist.md`
- `run_metadata.json`

### GTM Preview setup

Checklist items should tell the analyst what to preview, such as:

- Container or workspace to import into a safe review context.
- Test page or conversion flow.
- Tags expected to fire.
- Tags expected not to fire.
- Consent state to use when applicable.

### Tag firing behavior

For each proposed tag, trigger, or variable change, include:

- Page or event to test.
- Expected firing behavior.
- Trigger condition to confirm.
- Variables or parameters to inspect.
- Screenshots or preview logs to capture.

### Ecommerce behavior

For ecommerce findings or changes, include:

- Test event, such as `view_item`, `add_to_cart`, `begin_checkout`, or `purchase`.
- Required parameters, such as transaction ID, value, currency, and items.
- Expected GA4 or advertising conversion behavior.
- Manual verification that revenue and item data are not duplicated or missing.

### Consent-sensitive behavior

For advertising, remarketing, Custom HTML, enhanced conversion, user identifier, or sensitive data findings, include:

- Consent state to test.
- Vendor tag expected behavior before consent.
- Vendor tag expected behavior after consent.
- Any user identifier or sensitive data fields to inspect.
- Legal or privacy reviewer note when appropriate.

### Custom HTML and custom JavaScript

For Custom HTML or custom JavaScript findings, include:

- Code review requirement.
- External domains or endpoints to inspect.
- User data reads or writes to verify.
- Network behavior to inspect in browser tools when appropriate.
- Manual approval requirement before use.

### Rollback and rejection

For proposed changes included in `optimized_container.json`, include:

- Rollback note from `change_log.json`.
- How to reject the proposed change.
- What behavior should return to baseline.
- Who should approve the rollback or rejection.

## Evidence Requirements

QA evidence should be specific and reviewable:

- GTM Preview event names.
- Tag names and IDs.
- Trigger names and IDs.
- Variable values observed.
- DataLayer event and parameter names.
- Screenshots or logs when available.
- Consent state used during the test.
- Reviewer name or role when known.

Do not include raw sensitive user values in QA evidence. Describe field names or redacted values instead.

## Status Language

Use these checklist statuses:

- `todo`: Human QA has not been performed.
- `blocked`: QA cannot proceed without missing input, environment access, or human decision.
- `done`: QA was completed by a human or approved later tool and evidence is recorded.
- `not_applicable`: The item does not apply and the reason is recorded.

The MLP should default generated QA checklist items to `todo` unless evidence says otherwise.

## Output Alignment

`qa_checklist.md` should align with:

- `audit_report.md` for human-readable risk context.
- `audit_report.json` for finding IDs and rule IDs.
- `change_log.json` for proposed change IDs and rollback notes.
- `validation_report.json` for structural warnings and failures.

If QA guidance conflicts with another artifact, flag the conflict for manual review.
