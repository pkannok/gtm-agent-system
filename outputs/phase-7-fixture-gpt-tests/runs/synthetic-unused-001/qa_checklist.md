# QA Checklist

Package: GTM Container Audit & Patch Package
Run ID: `run_synthetic-unused-001_20260626T215120Z`
Fixture ID: `synthetic-unused-001`
Source file: `synthetic-unused-legacy-entities.json`

All QA statuses default to `todo`. This checklist is for human analyst review and GTM Preview/testing. It is not proof of tracking correctness, consent behavior, legal compliance, privacy compliance, production readiness, or publish safety.

## QA-001 — Package completeness

Related finding: `F-001`
Related rule: `GTM-QA-001`
Affected entity: package `run_synthetic-unused-001_20260626T215120Z`
Status: `todo`

Scenario to test: confirm the package includes all seven required artifacts.

Manual steps:

1. Confirm `optimized_container.json` exists.
2. Confirm `audit_report.md` exists.
3. Confirm `audit_report.json` exists.
4. Confirm `change_log.json` exists.
5. Confirm `validation_report.json` exists.
6. Confirm `qa_checklist.md` exists.
7. Confirm `run_metadata.json` exists.

Expected result: all seven artifacts are present and readable.

Evidence to capture: package file listing and reviewer name/date.

Reviewer role: GTM analyst.

## QA-002 — Review orphaned legacy trigger candidate

Related finding: `F-002`
Related rule: `GTM-UNUSED-001`
Related change: none applied
Affected entity: trigger `204`, `legacy - do not delete`
Status: `todo`

Scenario to test: determine whether trigger `204` is intentionally retained.

Manual steps:

1. Review the source export and confirm trigger `204` has no tag references.
2. Check whether the trigger is referenced in external documentation, QA notes, planned tags, or another GTM workspace.
3. Confirm whether the `legacy - do not delete` warning was intentionally added.
4. Decide to retain, rename, archive, or remove only in a separate reviewed workflow.

Expected result: analyst records a retention or cleanup decision with supporting evidence.

Evidence to capture: review notes, any related documentation references, and analyst approval.

Reviewer role: GTM analyst.

## QA-003 — Review unused data layer variable candidate

Related finding: `F-003`
Related rule: `GTM-UNUSED-001`
Related change: none applied
Affected entity: variable `306`, `DLV - legacy_unused_value`
Status: `todo`

Scenario to test: determine whether dataLayer key `legacy_unused_value` is still part of the site dataLayer contract.

Manual steps:

1. Confirm variable `306` has no visible exported references.
2. Review developer dataLayer documentation for `legacy_unused_value`.
3. Check whether any planned or unpublished tags rely on this key.
4. Decide to retain or remove only after analyst/developer approval.

Expected result: analyst records whether the dataLayer key remains required.

Evidence to capture: dataLayer documentation excerpt or reviewer note; do not capture raw sensitive user values.

Reviewer role: GTM analyst or developer.

## QA-004 — Review empty archive folder candidate

Related finding: `F-004`
Related rule: `GTM-UNUSED-001`
Related change: none applied
Affected entity: folder `404`, `Archive - Legacy Review`
Status: `todo`

Scenario to test: determine whether folder `404` is an intentional review placeholder.

Manual steps:

1. Confirm no exported entities use `parentFolderId: 404`.
2. Review whether the folder is used by analyst process or client convention.
3. Decide whether to retain the folder or remove it in a separate reviewed cleanup.

Expected result: analyst records a folder retention or cleanup decision.

Evidence to capture: review notes and any client/team convention references.

Reviewer role: GTM analyst.

## QA-005 — Preview active GA4 sign_up behavior in safe review context

Related finding: `F-005`
Related rule: `GTM-REF-001`
Related change: none applied
Affected entities: tag `105`, trigger `205`, variable `305`, folder `405`
Status: `todo`

Scenario to test: verify the active GA4 `sign_up` event configuration in GTM Preview before trusting or using the package.

Manual steps:

1. Use a safe review context only; do not publish from this package.
2. Trigger the `sign_up` custom event in GTM Preview.
3. Confirm tag `105` (`GA4 - Event - sign_up`) fires on trigger `205` (`CE - sign_up`).
4. Confirm variable `305` (`CONST - GA4 Measurement ID`) resolves to the expected measurement ID for the review environment.
5. Confirm no orphaned trigger or variable cleanup has been applied.

Expected result: preview evidence shows whether the active sign_up tag behaves as expected.

Evidence to capture: GTM Preview event name, tag firing status, variable value screenshot or redacted note, reviewer name/date.

Reviewer role: GTM analyst.

## QA-006 — Approval and rollback boundary

Related finding: `F-006`
Related rule: `GTM-QA-001`
Related change: none applied
Affected entity: package `run_synthetic-unused-001_20260626T215120Z`
Status: `todo`

Scenario to test: confirm human approval and rejection path before import, workspace creation, publishing, or production use.

Manual steps:

1. Confirm no changes were applied in `optimized_container.json`.
2. Review `change_log.json` and confirm recommendations are not applied.
3. Record whether the package is accepted for further analyst review, rejected, or needs revision.
4. Do not import, create a workspace, publish, or use in production without explicit human approval.

Expected result: approval status and next step are recorded.

Evidence to capture: reviewer note, approval/rejection decision, and date.

Reviewer role: GTM analyst or client stakeholder.
