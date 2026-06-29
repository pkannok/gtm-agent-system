# QA Checklist — GTM Container Audit & Patch Package

Fixture ID: `synthetic-duplicate-001`
Source file: `synthetic-duplicate-purchase-tags.json`
Run ID: `gtm-audit-synthetic-duplicate-001-20260626T000000Z`

This checklist is for human analyst review. No live GTM, GA4, Google Ads, website, API, workspace, or production system was inspected by this package.

## QA-001 — Package completeness and source scope

- Status: `todo`
- Related rules: `GTM-INV-001`, `GTM-QA-001`
- Affected entity: container `5103` / `Synthetic Duplicate Purchase Version`
- Scenario to test: Confirm the analyst received and can open all seven required artifacts.
- Manual steps:
  1. Confirm these files are present: `optimized_container.json`, `audit_report.md`, `audit_report.json`, `change_log.json`, `validation_report.json`, `qa_checklist.md`, and `run_metadata.json`.
  2. Confirm the source fixture is `synthetic-duplicate-001` and the only export input is `synthetic-duplicate-purchase-tags.json`.
  3. Confirm `optimized_container.json` is treated as a draft proposal, not a publish-ready GTM version.
- Expected result: All files are present and the analyst agrees the package is file-in/file-out only.
- Evidence to capture: File list, reviewer initials, review date.
- Reviewer role: technical marketing analyst.

## QA-002 — GTM Preview test for duplicate GA4 purchase firing

- Status: `todo`
- Related findings: `F-DUP-001`, `F-ECOM-001`
- Related rules: `GTM-DUP-001`, `GTM-ECOM-001`, `GTM-QA-001`
- Related change: `CHG-001`
- Affected entities: tag `103` (`GA4 - Event - purchase`), tag `104` (`GA4 - Event - purchase copy`), trigger `203` (`CE - purchase`)
- Scenario to test: Trigger a controlled test purchase event in GTM Preview.
- Manual steps:
  1. Import or inspect only in a safe review context approved by the analyst.
  2. Trigger one test `purchase` event.
  3. In GTM Preview, confirm whether tag `103`, tag `104`, or both fire on the same event.
  4. Record the Preview event name, tag firing list, and trigger details.
- Expected result: Analyst determines whether both tags fire for the same purchase event and whether this is intentional.
- Evidence to capture: GTM Preview screenshots/logs showing the purchase event and fired tags.
- Reviewer role: technical marketing analyst.
- Rollback/rejection note: Because this package did not apply duplicate cleanup, rejecting the recommendation leaves both original tags unchanged.

## QA-003 — Ecommerce deduplication and transaction ID review

- Status: `todo`
- Related findings: `F-DUP-001`, `F-ECOM-001`
- Related rules: `GTM-ECOM-001`, `GTM-QA-001`
- Affected entities: variable `304` (`DLV - ecommerce.transaction_id`), tags `103` and `104`
- Scenario to test: Confirm `transaction_id` is present and consistent for a test purchase.
- Manual steps:
  1. Inspect the dataLayer on the test purchase event.
  2. Confirm `ecommerce.transaction_id` is populated with a non-empty redacted/test value.
  3. Confirm whether both GA4 purchase tags send the same transaction ID.
  4. Confirm downstream deduplication expectations with the analytics owner before disabling or removing either tag.
- Expected result: One purchase should produce the intended transaction ID behavior without duplicate reporting risk.
- Evidence to capture: Redacted transaction ID field name/value presence, Preview variable resolution, analyst notes.
- Reviewer role: analytics owner or technical marketing analyst.

## QA-004 — Human decision on duplicate cleanup

- Status: `todo`
- Related finding: `F-DUP-001`
- Related change: `CHG-001`
- Related rule: `GTM-DUP-001`
- Affected entities: tag `103`, tag `104`
- Scenario to test: Decide whether tag `104` is intentional, legacy, test-only, or an accidental duplicate.
- Manual steps:
  1. Review naming, folder placement, fingerprints, and any client documentation.
  2. Decide which tag, if any, should be paused, removed, or consolidated in a safe GTM workspace.
  3. Record the decision and rationale before making any live or workspace change.
- Expected result: A documented human decision exists before any deletion, disabling, or consolidation action.
- Evidence to capture: Review note or ticket linking selected action to Preview evidence.
- Reviewer role: technical marketing analyst and analytics owner.

## QA-005 — Purchase payload completeness review

- Status: `todo`
- Related finding: `F-ECOM-001`
- Related rule: `GTM-ECOM-001`
- Affected entities: tags `103` and `104`
- Scenario to test: Confirm the purchase event carries all intended ecommerce fields.
- Manual steps:
  1. Review whether `value`, `currency`, and `items` are expected to be set through tag parameters, event data, GA4 settings, or another implementation pattern.
  2. Confirm purchase payload completeness using GTM Preview and approved analytics debugging tools.
  3. Do not add or edit ecommerce payload fields from this package without analyst review.
- Expected result: Analyst confirms whether missing observed parameters are acceptable for this implementation.
- Evidence to capture: DataLayer documentation, Preview variable screenshots/logs, analyst notes.
- Reviewer role: technical marketing analyst or analytics owner.

## QA-006 — Approval boundary checkpoint

- Status: `todo`
- Related rules: `GTM-QA-001`
- Affected entity: full package
- Scenario to test: Confirm no generated artifact is used as production-safe without human approval.
- Manual steps:
  1. Confirm no one treats `optimized_container.json` as a publish-ready guarantee.
  2. Confirm human review is complete before import, workspace creation, publishing, or production use.
  3. If any change is later made in GTM, document workspace/version, reviewer, and rollback plan.
- Expected result: Approval boundaries are documented.
- Evidence to capture: Approval note or ticket.
- Reviewer role: technical marketing analyst, analytics owner, and client stakeholder where applicable.
