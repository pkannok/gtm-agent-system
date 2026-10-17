# Manual QA checklist — synthetic-reference-001

**Draft / not executed.** All steps require human analyst action. Do not import or publish the retained broken-reference export on the assumption that it is fixed.

## QA-001 — Package and source integrity
- **Status:** `todo` | **Finding:** none | **Rule:** `GTM-INV-001` | **Change:** none | **Entity:** container GTM-SYN502
- **Scenario:** Inspect the seven deliverables.
- **Manual steps:** Confirm all seven filenames; compare optimized JSON with source; review validation warnings and confirm no application changes.
- **Expected:** Complete package, original export configuration preserved, three findings visible and unresolved.
- **Evidence:** File manifest, diff, analyst signoff.
- **Reviewer:** GTM analyst.

## QA-002 — Missing trigger and folder targets
- **Status:** `blocked` | **Findings:** F-REF-001, F-REF-002 | **Rule:** `GTM-REF-001` | **Change:** none | **Entity:** tag 102, `GA4 - Event - Purchase`
- **Scenario:** Confirm references `firingTriggerId=299` and `parentFolderId=499`.
- **Manual steps:** In an approved, isolated review context, inspect intended purchase event conditions and folder convention. Compare potential trigger `202 — CE - purchase` and folder `402 — GA4 - Ecommerce` with implementation documentation. Do not presume either is correct. Review any separately approved fix before safe test import.
- **Expected:** Analyst identifies confirmed targets or keeps repairs blocked; no unapproved trigger/folder change.
- **Evidence:** Approved mappings and screenshots or configuration diffs, without sensitive user data.
- **Reviewer:** GTM analyst / ecommerce owner. **Blocker:** approval and contextual evidence missing.

## QA-003 — Purchase tag firing and revenue mapping
- **Status:** `blocked` | **Findings:** F-REF-001, F-REF-003 | **Rule:** `GTM-REF-001` | **Change:** none | **Entity:** tag 102
- **Scenario:** Test a controlled `purchase` event after a separately reviewed repair in a non-production test context.
- **Manual steps:** Verify event and trigger conditions; inspect `GA4 - Event - Purchase` firing exactly at the intended event and not on unrelated page views. Inspect `value` parameter and `{{Missing Revenue}}` replacement candidate, plus transaction ID, currency, and items if the implementation supports them. Test both expected firing and expected non-firing states.
- **Expected:** Exactly the approved purchase-event firing behavior with a verified numeric value mapping; no missing-variable token.
- **Evidence:** Redacted Preview event log, tag firing screenshots, variable values, dataLayer field names.
- **Reviewer:** GTM analyst / developer. **Blocker:** unresolved references and absent dataLayer specification.

## QA-004 — Ecommerce duplication and downstream review
- **Status:** `blocked` | **Finding:** F-REF-003 | **Rule:** `GTM-REF-001` (also consult `GTM-ECOM-001`) | **Change:** none | **Entity:** tag 102 / variable 302
- **Scenario:** Confirm a single test purchase does not lead to duplicate conversion/revenue measurement.
- **Manual steps:** Verify transaction ID mapping in `DLV - ecommerce.transaction_id`; separately verify purchase value, currency, and items, and compare against redacted test order data. In approved test tooling, inspect whether any other tag or implementation duplicates the event.
- **Expected:** No duplicate purchases; coherent currency, value, transaction ID, and item data.
- **Evidence:** Redacted test order ID, event parameters, Preview logs and reviewer notes.
- **Reviewer:** Ecommerce developer and analytics analyst. **Blocker:** test environment and verified ecommerce specification unavailable.

## QA-005 — Rejection, rollback and human approvals
- **Status:** `todo` | **Findings:** F-REF-001, F-REF-002, F-REF-003 | **Rule:** `GTM-QA-001` | **Change:** none | **Entity:** tag 102
- **Scenario:** Decide whether to accept or reject future manually proposed repairs.
- **Manual steps:** Confirm `change_log.json` contains no applied changes. Reject any proposed repair by retaining the original source file; for an independently approved later patch, restore original `firingTriggerId=299`, `parentFolderId=499`, and `value={{Missing Revenue}}` in a review copy if rejection is required. Never treat this baseline as correct or production-safe. Obtain explicit analyst approval for new decisions.
- **Expected:** No change imported without approval; rejected proposal leaves source baseline untouched.
- **Evidence:** Diff, review decision, approver identity, rollback plan.
- **Reviewer:** GTM analyst and measurement owner.

Consent/legal/privacy verification was not performed and is not certified by this checklist.
