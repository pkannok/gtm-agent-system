# Manual QA Checklist — synthetic-ecommerce-001-20261017

**Status:** Draft / not executed. Every item remains `todo` or `blocked`. Human review is required before import, workspace creation, publishing, or production use.

## QA-001 — Package completeness
- **Status:** todo
- **Related finding / rule / change:** F-ECOM-001 / GTM-ECOM-001 / none
- **Affected entity:** Package (all seven artifacts)
- **Scenario:** Independent analyst opens the seven deliverables.
- **Steps:** Confirm exact filenames, JSON readability, source-export completeness, and cross-references.
- **Expected:** Seven artifacts exist; no live action or claimed production readiness.
- **Evidence:** Files manifest and reviewer signoff (analyst).

## QA-002 — Safe Preview setup
- **Status:** blocked — requires reviewer-controlled, non-production GTM Preview and test flow
- **Related finding / rule / change:** F-ECOM-001 / GTM-QA-001 / none
- **Affected entity:** Container GTM-SYN505, tag 105, trigger 205
- **Scenario:** Isolated controlled ecommerce test.
- **Steps:** After analyst approval, use an isolated review context; inspect trigger `CE - purchase` (205) configuration including actual event-name matching; initiate a test purchase without a real charge or personal information; inspect Preview event timeline and tag firing.
- **Expected:** Tag `GA4 - Event - purchase` (105) fires exactly once for the intended `purchase` event and does not fire on unrelated page views/events.
- **Evidence:** Redacted Preview event timeline, trigger details, tag-firing log, reviewer (GTM analyst).

## QA-003 — Purchase parameter integrity
- **Status:** blocked — actual dataLayer schema and test environment unavailable
- **Related finding / rule / change:** F-ECOM-001 / GTM-ECOM-001 / none
- **Affected entity:** Tag 105, variable 306, trigger 205
- **Scenario:** Complete purchase payload in controlled test.
- **Steps:** Have developer inspect redacted `dataLayer` purchase event. Identify actual `transaction_id`, `currency`, `value`, and `items` fields; check currency is a valid code, transaction ID is nonempty and unique per order, item objects are populated and values consistent. Check variable 306 resolves `ecommerce.value`. Review GA4 purchase event mapping after a human-approved implementation; verify resulting test request in permitted debug tools.
- **Expected:** Required ecommerce data reaches the intended measurement flow once, matches test order totals and item list, and does not double-count orders.
- **Evidence:** Redacted dataLayer payload and Preview Variables/Tags snapshots, outbound request parameter names (no sensitive values), test-order reconciliation (developer + analytics analyst).

## QA-004 — Mapping remediation approval
- **Status:** blocked — unverified dataLayer keys and mapping approach
- **Related finding / rule / change:** F-ECOM-001 / GTM-ECOM-001 / none
- **Affected entity:** Tag 105; possible new dataLayer variables are *recommendations only*
- **Scenario:** Proposed transaction ID, currency, and items mappings.
- **Steps:** Confirm dataLayer specification with developer and business owner. Independently review GTM event configuration and any consent implications. Record approved exact keys and accepted test results before making any change outside this package.
- **Expected:** No guessed variable paths, fallback currency, fabricated transaction identifiers, or unapproved tag payload changes.
- **Evidence:** Mapping specification, change review approval, reviewer (analytics analyst/developer).

## QA-005 — Consent and personal-data boundary
- **Status:** todo
- **Related finding / rule / change:** F-ECOM-001 / GTM-ECOM-001 / none
- **Affected entity:** GA4 purchase tag 105
- **Scenario:** Consent behavior and field sensitivity review, if relevant to client policy.
- **Steps:** Review client's consent expectations and test consent-denied/consent-granted states in approved Preview; inspect whether purchase payload includes personal identifiers or unnecessary personal information. Escalate to privacy reviewer if present. No consent configuration changes are proposed.
- **Expected:** Document observed behavior without claiming compliance.
- **Evidence:** Redacted consent-state testing notes and fields inspected, reviewer (analytics/privacy as applicable).

## QA-006 — Rejection / rollback
- **Status:** todo
- **Related finding / rule / change:** F-ECOM-001 / GTM-ECOM-001 / none
- **Affected entity:** Complete container export; tag 105
- **Scenario:** Reject any unapproved ecommerce remediation.
- **Steps:** Verify `change_log.json` contains zero applied changes and `optimized_container.json` equals the input byte-for-byte. If a separate human implementation is rejected, restore the approved baseline from the original export in the review context following normal change control. Do not import this draft as a shortcut.
- **Expected:** Baseline mappings stay unchanged; no claimed improvement until separately tested and approved.
- **Evidence:** File SHA-256 comparison and change-control decision, reviewer (GTM owner/analyst).
