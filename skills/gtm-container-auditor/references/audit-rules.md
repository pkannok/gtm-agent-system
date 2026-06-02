# GTM Audit Rule Catalog

## Purpose

This catalog defines the first-pass audit rules for the GTM Container Audit & Patch Package.

Future Custom GPT and Skill workflows should cite these rule IDs in `audit_report.json` findings and use them to keep `audit_report.md`, `change_log.json`, `validation_report.json`, and `qa_checklist.md` consistent.

The catalog is a standards reference, not an audit script. It does not run audits, validate live site behavior, publish GTM changes, certify legal compliance, certify privacy compliance, or make generated GTM JSON safe to publish. All generated GTM artifacts remain draft proposals for human analyst review before import, workspace creation, publishing, or production use.

## How to Use Rule IDs

Each audit finding should include:

- `rule_id`
- Finding severity.
- Affected GTM entity type.
- Affected entity ID and name, if available.
- Evidence gathered from the GTM container export.
- Recommended action.
- Whether automated change is allowed, blocked, or manual-review only.
- Related proposed change ID when a proposed file-based change is included.

Example finding citation:

```text
Rule ID: GTM-NAME-001
Affected entity: tag 12, "GA4"
Evidence: Tag type appears to be GA4 event, but the name does not identify event purpose.
Recommended action: Rename to a project-specific format from standards/agency/naming-conventions.md.
```

## Severity Guidance

- `info`: Useful context or inventory note. No defect is implied.
- `low`: Low-risk cleanup opportunity, usually documentation, naming, or organization.
- `medium`: Meaningful risk, ambiguity, broken references, duplicate behavior, or consent-sensitive uncertainty that requires analyst review.
- `high`: Likely tracking breakage, sensitive data risk, consent/risk issue, ecommerce revenue risk, or a proposed action that could affect production behavior.

Schema validation, naming cleanup, and rule matching do not prove tracking correctness, consent behavior, legal compliance, privacy compliance, or production readiness.

## Automated Change Policy Values

- `allowed_candidate`: The MLP may propose a file-based change in `optimized_container.json` and record it in `change_log.json`, but human review is still required.
- `manual_review_only`: The MLP may recommend a change, but should not apply it to `optimized_container.json` without human analyst review.
- `blocked`: The MLP must not apply the change. It may document the issue and add QA or manual-review guidance.

## GTM-INV-001 - Container Inventory Completeness

Rule ID:
`GTM-INV-001`

Category:
Inventory.

Severity guidance:
Use `info` for normal inventory summaries. Use `low` when entity counts or grouping patterns suggest documentation gaps. Use `medium` when inventory data is missing, malformed, or inconsistent enough to limit audit confidence.

What to inspect:
Container metadata, export format version, account ID, container ID, container name, tags, triggers, variables, folders, templates, and zones when present.

Evidence required:
Source filename, container identifiers, export format version, entity counts by type, and any missing or malformed top-level sections.

Recommended action:
Summarize the container inventory in `audit_report.md` and `audit_report.json`. Flag missing or malformed inventory sections as audit limitations.

Automated change policy:
`blocked`. Inventory findings should not create optimized GTM changes.

Manual-review triggers:
Missing top-level sections, malformed entity arrays, unknown export format, unexpectedly empty container, or container identity mismatch.

Related output artifact:
`audit_report.json`, `audit_report.md`, `run_metadata.json`.

## GTM-REF-001 - Reference Integrity

Rule ID:
`GTM-REF-001`

Category:
Reference integrity.

Severity guidance:
Use `medium` for unresolved references that may prevent tags, triggers, or variables from working. Use `high` when a broken reference affects ecommerce, consent-sensitive tags, advertising conversions, or broad sitewide tracking.

What to inspect:
Tag-to-trigger references, tag-to-variable references, variable references inside tag parameters, trigger filters, folder references, template references, and any IDs or names referenced by configuration.

Evidence required:
Affected entity ID and name, referenced entity ID or name, reference location, whether the referenced entity exists, and the likely impact.

Recommended action:
Report the broken or ambiguous reference and recommend human review. If the intended target is obvious from file evidence, propose a manual-review-only correction.

Automated change policy:
`manual_review_only`. Do not automatically repair references unless a later task explicitly authorizes deterministic repair behavior.

Manual-review triggers:
Any broken reference, ambiguous target, Custom HTML or custom template involvement, consent-sensitive tag involvement, ecommerce involvement, or cross-vendor conversion tracking involvement.

Related output artifact:
`audit_report.json`, `audit_report.md`, `validation_report.json`, `qa_checklist.md`, and `change_log.json` only when a proposed correction is documented.

## GTM-DUP-001 - Duplicate or Overlapping Tracking

Rule ID:
`GTM-DUP-001`

Category:
Duplicates.

Severity guidance:
Use `low` for duplicate naming or clearly inactive duplicate candidates. Use `medium` for likely duplicate tags firing on similar triggers. Use `high` for duplicate ecommerce, conversion, remarketing, or revenue-affecting tags.

What to inspect:
Tags with same vendor, event name, conversion label, pixel ID, measurement ID, trigger set, ecommerce payload, or similar Custom HTML endpoints. Also inspect duplicate triggers and variables that appear to serve the same purpose.

Evidence required:
Entity IDs and names for all duplicate candidates, matching fields, trigger overlap, vendor/platform signal, and why the items appear duplicate rather than intentionally separate.

Recommended action:
Identify duplicate candidates and recommend analyst review. For low-risk naming duplicates, suggest consolidation naming only. For firing or payload duplicates, recommend GTM Preview testing and manual review.

Automated change policy:
`manual_review_only` for duplicate cleanup. `blocked` for deleting or disabling entities in the MLP.

Manual-review triggers:
Any duplicate candidate that affects conversions, ecommerce, consent-sensitive tags, Custom HTML, all-pages firing, or vendor-managed tags.

Related output artifact:
`audit_report.json`, `audit_report.md`, `qa_checklist.md`, and `change_log.json` only for proposed file-based, reviewable changes.

## GTM-UNUSED-001 - Unused or Orphaned Entities

Rule ID:
`GTM-UNUSED-001`

Category:
Unused entities.

Severity guidance:
Use `low` for unused folders or variables with no obvious risk. Use `medium` for unused triggers, tags, templates, or variables that may be legacy or unclear. Use `high` only when unused-looking entities are connected to consent, Custom HTML, ecommerce, or conversion tracking and could be misclassified.

What to inspect:
Variables with no references, triggers not attached to tags, folders with stale groupings, templates not used by tags, and tags that appear inactive only from exported configuration.

Evidence required:
Entity ID and name, entity type, reference count from the export, related folders, related templates, and uncertainty notes.

Recommended action:
Flag unused candidates for analyst review. Recommend archive notes or QA review, not deletion.

Automated change policy:
`blocked` for deletion. `manual_review_only` for renaming or archive labeling.

Manual-review triggers:
Any delete, disable, or archive recommendation; any entity with `legacy`, `do not delete`, `hold`, `vendor managed`, `consent`, `privacy`, or `client approved` in its name; and any entity that could be referenced outside the exported GTM configuration.

Related output artifact:
`audit_report.json`, `audit_report.md`, `qa_checklist.md`, and `change_log.json` only if a non-delete proposed change is documented.

## GTM-NAME-001 - Naming Standard Alignment

Rule ID:
`GTM-NAME-001`

Category:
Naming.

Severity guidance:
Use `low` for clear name-only cleanup. Use `medium` when the name is ambiguous enough to affect review or QA. Use `high` only when the naming issue hides consent-sensitive, ecommerce, conversion, or Custom HTML risk.

What to inspect:
Tag names, trigger names, variable names, folder names, and future recipe names against `standards/agency/naming-conventions.md`.

Evidence required:
Entity type, entity ID, current name, inferred platform or purpose, relevant naming rule, proposed name when available, and whether the rename is name-only.

Recommended action:
Suggest a clear name that follows the naming convention when evidence is sufficient. Mark ambiguous or risky rename candidates for manual review.

Automated change policy:
`allowed_candidate` only for low-risk name-only cleanup with clear evidence and no manual-review trigger. `manual_review_only` for Custom HTML, custom templates, custom JavaScript variables, consent-sensitive entities, or inferred names.

Manual-review triggers:
Custom HTML, custom templates, custom JavaScript variables, consent-sensitive tags, ecommerce tags, vendor-managed tags, names with warnings, or any name referenced outside GTM.

Related output artifact:
`audit_report.json`, `audit_report.md`, `change_log.json`, and `optimized_container.json` only for proposed file-based name-only changes.

## GTM-ECOM-001 - Ecommerce Tracking Integrity

Rule ID:
`GTM-ECOM-001`

Category:
Ecommerce.

Severity guidance:
Use `medium` for incomplete, ambiguous, or inconsistent ecommerce tracking signals. Use `high` for purchase, revenue, transaction ID, item array, or conversion tracking risks that may affect reporting or optimization.

What to inspect:
GA4 ecommerce event tags, purchase events, add-to-cart events, checkout events, dataLayer variables for transaction ID, value, currency, items, coupon, affiliation, and any Google Ads or platform conversion tags using ecommerce values.

Evidence required:
Affected tag and variable IDs, ecommerce event names, dataLayer key names, required parameters observed or missing, related triggers, conversion linkage, and assumptions.

Recommended action:
Flag missing or inconsistent ecommerce fields and recommend manual QA with GTM Preview and test purchases where appropriate. Recommend dataLayer documentation review when keys are unclear.

Automated change policy:
`manual_review_only` for recommendations. `blocked` for changing ecommerce payloads, dataLayer keys, event names, values, currency, item arrays, or conversion labels in the MLP.

Manual-review triggers:
Purchase or revenue tracking, transaction IDs, item arrays, currency/value parameters, enhanced conversions, advertising conversions, Custom HTML, custom JavaScript, or inferred dataLayer mapping.

Related output artifact:
`audit_report.json`, `audit_report.md`, `qa_checklist.md`, `validation_report.json`, and `change_log.json` only when a proposed reviewable change is documented.

## GTM-CONSENT-001 - Consent and Privacy Risk

Rule ID:
`GTM-CONSENT-001`

Category:
Consent/risk.

Severity guidance:
Use `medium` for advertising, remarketing, user identifier, or Custom HTML findings that require consent review. Use `high` when sensitive data, enhanced conversions, broad all-pages remarketing, missing consent settings, or unclear user identifier handling is involved.

What to inspect:
Advertising tags, remarketing tags, Custom HTML, enhanced conversion fields, user identifiers, sensitive data variables, consent settings, CMP tags, consent initialization triggers, and broad all-pages firing behavior.

Evidence required:
Affected entity ID and name, vendor/platform signal, consent settings observed, trigger scope, sensitive field names, Custom HTML or template signal, and whether the issue is detected or inferred.

Recommended action:
Flag consent-sensitive entities for analyst review using `standards/agency/consent-standard.md`. Recommend GTM Preview, network inspection, and appropriate legal/privacy review where applicable.

Automated change policy:
`blocked` for consent-sensitive changes in the MLP. Do not add consent settings, remove tags, edit payloads, edit Custom HTML, or add/remove identifiers.

Manual-review triggers:
Any advertising or remarketing vendor tag, Custom HTML, enhanced conversions, user identifiers, sensitive data fields, missing or unclear consent settings, all-pages vendor tags, or uncertainty about consent sensitivity.

Related output artifact:
`audit_report.json`, `audit_report.md`, `qa_checklist.md`, and `validation_report.json`. Use `change_log.json` only for non-sensitive documentation or naming proposals that still require review.

## GTM-QA-001 - QA and Preview Readiness

Rule ID:
`GTM-QA-001`

Category:
QA.

Severity guidance:
Use `info` for routine QA recommendations. Use `low` for straightforward preview steps. Use `medium` when QA is needed for meaningful tracking risk. Use `high` when QA is required before trusting ecommerce, consent-sensitive, conversion, or Custom HTML behavior.

What to inspect:
Findings, proposed changes, validation results, risk summary, affected entities, trigger scopes, Custom HTML, ecommerce tags, consent-sensitive tags, and any optimized-container changes.

Evidence required:
Finding IDs, proposed change IDs, affected entities, risk level, required GTM Preview scenarios, expected events or tags to verify, and manual-review owner when known.

Recommended action:
Add concrete QA checklist items to `qa_checklist.md`, including preview scenarios, test events, expected tag behavior, and items that require analyst review.

Automated change policy:
`blocked`. QA findings should not modify GTM configuration. They should create review and testing guidance only.

Manual-review triggers:
Any proposed change, any high-risk finding, any consent-sensitive finding, any ecommerce finding, any Custom HTML finding, or any validation warning/failure.

Related output artifact:
`qa_checklist.md`, `audit_report.md`, `audit_report.json`, and `validation_report.json`.
