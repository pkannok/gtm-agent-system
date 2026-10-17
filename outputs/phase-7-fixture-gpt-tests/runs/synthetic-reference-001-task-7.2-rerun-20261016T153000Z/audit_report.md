# GTM Container Audit & Patch Package — synthetic-reference-001-20261016

## 1. Executive summary

- **Fixture:** `synthetic-reference-001`
- **Source file:** `synthetic-broken-references(2).json`
- **Container:** `Synthetic Broken References Container` (`GTM-SYN502`; account `9001`, container `5102`)
- **Overall risk:** high.
- **Finding counts:** high 2; medium 1; low 0; info 0.
- **Primary rule:** `GTM-REF-001` (Reference Integrity).
- **Changes included in optimized JSON:** zero; the optimized JSON retains the complete original export byte-equivalent in parsed JSON content.
- **Human approval:** required.

This output is a **draft proposal for human review**. No import, GTM workspace creation, publication, production change, or live verification occurred.

## 2. Container inventory

| Entity type | Count |
| --- | ---: |
| Tags | 1 |
| Triggers | 1 |
| User-defined variables | 1 |
| Folders | 1 |
| Built-in variables | 1 |
| Custom templates | 0 |

Export format version: `2`. Exported version name: `Synthetic Broken References Version`. The only tag is `102 — GA4 - Event - Purchase`; available trigger `202 — CE - purchase`, user-defined variable `302 — DLV - ecommerce.transaction_id`, and folder `402 — GA4 - Ecommerce`. The export does not include sufficient context to establish a revenue mapping or actual purchase trigger logic.

## 3. Highest-risk findings

- **F-REF-001 / GTM-REF-001 / high:** Tag `102` lists nonexistent firing trigger ID `299` at `containerVersion.tag[0].firingTriggerId[0]`. Trigger `202` exists but is **not** established as the intended substitute. Inference: purchase tracking may not fire as intended. Human review required.
- **F-REF-003 / GTM-REF-001 / high:** Tag `102` uses `{{Missing Revenue}}` as its `value` parameter at `containerVersion.tag[0].parameter[1].value`. No exported variable has that name. Inference: reported purchase value may be missing or wrong. Human review required.
- **F-REF-002 / GTM-REF-001 / medium:** Tag `102` lists nonexistent parent folder ID `499` at `containerVersion.tag[0].parentFolderId`. Folder `402` exists but cannot be assumed the intended folder. Folder organization may be inconsistent. Human review required.

These are observations about the exported configuration, not proof of live measurement failures.

## 4. Proposed changes

No change is approved for file-based application. Reference repairs under `GTM-REF-001` are `manual_review_only`, so no change IDs were allocated. See `audit_report.json` for `F-REF-001`, `F-REF-002`, and `F-REF-003` and `change_log.json` for the empty applied-change set. Candidate trigger `202` and folder `402` are *review hypotheses*, not assigned replacements. Revenue requires a verified dataLayer mapping; the existing transaction ID variable is not a revenue variable.

## 5. Changes applied in optimized JSON

None. `optimized_container.json` preserves the complete supplied export, with its wrapper, tags, triggers, variables, folders, and all related fields intact. No entities were removed, disabled, renamed, or rewired. **`optimized_container.json` is a proposed artifact, not a publish-ready guarantee.** Since broken references remain, it must not be treated as a repaired import candidate.

## 6. Changes recommended but not applied

1. **F-REF-001:** Confirm intended purchase event trigger and its conditions; only then manually propose replacing ID `299`. Not applied because tag firing semantics are unverified and purchase tracking is sensitive to trigger logic.
2. **F-REF-002:** Confirm expected folder placement; only then consider mapping `499` to `402`. Not applied because folder intent is not proven by name.
3. **F-REF-003:** Confirm the purchase value key, currency, transaction ID and items with implementation stakeholders; then define or select a verified value variable. Not applied because the source provides no revenue dataLayer key and ecommerce payload edits are blocked for automation (`GTM-ECOM-001`).

No consent-sensitive or advertising behavior was inferred from the fixture alone. Consent correctness remains unverified.

## 7. Validation results

- Seven artifacts produced and JSON parse checks performed.
- Full GTM export wrapper and core arrays retained.
- Three unresolved references remain **by design** under manual-review-only policy.
- No package schema files or deterministic repository validator were available, so strict schema conformance was **not verified**.
- Details are in `validation_report.json`.

**Validation results do not prove tracking correctness, consent behavior, legal compliance, privacy compliance, or production readiness.**

## 8. QA checklist

See `qa_checklist.md` for package inspection, human confirmation of trigger/folder targets, purchase Preview testing, revenue and dataLayer checks, duplicate purchase checking, evidence capture, and rejection/rollback. All human QA steps remain pending.

## 9. Human approval notes

**Human review is required before import, workspace creation, publishing, or production use.** The reviewing GTM analyst should establish intended targets; a developer or ecommerce owner should confirm dataLayer mappings; the analyst and business measurement owner should approve any eventual patch. No live systems were inspected or changed.

## 10. Appendix: entity-level findings

| Finding | Rule | Severity | Affected entity | Evidence | Policy | QA |
| --- | --- | --- | --- | --- | --- | --- |
| F-REF-001 | GTM-REF-001 | high | tag 102, GA4 - Event - Purchase | trigger ID `299` absent; `202` merely plausible | manual_review_only | QA-002, QA-003 |
| F-REF-002 | GTM-REF-001 | medium | tag 102, GA4 - Event - Purchase | folder ID `499` absent; `402` merely plausible | manual_review_only | QA-002 |
| F-REF-003 | GTM-REF-001 | high | tag 102, GA4 - Event - Purchase | token `{{Missing Revenue}}` unresolved | manual_review_only | QA-003, QA-004 |

All three findings require manual review; there are no related change IDs because no patch was applied. Evidence paths, detected facts, inferred impacts, and recommendations are detailed in `audit_report.json`.
