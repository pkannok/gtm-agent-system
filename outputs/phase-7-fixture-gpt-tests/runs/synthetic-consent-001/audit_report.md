# audit_report.md

# GTM Container Audit & Patch Package

Fixture ID: `synthetic-consent-001`
Run ID: `gtm-audit-synthetic-consent-001-20260626T220218Z`
Source file: `synthetic-consent-risk-remarketing.json`
Generated at: `2026-06-26T22:02:18Z`

This output is a draft proposal for human review. Human review is required before import, workspace creation, publishing, or production use.

## 1. Executive summary

The export is for container `Synthetic Consent Risk Container` (`GTM-SYN506`) from `synthetic-consent-risk-remarketing.json`.

Overall risk level: **high**.

Finding counts:

- High: 3
- Medium: 0
- Low: 0
- Info: 1

The highest-risk issues are consent-sensitive all-pages firing patterns:

1. Tag `106`, `Google Ads - Remarketing - All Pages`, appears to be a broad advertising/remarketing tag firing on `PV - All Pages` without clear consent evidence in the export.
2. Tag `107`, `Custom HTML - Vendor Pixel`, loads an external vendor script and fires on `PV - All Pages` without clear consent evidence in the export.

No proposed file-based changes were applied to `optimized_container.json`. The optimized JSON is intentionally identical to the source export because consent-sensitive changes, Custom HTML edits, trigger changes, removals, and consent setting changes are blocked for automation in this MLP package.

## 2. Container inventory

Rule ID: `GTM-INV-001`

Observed from the export:

- Account ID: `9001`
- Container ID: `5106`
- Public ID: `GTM-SYN506`
- Container name: `Synthetic Consent Risk Container`
- Container version name: `Synthetic Consent Risk Version`
- Export format version: `2`
- Export time: `2026-06-09 00:00:00`

Entity counts:

| Entity type | Count |
| --- | ---: |
| Tags | 2 |
| Triggers | 1 |
| Variables | 1 |
| Folders | 1 |
| Built-in variables | 1 |
| Custom templates | 0 |
| Zones | 0 |

Reference integrity checks from the export found the observed tag-to-trigger, tag-to-variable, and tag-to-folder references resolvable. This does not verify live site behavior.

## 3. Highest-risk findings

### F-002 — All-pages Google Ads remarketing tag lacks clear consent evidence in export

- Rule ID: `GTM-CONSENT-001`
- Severity: `high`
- Affected entities:
  - Tag `106`, `Google Ads - Remarketing - All Pages`
  - Trigger `206`, `PV - All Pages`
  - Variable `306`, `CONST - Google Ads Conversion ID`
- Detected facts:
  - Tag `106` is named `Google Ads - Remarketing - All Pages`.
  - Tag `106` has type `sp` and includes conversion ID variable reference `{{CONST - Google Ads Conversion ID}}`.
  - Variable `306` resolves to `AW-TEST506` in the export.
  - Tag `106` fires on trigger `206`, `PV - All Pages`, type `PAGEVIEW`.
  - No explicit tag-level consent settings, blocking trigger, consent initialization tag, or CMP tag were observed in the export.
- Inferred issue: This appears to be a broad remarketing/audience tag for an advertising vendor firing on all page views without clear consent gating evidence in the export.
- Recommended action: Require analyst consent review. Confirm intended consent categories, GTM consent settings, CMP behavior, blocking/exception triggers, and network behavior in GTM Preview.
- Manual review required: Yes.
- Related change ID: none; unsafe automated changes were blocked.

### F-003 — Custom HTML vendor pixel fires on all pages without clear consent evidence

- Rule ID: `GTM-CONSENT-001`
- Severity: `high`
- Affected entities:
  - Tag `107`, `Custom HTML - Vendor Pixel`
  - Trigger `206`, `PV - All Pages`
- Detected facts:
  - Tag `107` has type `html`, which is Custom HTML.
  - The visible HTML loads `https://vendor.example.test/pixel.js`.
  - Tag `107` fires on trigger `206`, `PV - All Pages`, type `PAGEVIEW`.
  - No explicit tag-level consent settings, blocking trigger, consent initialization tag, or CMP tag were observed in the export.
- Inferred issue: This appears to be an external vendor pixel script firing broadly on all page views. The export alone does not show whether the vendor code reads cookies, identifiers, storage, URL parameters, forms, or other user data.
- Recommended action: Require human code review, consent review, GTM Preview testing, and browser network inspection.
- Manual review required: Yes.
- Related change ID: none; Custom HTML and consent-sensitive automated changes were blocked.

### F-004 — Manual GTM Preview and consent-sensitive QA required before any use

- Rule ID: `GTM-QA-001`
- Severity: `high`
- Affected entities:
  - Tag `106`, `Google Ads - Remarketing - All Pages`
  - Tag `107`, `Custom HTML - Vendor Pixel`
- Detected facts:
  - Two consent-sensitive tags fire on the all-pages pageview trigger.
  - No live site behavior was inspected and no GTM Preview session was executed by this file-in/file-out run.
- Recommendation: Complete `qa_checklist.md` before import, workspace creation, publishing, or production use.

## 4. Proposed changes

No file-based GTM configuration changes are proposed for direct inclusion in this package.

Recommended review actions were recorded in `change_log.json` as `not_applied_recommendations`:

- `REC-001`: Review consent gating for tag `106`, `Google Ads - Remarketing - All Pages`.
- `REC-002`: Review Custom HTML code and vendor endpoint for tag `107`, `Custom HTML - Vendor Pixel`.

These recommendations are not live GTM mutations and are not applied in `optimized_container.json`.

## 5. Changes applied in optimized JSON

No changes were applied.

`optimized_container.json` is a proposed artifact, not a publish-ready guarantee. In this package it is intentionally identical to the source export because the detected risks require human review rather than automated edits.

## 6. Changes recommended but not applied

### REC-001 — Consent gating review for Google Ads remarketing

- Related finding ID: `F-002`
- Rule ID: `GTM-CONSENT-001`
- Reason not applied: Consent-sensitive changes are blocked for automation. Adding consent settings, changing triggers, removing tags, or editing payloads could alter production behavior.
- Manual-review trigger: advertising vendor tag, remarketing signal, all-pages trigger, missing or unclear consent settings.
- Suggested analyst next step: Review the consent plan and test before/after consent states in GTM Preview and browser network tools.

### REC-002 — Custom HTML vendor pixel review

- Related finding ID: `F-003`
- Rule ID: `GTM-CONSENT-001`
- Reason not applied: Custom HTML and consent-sensitive code edits are blocked for automation.
- Manual-review trigger: Custom HTML, external script, all-pages trigger, missing or unclear consent settings.
- Suggested analyst next step: Review the code and vendor endpoint, then test before/after consent states in GTM Preview and browser network tools.

## 7. Validation results

Package validation summary:

- Required artifacts generated: 7 of 7.
- JSON artifacts parse: yes.
- Source export parses as JSON: yes.
- Optimized container parses as JSON: yes.
- Optimized container is identical to source: yes.
- Live platform validation: not performed and out of scope.

Validation results do not prove tracking correctness, consent behavior, legal compliance, privacy compliance, or production readiness.

## 8. QA checklist

Highest-priority QA items from `qa_checklist.md`:

- `QA-002`: Test Google Ads remarketing behavior before advertising/remarketing consent.
- `QA-003`: Test Google Ads remarketing behavior after advertising/remarketing consent.
- `QA-004`: Review Custom HTML and the external vendor endpoint.
- `QA-005`: Test Custom HTML network behavior before and after consent.
- `QA-006`: Confirm no automated file-based changes were applied and document the analyst decision.

The MLP did not execute QA. Manual verification is required.

## 9. Human approval notes

Human review is required before import, workspace creation, publishing, or production use.

Recommended reviewers:

- Technical marketing analyst for GTM structure, tag behavior, and preview testing.
- Developer or technical owner for Custom HTML code review.
- Legal/privacy reviewer or appropriate client stakeholder for consent-sensitive advertising and vendor pixel behavior.

This package did not connect to, inspect, change, import, publish, or verify any live GTM, GA4, Google Ads, API, workspace, website, or production platform.

## 10. Appendix: entity-level findings

### F-001

- Rule ID: `GTM-INV-001`
- Severity: `info`
- Category: inventory
- Affected entity: container `5106`, `Synthetic Consent Risk Container`
- Detected facts: The source export was parsed and inventory counts were captured.
- Recommendation: Use the inventory as audit scope and preserve limitations around live behavior.
- Automated-change policy: `blocked`
- Manual-review requirement: No
- Related QA item IDs: `QA-001`

### F-002

- Rule ID: `GTM-CONSENT-001`
- Severity: `high`
- Category: consent/risk
- Affected entity type: tag
- Affected entity ID and name: `106`, `Google Ads - Remarketing - All Pages`
- Evidence: Tag type `sp`, conversion ID variable reference, all-pages pageview trigger, no clear consent settings observed in export.
- Recommendation: Consent review and GTM Preview/network testing.
- Automated-change policy: `blocked`
- Manual-review triggers: advertising vendor tag, remarketing signal, all-pages trigger, missing or unclear consent settings.
- Related change IDs: none
- Related QA item IDs: `QA-002`, `QA-003`, `QA-006`

### F-003

- Rule ID: `GTM-CONSENT-001`
- Severity: `high`
- Category: consent/risk
- Affected entity type: tag
- Affected entity ID and name: `107`, `Custom HTML - Vendor Pixel`
- Evidence: Tag type `html`, external script `https://vendor.example.test/pixel.js`, all-pages pageview trigger, no clear consent settings observed in export.
- Recommendation: Custom HTML code review, consent review, GTM Preview testing, and browser network inspection.
- Automated-change policy: `blocked`
- Manual-review triggers: Custom HTML, external script, all-pages trigger, missing or unclear consent settings.
- Related change IDs: none
- Related QA item IDs: `QA-004`, `QA-005`, `QA-006`

### F-004

- Rule ID: `GTM-QA-001`
- Severity: `high`
- Category: QA
- Affected entity type: tags
- Affected entity IDs and names: `106`, `Google Ads - Remarketing - All Pages`; `107`, `Custom HTML - Vendor Pixel`
- Evidence: Consent-sensitive all-pages tags observed; live QA not performed.
- Recommendation: Complete manual QA before any import, workspace creation, publishing, or production use.
- Automated-change policy: `blocked`
- Manual-review triggers: consent-sensitive findings, Custom HTML, all-pages advertising/vendor behavior.
- Related change IDs: none
- Related QA item IDs: `QA-001`, `QA-002`, `QA-003`, `QA-004`, `QA-005`, `QA-006`
