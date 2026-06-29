# QA Checklist — GTM Container Audit & Patch Package

All statuses default to `todo` because no live GTM Preview, GA4 DebugView, Google Ads, website, API, workspace, or production platform was inspected or changed.

## QA-PKG-001 — Package completeness

- Related finding ID: `F-002`
- Related rule ID: `GTM-QA-001`
- Related change ID: none
- Affected GTM entity: package-level
- Scenario to test: confirm the package contains all seven required artifacts.
- Manual steps:
  1. Confirm `optimized_container.json` is present.
  2. Confirm `audit_report.md` is present.
  3. Confirm `audit_report.json` is present.
  4. Confirm `change_log.json` is present.
  5. Confirm `validation_report.json` is present.
  6. Confirm `qa_checklist.md` is present.
  7. Confirm `run_metadata.json` is present.
- Expected result: all seven artifacts are available and align on finding IDs, change IDs, and safety wording.
- Evidence to capture: package file list and any validation notes.
- Reviewer or role: technical marketing analyst.
- Status: `todo`

## QA-ECOM-001 — Purchase event dataLayer verification

- Related finding ID: `F-001`
- Related rule ID: `GTM-ECOM-001`
- Related change IDs: `CHG-001`, `CHG-002`, `CHG-003`
- Affected GTM entity: tag `105`, `GA4 - Event - purchase`; trigger `205`, `CE - purchase`; variable `306`, `DLV - ecommerce.value`.
- Scenario to test: complete a purchase test in a safe GTM Preview context.
- Manual steps:
  1. Import or inspect only in a safe review context after approval.
  2. Open GTM Preview for the relevant non-production or approved test environment.
  3. Complete a controlled purchase flow.
  4. Select the `purchase` event in Preview.
  5. Inspect the dataLayer payload for `ecommerce.value`, `ecommerce.transaction_id`, `transaction_id`, `ecommerce.currency`, `currency`, and item-array fields.
  6. Confirm tag `105` firing status on trigger `205`.
- Expected result: the analyst can determine whether transaction ID and currency are available and what exact keys should be mapped.
- Evidence to capture: Preview event log, tag firing result, redacted dataLayer payload, and screenshots. Do not capture raw sensitive user values.
- Reviewer or role: technical marketing analyst and dataLayer/developer owner.
- Status: `todo`

## QA-ECOM-002 — Proposed transaction ID and currency mapping review

- Related finding ID: `F-001`
- Related rule ID: `GTM-ECOM-001`
- Related change IDs: `CHG-001`, `CHG-002`, `CHG-003`
- Affected GTM entity: tag `105`, `GA4 - Event - purchase`.
- Scenario to test: review whether proposed transaction ID and currency mappings should be added.
- Manual steps:
  1. Confirm the approved transaction ID key and currency key from implementation documentation or developer evidence.
  2. Confirm the currency value format, such as ISO 4217 code.
  3. Confirm the transaction ID is stable, unique per purchase, and not a sensitive user identifier.
  4. Confirm adding mappings would not duplicate existing server-side, GA4, or ecommerce tracking.
  5. If approved, test the mappings in a safe preview context before production use.
- Expected result: a human analyst approves, rejects, or revises the proposed mappings with documented evidence.
- Evidence to capture: dataLayer contract reference, Preview screenshots, GA4 DebugView/test output when available, and reviewer notes.
- Reviewer or role: technical marketing analyst, analytics owner, and developer/dataLayer owner.
- Status: `todo`

## QA-ROLLBACK-001 — Reject or roll back proposed ecommerce recommendations

- Related finding ID: `F-001`
- Related rule ID: `GTM-QA-001`
- Related change IDs: `CHG-001`, `CHG-002`, `CHG-003`
- Affected GTM entity: tag `105`, `GA4 - Event - purchase`; proposed variables only.
- Scenario to test: confirm the analyst can reject the proposed recommendations without changing the source behavior.
- Manual steps:
  1. Review `change_log.json`.
  2. Confirm no recommended ecommerce payload changes are reflected in `optimized_container.json`.
  3. If the recommendations are rejected, preserve tag `105` and variable `306` as-is.
  4. Document why the recommendation was rejected or deferred.
- Expected result: rejected recommendations leave source behavior unchanged.
- Evidence to capture: analyst decision note and file comparison if needed.
- Reviewer or role: technical marketing analyst.
- Status: `todo`

## Approval checkpoint

Human approval is required before import, workspace creation, publishing, or production use. This checklist is manual guidance only and does not prove tracking correctness, consent behavior, legal compliance, privacy compliance, production readiness, or publish safety.
