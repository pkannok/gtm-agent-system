# Human QA Checklist — synthetic-naming-001

**Status:** Draft; all manual QA is pending. This checklist does not certify tracking, consent, privacy, or production readiness.

### QA-000 — Package completeness
- **Status:** `todo`
- **Finding / rule / change:** none / `GTM-QA-001` / none
- **Affected entity:** Package
- **Scenario:** Confirm all seven canonical files and inspect validation warnings.
- **Steps:** Check file manifest, compare report finding IDs to change IDs and source GTM IDs, and review `validation_report.json`.
- **Expected:** All seven files exist, parse where JSON, and have consistent links.
- **Evidence:** Analyst-signed manifest and review notes.
- **Reviewer:** GTM analyst.

### QA-SETUP — Isolated GTM Preview setup
- **Status:** `blocked` (requires a human-controlled safe review environment and appropriate access)
- **Finding / rule / change:** `F-001`, `F-002` / `GTM-QA-001` / `C-001`, `C-002`
- **Affected entity:** Container `GTM-SYN501`
- **Scenario:** Compare source and proposed export without changing a live workspace.
- **Steps:** Following required approval, prepare an isolated review context using an analyst-approved process; compare a representative page view and a lead submission flow. Observe the source behavior first, then test the proposed display-name edits. Test both expected firing and non-firing cases and record applicable consent state. Do not infer live tracking correctness from the fixture.
- **Expected:** Display names differ only as proposed; firing and payload behavior remain unchanged. Whether firing is *appropriate* requires separate business validation.
- **Evidence:** Redacted Preview screenshots, relevant events and tag IDs, consent state, reviewer notes.
- **Reviewer:** GTM analyst.

### QA-001 — tag 101
- **Status:** `todo`
- **Finding / rule / change:** `F-001` / `GTM-NAME-001` / `C-001`
- **Scenario:** Review naming proposal and preserve existing behavior for tag `101`.
- **Steps:**
  1. Compare tag ID 101 configuration before and after patch.
  2. In an isolated GTM review environment, preview a page view; inspect whether tag 101 fires and inspect eventName=lead_submit and the measurementId variable reference.
  3. Confirm no downstream tooling relies on old display name tag 1.
- **Expected:** Tag 101 configuration and firing remain identical to source except display name.
- **Evidence:** Source and draft object comparison, reviewer decision, screenshots or redacted GTM Preview event/tag records as relevant.
- **Reviewer:** GTM analyst.

### QA-002 — trigger 201
- **Status:** `todo`
- **Finding / rule / change:** `F-002` / `GTM-NAME-001` / `C-002`
- **Scenario:** Review naming proposal and preserve existing behavior for trigger `201`.
- **Steps:**
  1. Compare trigger ID 201 type PAGEVIEW and absence of filters before and after patch.
  2. Preview a representative page and confirm trigger 201 evaluation and tag 101 firing are unchanged.
  3. Check pages where the event should not be sent; any inappropriate lead_submit firing is an existing behavior risk, not a proposed logic fix.
- **Expected:** Trigger 201 and related tag firing are equivalent to source; display name alone changes.
- **Evidence:** Source and draft object comparison, reviewer decision, screenshots or redacted GTM Preview event/tag records as relevant.
- **Reviewer:** GTM analyst.

### QA-003 — variable 301
- **Status:** `todo`
- **Finding / rule / change:** `F-003` / `GTM-NAME-001` / `none (withheld)`
- **Scenario:** Review naming proposal and preserve existing behavior for variable `301`.
- **Steps:**
  1. Do not rename in the supplied draft.
  2. Inspect tag 101 measurementId={{id}}; confirm variable ID 301 resolves to the intended test measurement ID under human review.
  3. If a rename is later approved, review every textual {{id}} reference, update coherently under a separate controlled patch, and retest.
- **Expected:** Original variable name id and {{id}} reference remain intact until coordinated human-approved edit.
- **Evidence:** Source and draft object comparison, reviewer decision, screenshots or redacted GTM Preview event/tag records as relevant.
- **Reviewer:** GTM analyst.

### QA-004 — folder 401
- **Status:** `todo`
- **Finding / rule / change:** `F-004` / `GTM-NAME-001` / `none (withheld)`
- **Scenario:** Review naming proposal and preserve existing behavior for folder `401`.
- **Steps:**
  1. Review membership: tag 101 and variable 301 have parentFolderId 401.
  2. Ask the GTM owner whether this grouping is intentionally dedicated to GA4 measurement.
  3. Approve or reject proposed folder name without changing folder ID or membership.
- **Expected:** Folder name misc and membership remain intact unless analyst authorizes a later edit.
- **Evidence:** Source and draft object comparison, reviewer decision, screenshots or redacted GTM Preview event/tag records as relevant.
- **Reviewer:** GTM analyst.

### QA-ROLLBACK — Reject or roll back name-only changes
- **Status:** `todo`
- **Finding / rule / change:** `F-001`, `F-002` / `GTM-NAME-001` / `C-001`, `C-002`
- **Affected entity:** Tag `101`, trigger `201`
- **Scenario:** Verify reversibility before any approved import.
- **Steps:** Reject the proposed export or restore tag 101 name `tag 1` and trigger 201 name `all`; retain source IDs, references, and all configuration. Refer to exact `change_log.json` rollback notes.
- **Expected:** Source naming restored, with unchanged baseline firing logic, event name and variable binding.
- **Evidence:** JSON comparison and reviewer approval/rejection record.
- **Reviewer:** GTM analyst / change approver.

### QA-APPROVAL — Human sign-off
- **Status:** `todo`
- **Finding / rule / change:** `F-001`–`F-004` / `GTM-NAME-001` / `C-001`, `C-002`
- **Affected entity:** All proposed and withheld naming edits
- **Scenario:** Determine if any proposal can proceed to separately authorized review/import activity.
- **Steps:** Approve/reject each candidate; investigate possible external name-based dependencies, confirm folder intent, verify trigger scope, and document any consent considerations for the analytic tag under the applicable client policy.
- **Expected:** Approval decisions recorded before import, workspace creation, publishing, or production use.
- **Evidence:** Analyst sign-off, approved change list, QA notes; no raw personal data.
- **Reviewer:** GTM analyst, relevant stakeholder.

No ecommerce, advertising, Custom HTML, or sensitive-data implementation is evidenced by this small fixture. This is not proof that such behavior is absent from the live site.
