# qa_checklist.md

# GTM Container Audit & Patch Package QA Checklist

Fixture ID: `synthetic-consent-001`
Run ID: `gtm-audit-synthetic-consent-001-20260626T220218Z`
Source file: `synthetic-consent-risk-remarketing.json`
Status: Draft proposal for human review.

Human review is required before import, workspace creation, publishing, or production use. This checklist has not been executed by this file-in/file-out run.

## QA-001 — Package completeness

- Related finding ID: `F-001`
- Related rule ID: `GTM-QA-001`
- Affected GTM entity: package artifacts
- Scenario to test: Confirm the package contains all seven canonical artifacts.
- Manual steps:
  1. Confirm `optimized_container.json` is present.
  2. Confirm `audit_report.md` is present.
  3. Confirm `audit_report.json` is present.
  4. Confirm `change_log.json` is present.
  5. Confirm `validation_report.json` is present.
  6. Confirm `qa_checklist.md` is present.
  7. Confirm `run_metadata.json` is present.
- Expected result: All seven artifacts are present and readable.
- Evidence to capture: File list or package manifest.
- Reviewer or role: Technical marketing analyst.
- Status: `todo`

## QA-002 — Google Ads remarketing consent review before consent

- Related finding ID: `F-002`
- Related rule ID: `GTM-CONSENT-001`
- Related change ID: none; no automated change was applied.
- Affected GTM entity: tag `106`, `Google Ads - Remarketing - All Pages`; trigger `206`, `PV - All Pages`.
- Scenario to test: Preview a pageview before advertising/remarketing consent is granted.
- Manual steps:
  1. Use a safe GTM review or preview context, not production publishing.
  2. Set the CMP or consent state to no advertising/remarketing consent.
  3. Load a representative page.
  4. Inspect GTM Preview for tag `106`.
  5. Inspect browser network requests for Google Ads remarketing activity.
- Expected result: Behavior matches the client's consent policy and applicable analyst/legal/privacy requirements. Do not assume the expected result from this package alone.
- Evidence to capture: Consent state, GTM Preview event, tag firing/non-firing status, network request notes with sensitive values redacted.
- Reviewer or role: Technical marketing analyst plus legal/privacy reviewer as appropriate.
- Status: `todo`

## QA-003 — Google Ads remarketing consent review after consent

- Related finding ID: `F-002`
- Related rule ID: `GTM-CONSENT-001`
- Related change ID: none; no automated change was applied.
- Affected GTM entity: tag `106`, `Google Ads - Remarketing - All Pages`; variable `306`, `CONST - Google Ads Conversion ID`.
- Scenario to test: Preview a pageview after advertising/remarketing consent is granted.
- Manual steps:
  1. Set the CMP or consent state to advertising/remarketing consent granted.
  2. Load a representative page.
  3. Confirm whether tag `106` fires on trigger `206`.
  4. Confirm the conversion ID value resolves as expected and does not expose unintended data.
- Expected result: Behavior matches the approved tracking plan and consent policy.
- Evidence to capture: GTM Preview logs, tag status, resolved conversion ID field, network request metadata with sensitive values redacted.
- Reviewer or role: Technical marketing analyst.
- Status: `todo`

## QA-004 — Custom HTML code review

- Related finding ID: `F-003`
- Related rule ID: `GTM-CONSENT-001`
- Related change ID: none; no automated change was applied.
- Affected GTM entity: tag `107`, `Custom HTML - Vendor Pixel`.
- Scenario to test: Review the visible Custom HTML and vendor endpoint before any use.
- Manual steps:
  1. Inspect the Custom HTML body.
  2. Confirm the external endpoint `vendor.example.test`.
  3. Review vendor documentation or source code where available.
  4. Check whether the script reads cookies, local storage, session storage, URL parameters, forms, user identifiers, or dataLayer values.
- Expected result: Analyst and developer understand the vendor script behavior and privacy implications before approving any import or production use.
- Evidence to capture: Code review notes, endpoint list, vendor documentation links, sensitive data field names only with raw values redacted.
- Reviewer or role: Technical marketing analyst/developer plus legal/privacy reviewer as appropriate.
- Status: `todo`

## QA-005 — Custom HTML network and consent behavior

- Related finding ID: `F-003`
- Related rule ID: `GTM-CONSENT-001`
- Related change ID: none; no automated change was applied.
- Affected GTM entity: tag `107`, `Custom HTML - Vendor Pixel`; trigger `206`, `PV - All Pages`.
- Scenario to test: Preview Custom HTML behavior before and after consent.
- Manual steps:
  1. In a safe preview context, load a page with no advertising/remarketing consent.
  2. Inspect whether tag `107` fires and whether `vendor.example.test` receives a request.
  3. Repeat after consent is granted.
  4. Confirm the result matches client policy and legal/privacy guidance.
- Expected result: Vendor script behavior matches approved consent expectations.
- Evidence to capture: Consent state, GTM Preview event, tag status, browser network request metadata with sensitive values redacted.
- Reviewer or role: Technical marketing analyst/developer plus legal/privacy reviewer as appropriate.
- Status: `todo`

## QA-006 — Rejection and rollback review

- Related finding IDs: `F-002`, `F-003`, `F-004`
- Related rule ID: `GTM-QA-001`
- Related change ID: none; `optimized_container.json` is identical to the source export.
- Affected GTM entity: package-level proposed recommendations.
- Scenario to test: Confirm there are no automated file-based changes to accept or reject.
- Manual steps:
  1. Compare source export and `optimized_container.json`.
  2. Confirm no consent settings, tag payloads, trigger logic, Custom HTML code, IDs, or entity names were changed.
  3. Document whether the human analyst rejects, defers, or separately implements the recommended consent review changes.
- Expected result: The file-based optimized JSON remains unchanged; any future change is made only after human approval in a safe GTM review process.
- Evidence to capture: Diff result, analyst decision, approval notes.
- Reviewer or role: Technical marketing analyst/client stakeholder.
- Status: `todo`
