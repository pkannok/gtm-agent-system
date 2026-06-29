# QA Checklist — GTM Container Audit & Patch Package

Source file: `synthetic-broken-references.json`
Fixture ID: `synthetic-reference-001`
Run ID: `run-4009056865b0`

All statuses default to `todo` because no live GTM Preview, website QA, GA4, Google Ads, API, workspace, or production platform was inspected or verified.

Human review is required before import, workspace creation, publishing, or production use.

## QA-001 — Package completeness review

- Status: `todo`
- Related findings: `F-INV-001`
- Related rules: `GTM-INV-001`
- Related changes: `none`
- Affected entity: `container` `5102` — `Synthetic Broken References Container`
- Reviewer role: `GTM analyst`

Manual steps:
- [ ] Confirm all seven required artifacts are present.
- [ ] Open each JSON artifact and confirm it parses.
- [ ] Confirm optimized_container.json is treated as a draft proposal, not as publish-ready output.

Expected result: All seven artifacts are available and reviewed before any import or workspace action.

Evidence to capture: Reviewer notes confirming artifact names and parse status.

## QA-002 — Broken reference review

- Status: `todo`
- Related findings: `F-REF-001, F-REF-002, F-REF-003`
- Related rules: `GTM-REF-001`
- Related changes: `CHG-REC-001, CHG-REC-002, CHG-REC-003`
- Affected entity: `tag` `102` — `GA4 - Event - Purchase`
- Reviewer role: `GTM analyst`

Manual steps:
- [ ] Inspect tag 102 in a safe review context.
- [ ] Confirm whether trigger 202, folder 402, and a revenue variable are the intended targets.
- [ ] Do not import or publish changes until the analyst confirms the target references.

Expected result: The analyst records confirmed target IDs/names or rejects each recommended repair.

Evidence to capture: Screenshots or notes showing source references and confirmed target entities.

## QA-003 — GA4 purchase event and ecommerce value QA

- Status: `todo`
- Related findings: `F-REF-001, F-REF-003, F-ECOM-001`
- Related rules: `GTM-REF-001, GTM-ECOM-001`
- Related changes: `CHG-REC-001, CHG-REC-003`
- Affected entity: `tag` `102` — `GA4 - Event - Purchase`
- Reviewer role: `GTM analyst / developer`

Manual steps:
- [ ] Run a test purchase flow in GTM Preview in a safe QA environment after any analyst-approved repair.
- [ ] Confirm the purchase event occurs.
- [ ] Confirm the GA4 purchase tag fires only on the intended purchase event.
- [ ] Inspect the value, currency, transaction_id, and items values. Do not record raw sensitive user values.

Expected result: Purchase tag firing and ecommerce parameters match client/source documentation and are not duplicated or missing.

Evidence to capture: GTM Preview event log, tag firing status, and redacted parameter values.

## QA-004 — Orphaned entity review

- Status: `todo`
- Related findings: `F-UNUSED-001`
- Related rules: `GTM-UNUSED-001`
- Related changes: `none`
- Affected entity: `multiple` `202/402/302` — `CE - purchase / GA4 - Ecommerce / DLV - ecommerce.transaction_id`
- Reviewer role: `GTM analyst`

Manual steps:
- [ ] Review whether trigger 202, folder 402, and variable 302 are intentionally unused, legacy, or intended reference targets.
- [ ] Do not delete, disable, or archive from export evidence alone.
- [ ] Record final disposition for each entity.

Expected result: Each apparently orphaned entity has an analyst-approved disposition.

Evidence to capture: Reviewer notes identifying keep, repair target, archive candidate, or needs-more-info status.

## QA-005 — Approval and safety boundary review

- Status: `todo`
- Related findings: `none`
- Related rules: `GTM-QA-001`
- Related changes: `none`
- Affected entity: `package` `run-4009056865b0` — `GTM Container Audit & Patch Package`
- Reviewer role: `GTM analyst / client stakeholder`

Manual steps:
- [ ] Confirm the package was not treated as a live GTM change.
- [ ] Confirm human approval is documented before import, workspace creation, publishing, or production use.
- [ ] Confirm validation findings are not treated as proof of tracking correctness or compliance.

Expected result: Approval boundaries are documented before any next action.

Evidence to capture: Reviewer approval notes or rejection notes.
