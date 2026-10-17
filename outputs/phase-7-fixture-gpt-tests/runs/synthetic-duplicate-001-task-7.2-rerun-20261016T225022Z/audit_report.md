# GTM Container Audit & Patch Package — synthetic-duplicate-001

## 1. Executive summary
Source: `synthetic-duplicate-purchase-tags(1).json`. Container: **Synthetic Duplicate Purchase Container** (`GTM-SYN503`; account `9001`, container `5103`). **Overall risk: high.** Findings: **2 high, 0 medium, 0 low, 0 info**. **Human approval is required**. There are **0 proposed changes applied** to the optimized export because deleting/disabling duplicate ecommerce purchase tags is blocked for automation. All generated GTM artifacts are draft proposals for human review.

## 2. Container inventory
Export format version: `2`; export timestamp stated in fixture: `2026-06-09 00:00:00`. Tags: **2**; triggers: **1**; user-defined variables: **2**; folders: **1**; custom templates: **0**; built-in variables: **1**; zones: **not present** in supplied export. Both GA4 tags are in folder 403 `GA4 - Ecommerce`. Tag-to-trigger and variable name references exist in the export. Trigger 203's name is `CE - purchase`, but an explicit custom-event condition is not present in the serialized trigger; runtime matching is not independently proven. No live access or QA took place.

## 3. Highest-risk findings
### F-001 — GTM-DUP-001 (high): duplicate GA4 purchase candidates
**Observed:** Tag 103 `GA4 - Event - purchase` and tag 104 `GA4 - Event - purchase copy` are both type `gaawe`, fire on trigger 203 `CE - purchase`, send event `purchase`, use `{{CONST - GA4 Measurement ID}}` (variable 303, `G-TEST503`) and map `transaction_id` via `{{DLV - ecommerce.transaction_id}}` (variable 304). Their parameter sets are identical. **Inference:** They may send duplicate purchases and revenue if both fire. Intentional duplication cannot be ruled out by export alone. **Recommendation:** Inspect test-purchase Preview and request evidence; choose one implementation only after review. **Policy:** `manual_review_only` for duplicate cleanup; `blocked` for deletion/disabling. **Human review:** required. **Related applied change:** none.

### F-002 — GTM-ECOM-001 (high): purchase data completeness and revenue integrity
**Observed:** Both tags configure `transaction_id`; neither explicitly serializes parameters for `value`, `currency`, or `items`. **Inference:** Missing or inherited ecommerce fields may affect reporting; simultaneous purchase tags may lead to duplicate revenue. This is not proof that fields are absent from runtime GA4 hits. **Recommendation:** Verify parameters and deduplication in a test order via GTM Preview, dataLayer, and DebugView. **Policy:** `manual_review_only` for recommendations; `blocked` for payload edits. **Human review:** required. **Related applied change:** none.

## 4. Proposed changes
No file-based changes were proposed for application. Remediation candidate **R-001 (not applied; not a change_log entry)**: after analyst confirms duplicate firing and client measurement intent, retain the canonical tag and separately approve disabling/removing the redundant tag. Affected: tags 103/104, trigger 203. **Risk:** high. **Policy:** blocked for automated disabling/deletion under `GTM-DUP-001`; requires human approval. **Rollback concept:** restore both original tag objects from `synthetic-duplicate-purchase-tags(1).json` and re-run test purchase QA.

## 5. Changes applied in optimized JSON
None. `optimized_container.json` preserves the complete source GTM export unchanged, including wrapper, tags, trigger, variables, folder, built-in variable and template list. This is intentional and consistent with `change_log.json` having zero changes.

**`optimized_container.json` is a proposed artifact, not a publish-ready guarantee.**

## 6. Changes recommended but not applied
- **R-001 / F-001 / GTM-DUP-001:** Investigate and, only if approved, disable/remove one duplicate tag. Not applied: prohibited destructive/behavioral automation and uncertain client intent. Analyst should document canonical tag and rollback approach.
- **R-002 / F-002 / GTM-ECOM-001:** Confirm `value`, `currency`, `items`, transaction uniqueness and dataLayer mapping in runtime. Not applied: ecommerce payload changes are blocked; exported parameter absence does not prove runtime absence.
- **R-003 / F-001 / GTM-QA-001:** Verify event condition and consent state manually before any action. Not applied: no change justified by export evidence.

## 7. Validation results
All seven artifacts are generated. Source and optimized JSON parse and are equal. Visible trigger ID, folder ID, and tag variable token references resolve inside the supplied export. Warnings: two high-risk purchase findings still require remediation/QA; repository JSON Schema and deterministic validator files are unavailable, so **strict schema validation is not claimed**. See `validation_report.json`.

**Validation results do not prove tracking correctness, consent behavior, legal compliance, privacy compliance, or production readiness.**

## 8. QA checklist
See `qa_checklist.md`, especially QA-002 (single `purchase` event: determine whether tags 103 and 104 both fire), QA-003 (transaction ID, value, currency, items, and repeat-purchase handling), QA-004 (consent state where applicable), and QA-005 (future approval/rejection and rollback). All statuses `todo`; no GTM Preview or other platform was accessed.

## 9. Human approval notes
A GTM/analytics analyst must evaluate duplicate tracking and test ecommerce events; a developer may need to inspect dataLayer implementation. Consent/privacy reviewer input is required if client policy or observed configuration makes it relevant. **Human review is required before import, workspace creation, publishing, or production use.** No live GTM, GA4, Ads, workspace, API, or website was accessed or modified.

## 10. Appendix: entity-level findings
| Finding | Rule | Severity | Category | GTM entities | Evidence location | Recommendation | Automation policy | QA |
|---|---|---|---|---|---|---|---|---|
| F-001 | GTM-DUP-001 | high | duplicates | tag 103, tag 104, trigger 203, variables 303/304 | `containerVersion.tag[0]`, `tag[1]`, `trigger[0]`, `variable[0:2]` | Investigate double firing; manual canonical-tag decision | manual_review_only; deleting/disabling blocked | QA-002, QA-004, QA-005 |
| F-002 | GTM-ECOM-001 | high | ecommerce | tag 103, tag 104, trigger 203, variable 304 | `containerVersion.tag[0:2].parameter`, `variable[1]` | Check transaction, revenue and item data and repeat sends | manual_review_only; payload edits blocked | QA-003 |

**Assumptions:** Tags sharing one trigger and payload are duplicate candidates, not proven duplicate network hits. No client profile was supplied. The fixture is synthetic. The JSON Schema files were not available for exact contract enforcement.
