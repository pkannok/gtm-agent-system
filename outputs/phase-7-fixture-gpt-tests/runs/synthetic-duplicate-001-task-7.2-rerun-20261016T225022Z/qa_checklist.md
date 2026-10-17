# QA Checklist — synthetic-duplicate-001

**Status:** All checks pending human analyst review. No live QA was performed. The optimized JSON is unchanged from the source.

| QA ID | Related finding(s) | Rule(s) | Change ID | Affected entities | Status | Owner |
|---|---|---|---|---|---|---|
| QA-001 | F-001, F-002 | GTM-QA-001 | None | Package | todo | GTM analyst |
| QA-002 | F-001 | GTM-DUP-001 | None | Tags 103/104; trigger 203 | todo | GTM analyst |
| QA-003 | F-002 | GTM-ECOM-001 | None | Tags 103/104; variable 304 | todo | Analytics/developer |
| QA-004 | F-001, F-002 | GTM-DUP-001, GTM-ECOM-001 | None | Tags 103/104 | todo | GTM analyst |
| QA-005 | F-001 | GTM-DUP-001 | None | Proposed future remediation | todo | Approving analyst |

## QA-001 — Package completeness
- **Scenario:** Confirm all seven contract artifacts are present.
- **Steps:** Inspect filenames, open JSON files, compare run IDs and finding references, confirm source and optimized export hash equality.
- **Expected:** All seven files present, valid JSON syntax, consistent findings F-001/F-002, zero file-based GTM changes.
- **Capture:** File inventory, parse results, hashes, reviewer sign-off.

## QA-002 — Duplicate firing on a single purchase
- **Scenario:** Safe GTM Preview against an approved test checkout, with consent state noted.
- **Steps:** Confirm custom event trigger 203 (`CE - purchase`) matches the intended `purchase` dataLayer event; perform **one** test purchase with a redacted transaction ID. In Preview inspect tag 103 (`GA4 - Event - purchase`) and tag 104 (`GA4 - Event - purchase copy`), firing reasons, exceptions, sequencing, and outgoing GA4 requests.
- **Expected baseline to investigate:** Both tags are configured on trigger 203. **Desired behavior after an approved remediation:** one intended purchase hit to the correct GA4 destination per transaction; no second redundant hit. Neither condition is asserted as verified.
- **Capture:** Preview event timeline, each tag's fired/not-fired state, trigger conditions, redacted network/debug logs, consent state, reviewer and test timestamp.

## QA-003 — Ecommerce payload and deduplication
- **Scenario:** Test purchase with value, currency, item list, and unique transaction ID.
- **Steps:** Inspect `ecommerce.transaction_id` through variable 304; verify value/currency/items are available and correctly sent or explicitly document why absent; compare GTM Preview, GA4 DebugView (human-operated), and a test order record. Repeat page load or confirmation-page revisit in approved test environment.
- **Expected:** Only intended transaction and revenue representation, correct value and currency, required items data, stable unique transaction ID, no repeat hit or duplicate item/revenue data. Missing fields must be investigated, not assumed.
- **Capture:** Redacted dataLayer values, event parameter names, DebugView screenshot, order-to-event reconciliation.

## QA-004 — Consent and configuration review
- **Scenario:** Verify client-required analytics consent states where applicable; this fixture contains no explicit consent settings on the tags.
- **Steps:** Analyst reviews consent policy/configuration and tests pre/post-consent Preview behavior if required. Do not infer compliance or functional consent from absent export fields.
- **Expected:** Behavior matches documented client and legal/privacy decisions, not an automated claim.
- **Capture:** Consent state, tag firing traces, reviewer outcome.

## QA-005 — Rejection, rollback and approval
- **Scenario:** Evaluate a separately approved remediation for F-001, if created later.
- **Steps:** Preserve source export and compare against any future candidate patch. Rejection means retain/revert to both original tag objects 103 and 104, trigger 203 and their original parameters; retest baseline; require named analyst/stakeholder approval. This package itself includes **no** removal, disabling, or configuration change.
- **Expected:** No change without explicit approval and evidence; restoration reestablishes original export configuration if a future patch is rejected.
- **Capture:** Diff, preserved original hash, approval/rejection decision, rollback test evidence.

**Human review is required before import, workspace creation, publishing, or production use.**
