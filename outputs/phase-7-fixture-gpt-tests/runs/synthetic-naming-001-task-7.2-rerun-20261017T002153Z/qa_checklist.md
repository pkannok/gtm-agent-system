# Manual QA Checklist — synthetic-naming-001

**All statuses: `todo` — no GTM Preview or live tests were performed.** Human approval is required before import, workspace creation, publishing, or production use.

### QA-001 — Package and safe review context
- **Status:** `todo` | **Related findings:** F-001/F-002 | **Rule:** GTM-NAME-001 | **Changes:** CH-001/CH-002
- **Scenario/manual steps:** Confirm seven artifacts and review in an isolated GTM test context only; do not use production.
- **Expected result:** All files present; approvals pending.
- **Evidence to capture:** File list, analyst signoff
- **Reviewer:** GTM analyst (not assigned).

### QA-002 — Tag 101 (GA4 - Event - lead_submit)
- **Status:** `todo` | **Related findings:** F-001 | **Rule:** GTM-NAME-001 | **Changes:** CH-001
- **Scenario/manual steps:** In GTM Preview on a suitable test page, inspect tag 101 before/after proposed rename; confirm eventName lead_submit, measurementId {{id}}, and firingTriggerId 201 remain unchanged.
- **Expected result:** Renamed tag exhibits same firing behavior as source under equivalent conditions; avoid interpreting event name as proof of form-submit gating.
- **Evidence to capture:** Before/after Preview screenshots and firing logs, redacted
- **Reviewer:** GTM analyst (not assigned).

### QA-003 — Trigger 201 (PV - All Pages)
- **Status:** `todo` | **Related findings:** F-002 | **Rule:** GTM-NAME-001 | **Changes:** CH-002
- **Scenario/manual steps:** Verify PAGEVIEW trigger 201 has no unexpected hidden restrictions; visit a test page and navigate through representative page views in a controlled preview. Inspect events where tag 101 does and does not fire.
- **Expected result:** Scope matches analyst-approved meaning of 'All Pages'; tag 101 fires only where baseline fired.
- **Evidence to capture:** Preview timeline, trigger detail screenshots, non-firing cases
- **Reviewer:** GTM analyst (not assigned).

### QA-004 — Variable 301 (id) / tag 101 token
- **Status:** `todo` | **Related findings:** F-003 | **Rule:** GTM-NAME-001 | **Changes:** none
- **Scenario/manual steps:** Inspect tag parameter measurementId={{id}} and resolve in Preview; compare with export constant G-TEST501. Do not rename variable until all references, including external documentation, are reviewed.
- **Expected result:** Token resolves as intended; no value or reference change is included in optimized JSON.
- **Evidence to capture:** Redacted variables panel and tag parameter screenshots
- **Reviewer:** GTM analyst (not assigned).

### QA-005 — Folder 401 (misc)
- **Status:** `todo` | **Related findings:** F-004 | **Rule:** GTM-NAME-001 | **Changes:** none
- **Scenario/manual steps:** Review tag 101 and variable 301 membership and confirm grouping purpose with GTM analyst.
- **Expected result:** Folder name stays misc until an approved name is selected.
- **Evidence to capture:** Folder membership and reviewer decision
- **Reviewer:** GTM analyst (not assigned).

### QA-006 — Rollback/rejection
- **Status:** `todo` | **Related findings:** F-001/F-002 | **Rule:** GTM-NAME-001 | **Changes:** CH-001/CH-002
- **Scenario/manual steps:** Compare changed entities against source JSON; reject by restoring tag 101 name to tag 1 and trigger 201 name to all. Recheck the same Preview scenarios if subsequently tested.
- **Expected result:** Baseline names restored; IDs, eventName, measurementId and firing conditions unchanged.
- **Evidence to capture:** JSON diff, rollback approval, before/after Preview records
- **Reviewer:** GTM analyst (not assigned).

### QA-007 — Conversion/event semantics
- **Status:** `todo` | **Related findings:** F-001 | **Rule:** GTM-QA-001 | **Changes:** CH-001
- **Scenario/manual steps:** The tag calls event 'lead_submit' but is attached to PAGEVIEW trigger 201. Analyst should confirm whether that event is expected on page views or only after a lead action. Do not alter trigger logic in this package.
- **Expected result:** Client-defined event intent and firing expectation documented; any logic fix separately approved.
- **Evidence to capture:** Approved measurement requirements, Preview event timeline
- **Reviewer:** GTM analyst (not assigned).

### QA-008 — Human approval checkpoint
- **Status:** `todo` | **Related findings:** F-001/F-002/F-003/F-004 | **Rule:** GTM-QA-001 | **Changes:** none
- **Scenario/manual steps:** Have analyst verify draft names, residual risks, external name references and test evidence prior to any import/workspace/publish/production decision.
- **Expected result:** Written approval or rejection; no automated production action.
- **Evidence to capture:** Reviewer, date, signoff record
- **Reviewer:** GTM analyst (not assigned).

## Boundaries
No ecommerce payload, consent configuration, custom code, variable value, tag payload, or trigger condition edits are included. No privacy or consent compliance determination is made from this export. Human Preview, tracking review and approval remain outstanding.
