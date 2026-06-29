# GTM Container Audit & Patch Package — Audit Report

## 1. Executive summary

Container reviewed: `Synthetic Duplicate Purchase Version` from `synthetic-duplicate-purchase-tags.json`. Fixture ID: `synthetic-duplicate-001`.

Overall risk level: **high**. The export contains two GA4 purchase event tags that appear to track the same `purchase` event on the same trigger with the same measurement ID variable and transaction ID variable. This matches the expected duplicate purchase tracking category and rules `GTM-DUP-001` and `GTM-ECOM-001`.

Finding counts:

- High: 2
- Medium: 0
- Low: 0
- Info: 2

Human approval is required before import, workspace creation, publishing, or production use. No GTM configuration changes were applied in `optimized_container.json`; duplicate ecommerce cleanup is manual-review-only.

This output is a draft proposal for human review.

## 2. Container inventory

Rule reference: `GTM-INV-001`

Observed from the exported JSON:

- Account ID: `9001`
- Container ID: `5103`
- Public ID: `GTM-SYN503`
- Container version name: `Synthetic Duplicate Purchase Version`
- Container name: `Synthetic Duplicate Purchase Container`
- Export format version: `2`
- Export time: `2026-06-09 00:00:00`
- Tags: 2
- Triggers: 1
- Variables: 2
- Folders: 1
- Built-in variables: 1
- Custom templates: 0
- Zones: 0

Audit limitation: the review is based only on the uploaded export fixture. Live site behavior, GTM Preview behavior, GA4 ingestion, consent behavior, and production safety were not verified.

## 3. Highest-risk findings

### F-DUP-001 — Duplicate GA4 purchase event tags fire on the same trigger

- Rule ID: `GTM-DUP-001`
- Severity: high
- Affected entities:
  - Tag `103`: `GA4 - Event - purchase`
  - Tag `104`: `GA4 - Event - purchase copy`
  - Trigger `203`: `CE - purchase`
- Detected facts:
  - Both affected tags use tag type `gaawe`.
  - Both set `eventName` to `purchase`.
  - Both use `{{CONST - GA4 Measurement ID}}` for the measurement ID.
  - Both use `{{DLV - ecommerce.transaction_id}}` for `transaction_id`.
  - Both fire on trigger ID `203`, named `CE - purchase`.
- Inferred issue: this appears to be duplicate GA4 purchase tracking. If both tags fire for the same purchase event, ecommerce reporting may be duplicated unless another mechanism deduplicates it.
- Recommended action: use GTM Preview and a controlled test purchase to confirm whether both tags fire. Do not delete, disable, or consolidate either tag automatically from this file export alone.
- Manual review: required.
- Related change: `CHG-001`.

### F-ECOM-001 — Purchase event tracking risk from duplicate GA4 ecommerce tags

- Rule ID: `GTM-ECOM-001`
- Severity: high
- Affected entities:
  - Tag `103`: `GA4 - Event - purchase`
  - Tag `104`: `GA4 - Event - purchase copy`
  - Variable `304`: `DLV - ecommerce.transaction_id`
  - Trigger `203`: `CE - purchase`
- Detected facts:
  - Both tags are GA4 `purchase` event tags.
  - Both include a `transaction_id` parameter mapped to `{{DLV - ecommerce.transaction_id}}`.
  - Variable `304` reads dataLayer key `ecommerce.transaction_id`.
  - The export does not show `value`, `currency`, or `items` parameters on either purchase tag.
- Inferred issue: duplicate firing may affect purchase counts or revenue reporting. Purchase payload completeness cannot be verified from this export alone.
- Recommended action: manually verify purchase event payload and deduplication behavior with GTM Preview and approved analytics debugging tools.
- Manual review: required.
- Related change: none applied.

## 4. Proposed changes

### CHG-001 — Duplicate GA4 purchase cleanup decision

- Related findings: `F-DUP-001`, `F-ECOM-001`
- Affected entities:
  - Tag `103`: `GA4 - Event - purchase`
  - Tag `104`: `GA4 - Event - purchase copy`
  - Trigger `203`: `CE - purchase`
- What would change: a human analyst may later choose to disable, remove, or consolidate one duplicate purchase tag after review.
- Why proposed: the two tags match on vendor/type, event name, measurement ID variable, transaction ID variable, and firing trigger.
- Risk level: high.
- Automated change policy: blocked for deletion/disabling; manual-review-only for duplicate cleanup.
- Rollback note: because no change was applied in this package, rollback is to keep both original tags unchanged. If an analyst later changes GTM, restore the source tag configuration from the original export if the decision is rejected.
- Human approval: required.

This proposed file-based package is not a live GTM mutation.

## 5. Changes applied in optimized JSON

No GTM configuration changes were applied in `optimized_container.json`.

Reason: `GTM-DUP-001` and `GTM-ECOM-001` treat duplicate ecommerce cleanup, deletion, disabling, and ecommerce payload changes as manual-review-only or blocked for automation in this MLP.

`optimized_container.json` is a proposed artifact, not a publish-ready guarantee.

## 6. Changes recommended but not applied

- Recommended review: determine whether tag `104` is an accidental duplicate of tag `103`.
  - Reason not applied: duplicate ecommerce tag cleanup could affect purchase tracking and reporting.
  - Manual-review trigger: purchase/revenue tracking and deletion/disabling decision.
  - Rule IDs: `GTM-DUP-001`, `GTM-ECOM-001`.
  - Analyst next step: use GTM Preview and a controlled test purchase before deciding which tag should remain active.

- Recommended review: confirm purchase payload completeness.
  - Reason not applied: adding or editing ecommerce fields changes tracking payloads and cannot be safely inferred from this export.
  - Manual-review trigger: ecommerce value, currency, item, and transaction ID mapping.
  - Rule ID: `GTM-ECOM-001`.
  - Analyst next step: compare GTM Preview output with dataLayer and GA4 ecommerce implementation requirements.

## 7. Validation results

Validation status: `pass_with_warnings`.

Checks performed:

- Source JSON parsed successfully.
- Required package artifacts are represented.
- `optimized_container.json` preserves the full source GTM export structure.
- Tag firing trigger references point to existing trigger ID `203`.
- Tag folder references point to existing folder ID `403`.

Warnings:

- Duplicate GA4 purchase tag cleanup was not applied because ecommerce deletion/disabling decisions require manual review.
- No live GTM Preview, GA4 DebugView, consent, or production behavior validation was performed.
- Purchase tags show `transaction_id`, but this fixture export does not show `value`, `currency`, or `items` parameters.

Validation results do not prove tracking correctness, consent behavior, legal compliance, privacy compliance, or production readiness.

## 8. QA checklist

Highest-priority QA items from `qa_checklist.md`:

- `QA-002`: run GTM Preview for a controlled purchase event and confirm whether tags `103` and `104` both fire.
- `QA-003`: confirm `ecommerce.transaction_id` resolves and is not duplicated unexpectedly.
- `QA-004`: document the human decision before disabling, removing, or consolidating either purchase tag.
- `QA-005`: confirm purchase payload completeness, including expected handling for value, currency, and items.
- `QA-006`: confirm approval boundaries before import, workspace creation, publishing, or production use.

## 9. Human approval notes

Human review is required before import, workspace creation, publishing, or production use.

Recommended reviewers:

- Technical marketing analyst for GTM configuration review.
- Analytics owner for GA4 purchase and ecommerce reporting expectations.
- Client stakeholder if tag removal or consolidation could affect reporting continuity.

This package did not connect to, inspect, change, import, publish, or verify any live GTM, GA4, Google Ads, API, workspace, website, or production platform.

## 10. Appendix: entity-level findings

### F-INV-001

- Rule ID: `GTM-INV-001`
- Severity: info
- Category: inventory
- Affected entity: container `5103` / `Synthetic Duplicate Purchase Version`
- Detected facts: the source export contains 2 tags, 1 trigger, 2 variables, 1 folder, 1 built-in variable, and 0 custom templates.
- Recommendation: use the inventory as the audit scope boundary.
- Automated-change policy: blocked.
- Related QA item: `QA-001`.

### F-DUP-001

- Rule ID: `GTM-DUP-001`
- Severity: high
- Category: duplicates
- Affected entities: tag `103`, tag `104`, trigger `203`
- Evidence: both tags are `gaawe`, both use `purchase`, both use `{{CONST - GA4 Measurement ID}}`, both use `{{DLV - ecommerce.transaction_id}}`, and both fire on `CE - purchase`.
- Recommendation: manual duplicate cleanup decision after GTM Preview.
- Automated-change policy: manual-review-only; deletion/disabling blocked for automation.
- Manual-review triggers: duplicate ecommerce tracking, purchase event, deletion/disabling decision.
- Related change: `CHG-001`.
- Related QA items: `QA-002`, `QA-003`, `QA-004`.

### F-ECOM-001

- Rule ID: `GTM-ECOM-001`
- Severity: high
- Category: ecommerce
- Affected entities: tag `103`, tag `104`, variable `304`, trigger `203`
- Evidence: both tags track `purchase` and map `transaction_id` to `{{DLV - ecommerce.transaction_id}}`; the export does not show `value`, `currency`, or `items` parameters on either tag.
- Recommendation: manually verify purchase event payload and deduplication behavior.
- Automated-change policy: manual-review-only.
- Manual-review triggers: purchase tracking, transaction ID mapping, ecommerce payload uncertainty.
- Related QA items: `QA-002`, `QA-003`, `QA-005`.

### F-REF-001

- Rule ID: `GTM-REF-001`
- Severity: info
- Category: reference integrity
- Affected entity: container `5103` / `Synthetic Duplicate Purchase Version`
- Evidence: trigger ID `203` and folder ID `403` referenced by the purchase tags exist in the export; variable names referenced in tag parameters match exported variables.
- Recommendation: no reference repair is proposed. Manual QA is still required.
- Automated-change policy: blocked.
- Related QA item: `QA-001`.
