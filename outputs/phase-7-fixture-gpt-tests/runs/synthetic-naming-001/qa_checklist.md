# QA Checklist — GTM Container Audit & Patch Package

All checklist items default to `todo`. Human review is required before import, workspace creation, publishing, or production use.

## QA-001 — Package completeness

- Related finding ID: `F-INV-001`
- Related rule ID: `GTM-INV-001`
- Related change ID: none
- Affected GTM entity: package
- Scenario to test: Confirm the deliverable package is complete.
- Manual steps:
  1. Confirm all seven required artifacts are present.
  2. Confirm JSON artifacts parse before analyst review.
  3. Confirm `audit_report.md`, `audit_report.json`, `change_log.json`, `validation_report.json`, and this checklist agree on finding and change IDs.
- Expected result: All seven artifacts are present and internally traceable.
- Evidence to capture: File list and parse status.
- Reviewer or role: Technical marketing analyst.
- Status: `todo`

## QA-002 — Tag rename review

- Related finding ID: `F-NAME-001`
- Related rule ID: `GTM-NAME-001`
- Related change ID: `CHG-NAME-001`
- Affected GTM entity: tag `101`, proposed name `GA4 - Event - lead_submit`
- Scenario to test: Confirm the proposed tag name accurately describes the existing tag configuration.
- Manual steps:
  1. Inspect tag `101` in a safe review context.
  2. Confirm tag type `gaawe` and event name `lead_submit`.
  3. Confirm the rename does not change firing triggers, event name, measurement ID, consent settings, or payload fields.
- Expected result: The proposed name is accurate and no behavior-changing edit is introduced.
- Evidence to capture: Screenshot or review note showing tag ID, proposed name, event name, and trigger reference.
- Reviewer or role: Technical marketing analyst.
- Status: `todo`

## QA-003 — Trigger rename review

- Related finding ID: `F-NAME-002`
- Related rule ID: `GTM-NAME-001`
- Related change ID: `CHG-NAME-002`
- Affected GTM entity: trigger `201`, proposed name `PV - All Pages`
- Scenario to test: Confirm the proposed trigger name describes the trigger type and scope.
- Manual steps:
  1. Inspect trigger `201`.
  2. Confirm trigger type is `PAGEVIEW`.
  3. Confirm the rename does not add filters or change trigger logic.
- Expected result: Trigger remains a pageview trigger and the name is reviewable.
- Evidence to capture: Screenshot or review note showing trigger ID, type, and proposed name.
- Reviewer or role: Technical marketing analyst.
- Status: `todo`

## QA-004 — Variable rename and token maintenance review

- Related finding ID: `F-NAME-003`
- Related rule ID: `GTM-NAME-001`
- Related change IDs: `CHG-NAME-003`, `CHG-REF-001`
- Affected GTM entities: variable `301`, tag `101`
- Scenario to test: Confirm the renamed measurement ID constant still resolves in the GA4 event tag.
- Manual steps:
  1. Inspect variable `301` and confirm its value remains `G-TEST501`.
  2. Inspect tag `101` and confirm the measurement ID field references `{{CONST - GA4 Measurement ID}}`.
  3. In GTM Preview or a safe import review context, confirm the resolved measurement ID value remains `G-TEST501`.
  4. Confirm no external dependency requires the old variable name `id`.
- Expected result: Variable value is unchanged and tag `101` still resolves the intended measurement ID.
- Evidence to capture: Review note or screenshot showing variable value and resolved tag measurement ID.
- Reviewer or role: Technical marketing analyst.
- Status: `todo`

## QA-005 — Folder rename review

- Related finding ID: `F-NAME-004`
- Related rule ID: `GTM-NAME-001`
- Related change ID: `CHG-NAME-004`
- Affected GTM entity: folder `401`, proposed name `GA4 - Core Measurement`
- Scenario to test: Confirm the proposed folder name accurately describes grouped entities.
- Manual steps:
  1. Inspect folder `401`.
  2. Confirm it contains the GA4 event tag and GA4 measurement ID constant variable.
  3. Confirm the rename does not imply publish approval or production readiness.
- Expected result: Folder name is clearer and does not imply safety or approval.
- Evidence to capture: Review note showing folder contents and proposed name.
- Reviewer or role: Technical marketing analyst.
- Status: `todo`

## QA-006 — Rollback and rejection review

- Related finding ID: all naming findings
- Related rule ID: `GTM-NAME-001`
- Related change IDs: `CHG-NAME-001`, `CHG-NAME-002`, `CHG-NAME-003`, `CHG-NAME-004`, `CHG-REF-001`
- Affected GTM entity: all proposed changes
- Scenario to test: Confirm each proposed change can be rejected or rolled back.
- Manual steps:
  1. Review `change_log.json`.
  2. Confirm rollback notes are clear for each change.
  3. If rejecting the variable rename, confirm the tag token also returns to `{{id}}`.
- Expected result: Analyst can reject or roll back any proposed change without deleting entities or changing tracking behavior.
- Evidence to capture: Signed review note or issue tracker comment.
- Reviewer or role: Technical marketing analyst.
- Status: `todo`
