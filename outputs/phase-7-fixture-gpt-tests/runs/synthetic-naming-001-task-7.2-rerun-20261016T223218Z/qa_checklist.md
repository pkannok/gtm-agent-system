# Human QA Checklist — synthetic-naming-001

**Status:** All checks `todo`; none executed. Draft proposal only. Human review is required before import, workspace creation, publishing, or production use.

## Preview environment and boundaries
Use an authorized isolated GTM review environment and test page/lead flow only after independent approval. No preview has been run. Verify baseline and draft behavior side by side; confirm tag 101 firing on trigger 201 and whether `lead_submit` on a PAGEVIEW trigger matches requirements. No consent-specific or ecommerce scenario is evidenced by this fixture; do not claim consent or ecommerce checks have passed.

## QA-001 — Review exact proposed name and external documentation dependencies
- Status: `todo`
- Related finding: `F-001`; rule: `GTM-NAME-001`; change: `C-001`
- Entity: Tag 101
- Manual steps: Compare tag 101 before/after; look for references to literal tag name in QA instructions and reports.
- Expected result: Only tag name differs; all GTM IDs and configuration unchanged.
- Evidence to capture: Reviewed JSON diff and analyst signoff
- Reviewer: GTM analyst

## QA-002 — Confirm pageview scope before naming All Pages
- Status: `todo`
- Related finding: `F-002`; rule: `GTM-NAME-001`; change: `none`
- Entity: Trigger 201
- Manual steps: In an approved isolated review context, inspect trigger 201 conditions and GTM Preview on intended test pages.
- Expected result: Observed firing scope agrees with documented intended scope; otherwise reject name.
- Evidence to capture: Preview screenshots showing event and trigger ID
- Reviewer: GTM analyst

## QA-003 — Verify measurementId reference integrity
- Status: `todo`
- Related finding: `F-003`; rule: `GTM-NAME-001`; change: `none`
- Entity: Variable 301 + tag 101
- Manual steps: Compare {{id}} text token in source and draft; if future rename authorized, find and update all reference occurrences then test.
- Expected result: Draft retains variable id and token {{id}}, resolving to same constant in review.
- Evidence to capture: Diff and redacted Preview variable inspection
- Reviewer: GTM analyst

## QA-004 — Confirm grouping purpose
- Status: `todo`
- Related finding: `F-004`; rule: `GTM-NAME-001`; change: `none`
- Entity: Folder 401
- Manual steps: Inspect members tag 101 and variable 301; ask analyst if folder should represent GA4 event measurement.
- Expected result: No folder rename until purpose is confirmed.
- Evidence to capture: Entity membership list and approval
- Reviewer: GTM analyst

## QA-005 — Lead conversion firing behavior
- Status: `todo`
- Related finding: `F-001`; rule: `GTM-QA-001`; change: `C-001`
- Entity: Tag 101 / trigger 201
- Manual steps: In isolated review, preview a normal page and an intended lead submission. Check firing and not-firing expectations with business owner; inspect lead_submit eventName.
- Expected result: Behavior unchanged between source and draft; any pageview-based lead_submit firing inconsistency is escalated, not silently repaired.
- Evidence to capture: Preview event timeline, tag fired/not fired log, redacted parameters
- Reviewer: GTM analyst

## QA-006 — Rollback and rejection
- Status: `todo`
- Related finding: `F-001`; rule: `GTM-QA-001`; change: `C-001`
- Entity: Whole export
- Manual steps: Compare optimized and source; reject C-001 by restoring tag 101 name tag 1; retain source file.
- Expected result: Baseline export exactly restored after name rollback.
- Evidence to capture: JSON diff and analyst approval
- Reviewer: GTM analyst

## QA-007 — Artifact and approvals review
- Status: `todo`
- Related finding: `none`; rule: `GTM-QA-001`; change: `none`
- Entity: Package
- Manual steps: Confirm seven named files, inspect validation warnings and acquire analyst approval before any import or workspace work.
- Expected result: All files accessible; no live actions without explicit future approval.
- Evidence to capture: Package inventory and review decision
- Reviewer: GTM analyst

## Approval boundary
No GTM import, workspace creation, publish, deployment, live API, legal certification, or consent certification was performed.
