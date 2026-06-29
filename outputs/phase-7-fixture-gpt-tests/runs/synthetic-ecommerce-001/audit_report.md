# GTM Container Audit & Patch Package

## 1. Executive summary

Source fixture: `synthetic-ecommerce-missing-fields.json`
Fixture ID: `synthetic-ecommerce-001`
Container: `Synthetic Ecommerce Missing Fields Container` (`GTM-SYN505`)
Overall risk level: **high**

Finding counts:

| Severity | Count |
| --- | ---: |
| High | 1 |
| Medium | 0 |
| Low | 0 |
| Info | 1 |

The highest-risk finding is that the GA4 purchase event tag lacks clear `transaction_id` and `currency` mappings. This is reported under rule `GTM-ECOM-001`.

No ecommerce payload changes were applied in `optimized_container.json`. The optimized artifact intentionally preserves the source export because transaction ID, currency, value, and dataLayer-key changes are unsafe to infer from the export alone.

This output is a draft proposal for human review. Human approval is required before import, workspace creation, publishing, or production use.

## 2. Container inventory

| Field | Observed value |
| --- | --- |
| Account ID | `9001` |
| Container ID | `5105` |
| Public ID | `GTM-SYN505` |
| Container name | `Synthetic Ecommerce Missing Fields Container` |
| Container version name | `Synthetic Ecommerce Missing Fields Version` |
| Export format version | `2` |
| Export time | `2026-06-09 00:00:00` |

Entity counts:

| Entity type | Count |
| --- | ---: |
| Tags | 1 |
| Triggers | 1 |
| Variables | 2 |
| Folders | 1 |
| Built-in variables | 1 |
| Custom templates | 0 |
| Zones | 0 |

Inventory note (`F-002`, `GTM-INV-001`): the export contains enough GTM-like structure for this file-based audit. This inventory does not verify live tag firing.

## 3. Highest-risk findings

### F-001 — GA4 purchase event lacks clear transaction ID and currency mappings

- Rule ID: `GTM-ECOM-001`
- Severity: **high**
- Category: ecommerce
- Affected entities:
  - Tag `105`, `GA4 - Event - purchase`
  - Trigger `205`, `CE - purchase`
  - Variable `306`, `DLV - ecommerce.value`
  - Folder `405`, `GA4 - Ecommerce`

Detected facts:

- Tag `105` is named `GA4 - Event - purchase` and has type `gaawe`.
- Tag `105` sets `eventName` to `purchase`.
- Tag `105` maps `value` to `{DLV - ecommerce.value}`.
- Variable `306` maps to the dataLayer key `ecommerce.value`.
- No explicit `transaction_id` parameter mapping was observed on tag `105`.
- No explicit `currency` parameter mapping was observed on tag `105`.
- No variables named or keyed for `ecommerce.transaction_id`, `transaction_id`, `ecommerce.currency`, or `currency` were observed.
- Tag `105` fires on trigger ID `205`, named `CE - purchase`.

Inferred issue:

The purchase tag appears to send value without a clear transaction ID or currency mapping. This may create revenue reporting ambiguity, missing currency context, and weaker deduplication or transaction reconciliation for ecommerce reporting.

Recommended action:

A human analyst should confirm the intended dataLayer contract and, if correct, add explicit GA4 purchase mappings for transaction ID and currency using approved dataLayer keys. Manual verification is required. The MLP must not infer or apply these ecommerce payload changes automatically.

Related proposed change IDs: `CHG-001`, `CHG-002`, `CHG-003`.

## 4. Proposed changes

### CHG-001 — Add transaction ID mapping after human review

- Related finding: `F-001`
- Affected entity: tag `105`, `GA4 - Event - purchase`
- What would change: add an explicit GA4 purchase event parameter mapping for `transaction_id` after confirming the approved dataLayer key.
- Why proposed: a purchase event without a clear transaction ID can weaken deduplication and transaction reconciliation.
- Risk level: high
- Automated-change policy: blocked
- Applied in optimized JSON: no
- Rollback note: reject this recommendation by leaving tag `105` unchanged.
- Human approval required: yes

### CHG-002 — Add currency mapping after human review

- Related finding: `F-001`
- Affected entity: tag `105`, `GA4 - Event - purchase`
- What would change: add an explicit GA4 purchase event parameter mapping for `currency` after confirming the approved dataLayer key.
- Why proposed: the purchase tag maps value but does not show currency, which can create reporting ambiguity.
- Risk level: high
- Automated-change policy: blocked
- Applied in optimized JSON: no
- Rollback note: reject this recommendation by leaving tag `105` unchanged.
- Human approval required: yes

### CHG-003 — Create transaction ID and currency dataLayer variables after human review

- Related finding: `F-001`
- Affected entities: proposed variables `DLV - ecommerce.transaction_id` and `DLV - ecommerce.currency`
- What would change: create dataLayer variables only after confirming that those are the approved client dataLayer keys.
- Why proposed: no transaction ID or currency variables were observed in the export.
- Risk level: high
- Automated-change policy: blocked
- Applied in optimized JSON: no
- Rollback note: reject this recommendation by not creating new variables.
- Human approval required: yes

## 5. Changes applied in optimized JSON

No changes were applied in `optimized_container.json`.

`optimized_container.json` is a proposed artifact, not a publish-ready guarantee. In this package it preserves the original uploaded export so that unsafe ecommerce payload changes are not inferred or applied automatically.

## 6. Changes recommended but not applied

The following recommendations were not applied because they would change ecommerce purchase behavior and require manual review under `GTM-ECOM-001`:

| Recommendation | Reason not applied | Suggested analyst next step |
| --- | --- | --- |
| Add `transaction_id` to tag `105` | Transaction ID mapping affects purchase/revenue tracking and cannot be inferred safely. | Confirm the dataLayer contract with analytics/development stakeholders. |
| Add `currency` to tag `105` | Currency/value mapping affects revenue reporting and must match the implementation. | Confirm the currency source and expected ISO currency format. |
| Create `DLV - ecommerce.transaction_id` and `DLV - ecommerce.currency` variables | Creating variables would encode unconfirmed dataLayer keys. | Add only after human approval and GTM Preview validation. |

Unsafe changes flagged:

- Automatically changing ecommerce payloads.
- Automatically creating dataLayer variables for transaction ID or currency.
- Changing event names, trigger logic, values, dataLayer keys, or conversion behavior.
- Treating validation as proof that ecommerce tracking works.

## 7. Validation results

Validation status: **passed with warnings**

Passed checks:

- Source fixture parsed as JSON.
- GTM-like top-level structure is present.
- GA4 purchase tag `105` and trigger `205` are present.
- Tag `105` references trigger `205`, which exists.
- Tag `105` references variables `CONST - GA4 Measurement ID` and `DLV - ecommerce.value`, which exist.
- `optimized_container.json` is valid JSON and intentionally preserves the source ecommerce payload.

Warnings:

- No explicit purchase `transaction_id` parameter or dataLayer variable was observed.
- No explicit purchase `currency` parameter or dataLayer variable was observed.
- Human review is required before adding transaction ID or currency mappings.

Validation results do not prove tracking correctness, consent behavior, legal compliance, privacy compliance, or production readiness.

## 8. QA checklist

Highest-priority manual QA items:

- Confirm the seven required artifacts are present.
- Review tag `105` in a safe GTM review context.
- Run a purchase test in GTM Preview and inspect the `purchase` event.
- Confirm whether `transaction_id`, `currency`, `value`, and item data appear in the dataLayer.
- Verify that adding transaction ID or currency mappings would not duplicate or override existing revenue data.
- Capture Preview logs, screenshots, and the dataLayer payload with sensitive values redacted.
- Obtain analyst approval before import, workspace creation, publishing, or production use.

## 9. Human approval notes

Human review is required before import, workspace creation, publishing, or production use.

Recommended reviewers:

- Technical marketing analyst for GTM configuration review.
- Analytics owner for GA4 purchase parameter expectations.
- Developer or dataLayer owner for transaction ID and currency key confirmation.
- Client stakeholder when revenue reporting definitions or currency behavior are business-specific.

No live GTM, GA4, Google Ads, website, API, workspace, or production platform was connected to, inspected, changed, imported, published, or verified.

## 10. Appendix: entity-level findings

### F-001

- Rule ID: `GTM-ECOM-001`
- Severity: high
- Category: ecommerce
- Affected entity type: tag
- Affected entity ID: `105`
- Affected entity name: `GA4 - Event - purchase`
- Evidence:
  - `parameter[eventName]`: `purchase`
  - `parameter[value]`: `{DLV - ecommerce.value}`
  - `parameter[transaction_id]`: not present
  - `parameter[currency]`: not present
  - Related trigger: `205`, `CE - purchase`
  - Related variable: `306`, `DLV - ecommerce.value`, dataLayer key `ecommerce.value`
- Recommendation: manually confirm and add transaction ID and currency mappings only after dataLayer contract review.
- Automated-change policy: blocked
- Manual-review triggers: purchase/revenue tracking, transaction IDs, currency/value parameters, ecommerce payload changes.
- Related change IDs: `CHG-001`, `CHG-002`, `CHG-003`
- Related QA item IDs: `QA-ECOM-001`, `QA-ECOM-002`

### F-002

- Rule ID: `GTM-INV-001`
- Severity: info
- Category: inventory
- Affected entity type: container
- Affected entity ID: `5105`
- Affected entity name: `Synthetic Ecommerce Missing Fields Container`
- Evidence:
  - Export format version: `2`
  - Public ID: `GTM-SYN505`
  - Entity counts: 1 tag, 1 trigger, 2 variables, 1 folder, 1 built-in variable, 0 custom templates.
- Recommendation: use this as the audit coverage baseline.
- Automated-change policy: blocked
- Manual-review triggers: none for the inventory note.
