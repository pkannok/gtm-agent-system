# GTM Container Audit & Patch Package

## 1. Executive summary

Source file: `synthetic-broken-references.json`
Fixture ID: `synthetic-reference-001`
Container: `Synthetic Broken References Container` (`GTM-SYN502`)
Overall risk level: **high**

Finding counts: **3 high**, **2 medium**, **0 low**, **1 info**.

Human approval is required before import, workspace creation, publishing, or production use. This output is a draft proposal for human review. No live GTM, GA4, Google Ads, website, API, workspace, or production platform was connected to, inspected, changed, imported, published, or verified.

No changes were applied in `optimized_container.json`. The source export was preserved because the detected issues are broken references and ecommerce mapping risks that require manual review under `GTM-REF-001` and `GTM-ECOM-001`.

## 2. Container inventory

- Account ID: `9001`
- Container ID: `5102`
- Container public ID: `GTM-SYN502`
- Container name: `Synthetic Broken References Container`
- Container version name: `Synthetic Broken References Version`
- Export format version: `2`
- Export time: `2026-06-09 00:00:00`
- Tags: `1`
- Triggers: `1`
- Variables: `1`
- Folders: `1`
- Built-in variables: `1`
- Custom templates: `0`
- Zones: `0`

Inventory rule: `GTM-INV-001`.

## 3. Highest-risk findings

### F-REF-001 — `GTM-REF-001` — high

Affected entity: tag `102`, `GA4 - Event - Purchase`.

Detected facts:
- The tag has `firingTriggerId` value `299`.
- No trigger with `triggerId` `299` exists in the export.
- The export does contain trigger `202`, `CE - purchase`, but the referenced ID does not match.

Inferred issue: the GA4 purchase tag may not fire as intended because its firing trigger reference is unresolved.

Recommended action: manually confirm the intended firing trigger. Trigger `202` is a plausible candidate by name, but changing trigger references can affect purchase tracking behavior and was not applied automatically.

Related recommended change: `CHG-REC-001`.

### F-REF-003 — `GTM-REF-001` — high

Affected entity: tag `102`, `GA4 - Event - Purchase`.

Detected facts:
- The tag parameter key `value` references `{{Missing Revenue}}`.
- No variable named `Missing Revenue` exists in the export.
- The export contains variable `302`, `DLV - ecommerce.transaction_id`, but that variable does not match the referenced revenue token.

Inferred issue: the GA4 purchase event value may resolve to an undefined value, affecting ecommerce revenue reporting.

Recommended action: manually confirm the intended revenue variable and dataLayer key before adding, renaming, or remapping any variable.

Related recommended change: `CHG-REC-003`.

### F-ECOM-001 — `GTM-ECOM-001` — high

Affected entity: tag `102`, `GA4 - Event - Purchase`.

Detected facts:
- The tag appears to be a GA4 event-style tag with `eventName` set to `purchase`.
- The `value` parameter references `{{Missing Revenue}}`.
- Currency and item array mappings were not detected from the export.

Inferred issue: purchase revenue reporting may be incomplete or broken.

Recommended action: review ecommerce dataLayer documentation and validate a test purchase in GTM Preview after any analyst-approved reference repair.

## 4. Proposed changes

No changes were applied to `optimized_container.json`.

The following recommendations are documented in `change_log.json` but not applied:

- `CHG-REC-001`: potential trigger reference repair for tag `102`, from missing trigger ID `299` to a confirmed intended trigger. Candidate target: trigger `202`, `CE - purchase`. Risk: high. Policy: manual-review only.
- `CHG-REC-002`: potential folder reference repair for tag `102`, from missing folder ID `499` to a confirmed intended folder. Candidate target: folder `402`, `GA4 - Ecommerce`. Risk: medium. Policy: manual-review only.
- `CHG-REC-003`: potential revenue variable repair for tag `102`, replacing or resolving `{{Missing Revenue}}` only after confirming the correct revenue dataLayer key. Risk: high. Policy: manual-review only.

These are file-based recommendations only, not live GTM mutations.

## 5. Changes applied in optimized JSON

No changes are reflected in `optimized_container.json`.

`optimized_container.json` is a proposed artifact, not a publish-ready guarantee. It preserves the uploaded source export exactly because the detected changes would affect trigger logic, folder assignment, or ecommerce value mapping and require human analyst review.

## 6. Changes recommended but not applied

- Trigger reference repair was not applied because `GTM-REF-001` is manual-review only and changing `firingTriggerId` can alter purchase tracking.
- Folder reference repair was not applied because the folder target is plausible but not deterministic from the export alone.
- Revenue variable repair was not applied because changing ecommerce value mapping requires confirmed dataLayer documentation and manual QA.
- No deletion, disabling, or archiving was applied for apparently orphaned trigger `202`, folder `402`, or variable `302`.

## 7. Validation results

Validation status: `failed_with_manual_review_required`.

Failed checks:
- Tag `102` references missing trigger ID `299`.
- Tag `102` references missing folder ID `499`.
- Tag `102` references missing variable token `{{Missing Revenue}}`.

Passed checks:
- Source JSON parsed.
- GTM export shape was detected.
- All seven required artifacts were generated.
- `optimized_container.json` parses as JSON.

Validation results do not prove tracking correctness, consent behavior, legal compliance, privacy compliance, or production readiness.

## 8. QA checklist

Highest-priority QA items are in `qa_checklist.md`:

- Confirm all seven package artifacts exist and parse.
- Review broken references for tag `102`.
- Confirm the intended firing trigger, folder, and revenue variable before making any repair.
- Run a test purchase flow in GTM Preview after analyst-approved changes.
- Capture redacted evidence for purchase event firing and ecommerce parameters.

## 9. Human approval notes

Human review is required before import, workspace creation, publishing, or production use.

Recommended reviewers:
- GTM analyst for reference integrity and package review.
- Developer or dataLayer owner for revenue variable and ecommerce payload confirmation.
- Client stakeholder or analytics owner before accepting any purchase tracking repair.

This package does not publish, deploy, import, create a workspace, or verify a production platform.

## 10. Appendix: entity-level findings

### F-INV-001 — GTM-INV-001 — info

Category: `inventory`
Affected entities: container `5102`, `Synthetic Broken References Container`

Detected facts:
- Source filename: synthetic-broken-references.json.
- Fixture ID: synthetic-reference-001.
- Export format version: 2.
- Account ID: 9001; container ID: 5102; public ID: GTM-SYN502.
- Entity counts observed: 1 tag, 1 trigger, 1 variable, 1 folder, 0 custom template, 1 built-in variable, 0 zone.

Inferred issue: None detected from this finding.

Recommendation: Use this inventory as audit coverage context. No GTM configuration change is proposed from this finding.

Automated-change policy: `blocked`

Manual review required: `false`

Related QA item IDs: QA-001

### F-REF-001 — GTM-REF-001 — high

Category: `reference_integrity`
Affected entities: tag `102`, `GA4 - Event - Purchase`

Detected facts:
- Tag 102 named "GA4 - Event - Purchase" has firingTriggerId "299".
- No trigger with triggerId "299" exists in the exported trigger array.
- The export does contain trigger 202 named "CE - purchase" but this is not the referenced ID.

Inferred issue: The GA4 purchase event tag may not fire as intended because its firing trigger reference is unresolved in the export.

Recommendation: Manual review required. Confirm the intended firing trigger in GTM or source documentation. A likely candidate by name is trigger 202, "CE - purchase", but the MLP does not automatically repair ambiguous trigger references.

Automated-change policy: `manual_review_only`

Manual review required: `true`

Manual-review triggers:
- `broken_reference`
- `trigger_logic_change`
- `ecommerce_purchase_event`

Related change IDs: CHG-REC-001

Related QA item IDs: QA-002, QA-003

### F-REF-002 — GTM-REF-001 — medium

Category: `reference_integrity`
Affected entities: tag `102`, `GA4 - Event - Purchase`

Detected facts:
- Tag 102 named "GA4 - Event - Purchase" has parentFolderId "499".
- No folder with folderId "499" exists in the exported folder array.
- The export does contain folder 402 named "GA4 - Ecommerce" but this is not the referenced ID.

Inferred issue: The tag's folder assignment is unresolved. This is primarily an organization and reviewability issue, not direct firing behavior.

Recommendation: Manual review required. Confirm intended folder assignment. A likely candidate by name is folder 402, "GA4 - Ecommerce", but the MLP does not automatically repair ambiguous folder references.

Automated-change policy: `manual_review_only`

Manual review required: `true`

Manual-review triggers:
- `broken_reference`
- `ambiguous_target`

Related change IDs: CHG-REC-002

Related QA item IDs: QA-002, QA-004

### F-REF-003 — GTM-REF-001 — high

Category: `reference_integrity`
Affected entities: tag `102`, `GA4 - Event - Purchase`

Detected facts:
- Tag 102 named "GA4 - Event - Purchase" parameter key "value" references variable token "{{Missing Revenue}}".
- No variable named "Missing Revenue" exists in the exported variable array.
- The export contains variable 302 named "DLV - ecommerce.transaction_id" with dataLayer key "ecommerce.transaction_id"; this does not match the referenced token.

Inferred issue: The GA4 purchase event value may resolve to an undefined value, which may affect ecommerce revenue reporting.

Recommendation: Manual review required. Confirm the intended revenue variable and dataLayer key before adding, renaming, or remapping any variable. Do not change ecommerce value mapping automatically from the export alone.

Automated-change policy: `manual_review_only`

Manual review required: `true`

Manual-review triggers:
- `broken_reference`
- `ecommerce_value_mapping`
- `variable_value_change`

Related change IDs: CHG-REC-003

Related QA item IDs: QA-002, QA-003

### F-ECOM-001 — GTM-ECOM-001 — high

Category: `ecommerce`
Affected entities: tag `102`, `GA4 - Event - Purchase`

Detected facts:
- Tag 102 is a GA4 event-style tag with eventName "purchase".
- The tag includes a value parameter set to "{{Missing Revenue}}".
- The referenced revenue variable is unresolved in the export.
- The export contains a transaction ID dataLayer variable, but no observed currency or items variable references on the purchase tag.

Inferred issue: Purchase revenue reporting may be incomplete or broken because the value parameter references a missing variable. Currency and item array mappings were not detected from the export.

Recommendation: Review ecommerce dataLayer documentation and validate a test purchase in GTM Preview. Confirm revenue, currency, transaction_id, and items mappings before making any payload change.

Automated-change policy: `manual_review_only`

Manual review required: `true`

Manual-review triggers:
- `purchase_event`
- `revenue_value`
- `ecommerce_payload_change`

Related QA item IDs: QA-003

### F-UNUSED-001 — GTM-UNUSED-001 — medium

Category: `unused_or_orphaned`
Affected entities: trigger `202`, `CE - purchase`, folder `402`, `GA4 - Ecommerce`, variable `302`, `DLV - ecommerce.transaction_id`

Detected facts:
- Trigger 202 is present but no tag references triggerId 202.
- Folder 402 is present but no exported entity uses parentFolderId 402.
- Variable 302 is present but no exported parameter references {{DLV - ecommerce.transaction_id}}.

Inferred issue: These entities appear orphaned from the exported relationships. They may be intended targets for the broken references, but that cannot be confirmed from ID/name mismatch alone.

Recommendation: Do not delete or archive automatically. Review whether these are the intended trigger, folder, and transaction ID variable for the purchase tag.

Automated-change policy: `blocked`

Manual review required: `true`

Manual-review triggers:
- `orphaned_entity`
- `possible_intended_reference_target`
- `deletion_blocked`

Related QA item IDs: QA-004
