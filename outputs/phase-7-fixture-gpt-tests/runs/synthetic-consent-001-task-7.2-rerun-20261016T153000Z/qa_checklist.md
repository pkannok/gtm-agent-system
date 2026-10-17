# Manual QA Checklist — synthetic-consent-001

**Status:** Draft; no human QA performed. **Approval gate:** Human review required before import, workspace creation, publishing, or production use. This checklist does not establish legal or consent compliance.

## QA-001 — Package completeness
- **Status:** `todo` | **Rule:** GTM-QA-001 | **Finding:** F-003 | **Change:** none | **Entity:** package
- **Scenario:** Review deliverable completeness and configuration preservation.
- **Manual steps:** Confirm all seven named artifacts exist; compare the input and optimized container entity IDs, parameters, triggers and consent fields; inspect validation warnings.
- **Expected:** Seven files; no configuration differences; no changes silently applied.
- **Evidence:** File manifest, JSON comparison, reviewer initials/date. **Reviewer:** GTM analyst.

## QA-002 — Denied/default consent on first pageview
- **Status:** `blocked` pending approved isolated test context and consent policy | **Rule:** GTM-CONSENT-001 | **Findings:** F-001, F-002, F-003 | **Change:** none | **Entities:** tag 106, tag 107, trigger 206
- **Scenario:** Fresh visit with relevant advertising/vendor consent denied or not yet granted.
- **Manual steps:** In an approved non-production review context, establish denied/default consent; open a test page; examine GTM Preview consent state, pageview, tags fired/not fired and network requests. Compare against client/CMP policy and any supported platform-specific consent behavior.
- **Expected:** Behavior matches approved consent requirements; do **not** assume both tags must be absent without confirming the required vendor-specific behavior and permitted cookieless signaling. Any unauthorized request must be investigated.
- **Evidence:** Redacted consent state, Preview event timeline, fired/not-fired tags, network host/path and timestamps. **Reviewer:** GTM analyst and privacy reviewer.

## QA-003 — Granted consent and consent transition
- **Status:** `blocked` pending approved test context and consent policy | **Rule:** GTM-CONSENT-001 | **Findings:** F-001, F-003 | **Change:** none | **Entities:** tag 106, trigger 206, variable 306
- **Scenario:** Fresh page with permission granted, followed by consent change/revocation as supported.
- **Manual steps:** Validate consent initialization order, tag 106's relevant checks, pageview 206, the variable reference `{{CONST - Google Ads Conversion ID}}`, duplicate firing, and network behavior. Test both fresh consent and consent transition.
- **Expected:** Only behavior approved by analyst/privacy requirements, without unintended premature, repeat or post-revocation collection.
- **Evidence:** Redacted Preview event timeline, consent states, tag firing record and network observations. **Reviewer:** GTM analyst and privacy reviewer.

## QA-004 — Custom HTML vendor script review
- **Status:** `blocked` pending code/vendor approval | **Rule:** GTM-CONSENT-001 | **Findings:** F-002, F-003 | **Change:** none | **Entities:** tag 107, trigger 206
- **Scenario:** External JavaScript loaded from `https://vendor.example.test/pixel.js` under denied and granted states.
- **Manual steps:** Obtain and review actual vendor script and documentation; inspect loaded code, additional endpoints, cookies/storage, URL/form/dataLayer/identifier access, network requests and consent dependencies in an approved isolated environment.
- **Expected:** Behavior understood and approved before any use; do not infer safety from the short HTML snippet.
- **Evidence:** Script/code review record, redacted network log, endpoint list, policy signoff. **Reviewer:** Developer/security and privacy reviewer.

## QA-005 — Conversion and ecommerce scope
- **Status:** `todo` | **Rule:** GTM-QA-001 | **Finding:** F-003 | **Change:** none | **Entity:** tag 106
- **Scenario:** Confirm whether remarketing is being mistaken for conversion measurement.
- **Manual steps:** Review intended Google Ads purpose and expected events. The fixture has no ecommerce or conversion-event tags; only test a purchase flow if a separate implementation is supplied and approved.
- **Expected:** No invented conversion or ecommerce QA results; any conversion requirements are tracked as outside this fixture's coverage.
- **Evidence:** Analyst scope decision and test plan, if applicable. **Reviewer:** Measurement analyst.

## QA-006 — Rejection, rollback and approval
- **Status:** `todo` | **Rule:** GTM-QA-001 | **Findings:** F-001, F-002, F-003 | **Change:** none | **Entities:** entire container
- **Scenario:** Reject any unapproved future remediation.
- **Manual steps:** Compare optimized vs original export; preserve original file/hash; decline any manual consent or HTML patch until reviewed. If an analyst later creates an approved patch, record separate change/rollback evidence.
- **Expected:** Baseline is the unchanged source export. No production effect occurs from this package.
- **Evidence:** Diff, reviewer decision, approval/rejection log. **Reviewer:** GTM owner and privacy stakeholder.

**Open approvals:** GTM analyst; privacy/legal reviewer as appropriate; developer/vendor-code reviewer for tag 107. All human tests remain outstanding.
