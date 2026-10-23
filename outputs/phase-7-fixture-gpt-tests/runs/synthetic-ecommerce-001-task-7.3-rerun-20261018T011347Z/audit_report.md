# GTM Container Audit & Patch Package — synthetic-ecommerce-001-20261017

## 1. Executive summary

**Source:** `synthetic-ecommerce-missing-fields.json` (fixture `synthetic-ecommerce-001`). **Container:** Synthetic Ecommerce Missing Fields Container (`GTM-SYN505`). **Overall risk:** high. **Findings:** high 1, medium 0, low 0, info 0. Human approval is required.

**Detected:** GA4 purchase tag 105 explicitly maps `value` but not `transaction_id`, `currency`, or `items`. **Decision:** zero GTM configuration edits; optimized JSON remains a byte-for-byte copy of the source because ecommerce payload changes are blocked from automation. This output is a draft proposal for human review.

## 2. Container inventory

- Account ID: `9001`; container ID: `5105`; public ID: `GTM-SYN505`
- Export format version: `2`; exported version name: `Synthetic Ecommerce Missing Fields Version`
- Tags: 1; triggers: 1; variables: 2; folders: 1; custom templates: 0; built-in variables: 1; zones: not included.
- Tag `105` — `GA4 - Event - purchase`, type `gaawe`, folder `405` (`GA4 - Ecommerce`), firing trigger `205`.
- Trigger `205` — `CE - purchase`, type `CUSTOM_EVENT`; the export does not show an explicit custom event filter or event-name condition.
- Variable `305` — `CONST - GA4 Measurement ID`, value `G-TEST505`; variable `306` — `DLV - ecommerce.value`, dataLayer key `ecommerce.value`.
- Structural relationships for the tag's trigger, folder, and named variable tokens resolve in the export. This does not validate runtime firing or external templates.

## 3. Highest-risk findings

### F-ECOM-001 — GTM-ECOM-001 — High

**Affected:** tag `105` (`GA4 - Event - purchase`), trigger `205` (`CE - purchase`), variable `306` (`DLV - ecommerce.value`).

**Observed facts:** tag 105 lists `eventName=purchase`, `measurementId={{CONST - GA4 Measurement ID}}`, and `value={{DLV - ecommerce.value}}`; no `transaction_id`, `currency`, or `items` keys appear in the tag parameter array. The export contains no dataLayer variables explicitly named for those three ecommerce fields.

**Inference:** purchase measurement may omit critical order identity/currency/item information and may produce incomplete revenue reporting. Absence of mappings in this export does not prove the fields are absent in every runtime path.

**Recommendation:** document the actual purchase dataLayer contract, verify one complete test purchase, then have a human analyst review the required GTM/GA4 mapping and any implementation change. **Manual review:** required. **Automated-change policy:** `blocked` for ecommerce payload edits; manual-review-only for advice. **Related change:** none (intentionally withheld).

## 4. Proposed changes

No file-based GTM configuration changes are proposed. The underlying correction is a **manual recommendation**, not a `change_log.json` entry: define/verify exact source keys for `transaction_id`, `currency`, and `items`, then review mappings on tag 105. Risk: high. Rollback for any later human-managed implementation: restore original tag settings/approved container baseline after change-control review. Human approval required.

## 5. Changes applied in optimized JSON

No changes. `optimized_container.json` is a complete, byte-identical copy of the input export, including the wrapper and all tag/trigger/variable arrays. This prevents guessed mappings while supplying the required canonical artifact. `optimized_container.json` is a proposed artifact, not a publish-ready guarantee.

## 6. Changes recommended but not applied

- Map `transaction_id`, `currency`, and `items` only **after** the developer confirms actual dataLayer sources (GTM-ECOM-001). Not applied because ecommerce payload edits are blocked by the MLP policy and source keys are unknown.
- Confirm the custom-event trigger actually matches `purchase` in Preview; its name alone does not prove behavior (GTM-QA-001). Not applied because trigger logic is not to be inferred or changed automatically.
- Do not add default currencies, fabricated transaction identifiers, or new variables without a reviewed schema. No deletion, disabling, or consent edits are proposed.

## 7. Validation results

All seven artifacts were generated. Source and optimized GTM JSON parse and their core reference tokens resolve; source and optimized bytes match. Machine-readable artifact shape and cross-reference checks were performed locally against the exact field contract in `instructions.md`; repository JSON Schema files and a repository validator were **not provided**, so authoritative schema validation was not run. See `validation_report.json` for machine-readable checks and warnings.

Validation results do not prove tracking correctness, consent behavior, legal compliance, privacy compliance, or production readiness.

## 8. QA checklist

See `qa_checklist.md` (QA-001 to QA-006). Key tests: controlled GTM Preview on `purchase`, one firing only, verify transaction ID/currency/items/value against a test order, detect duplicate revenue, inspect consent states where applicable, and record screenshots/redacted traces. These tests **have not been executed**.

## 9. Human approval notes

Human review is required before import, workspace creation, publishing, or production use. Require GTM/analytics analyst and developer review of ecommerce field sources and runtime tests. Escalate to a privacy reviewer if sensitive data or client consent requirements are implicated. No live service was accessed or modified.

## 10. Appendix: entity-level findings

**F-ECOM-001 | GTM-ECOM-001 | high | ecommerce | tag 105, trigger 205, variable 306**

- **Evidence:** `containerVersion.tag[0].parameter` includes `eventName`, `measurementId`, `value` but not `transaction_id`, `currency`, `items`; `containerVersion.variable` contains DLV `ecommerce.value` and no variables named for transaction ID/currency/items; trigger ID `205` appears in tag 105 firingTriggerId.
- **Inferred issue:** incomplete GA4 purchase metadata / revenue reporting risk.
- **Recommended actions:** verify dataLayer keys and test purchase, review mapping with developer/analyst, test one firing and expected totals before any independently approved change.
- **Automated change policy:** `blocked` (payload mutation); manual-review-only recommendation.
- **Manual review trigger:** purchase/revenue fields with unknown source mappings.
- **Related change IDs:** none (no applied patch).
- **Related QA item IDs:** QA-002, QA-003, QA-004, QA-005, QA-006.
