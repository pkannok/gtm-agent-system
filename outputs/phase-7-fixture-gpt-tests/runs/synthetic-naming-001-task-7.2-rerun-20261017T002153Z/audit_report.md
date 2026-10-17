# GTM Container Audit & Patch Package — synthetic-naming-001-20261016

## 1. Executive summary
**Source:** `synthetic-naming-issues(3).json` · **Container:** Synthetic Naming Issues Container (`GTM-SYN501`) · **Overall risk:** medium (review ambiguity, not confirmed tracking failure).

Four findings: **0 high, 2 medium, 2 low, 0 info**. Two low-risk, name-only draft edits are reflected in `optimized_container.json`; two ambiguous recommendations are intentionally withheld. **Human approval is required.** All generated GTM artifacts are draft proposals requiring human review.

## 2. Container inventory
- Account ID: `9001`; container ID: `5101`; public ID: `GTM-SYN501`; export format version: `2`.
- Entities: 1 tag, 1 trigger, 1 user-defined variable, 1 folder, 1 built-in variable, 0 custom templates; no zone section supplied.
- Relationships observed: tag `101` fires on trigger `201`; tag parameter `measurementId` uses `{{id}}` (variable `301`); tag `101` and variable `301` belong to folder `401`.
- Reference scan: referenced trigger, variable token and folder IDs resolve within the export. Export-only checks cannot establish live tracking correctness.

## 3. Highest-risk findings
No **high-severity** finding was detected from the export. Two **medium** review uncertainties:
- **F-003 — GTM-NAME-001 / NAME-VARIABLE-001:** Variable `301` is `id` and holds a constant used by tag `101` via `{{id}}`. Renaming only its definition would break the name-based reference. **Manual review only; no patch.**
- **F-004 — GTM-NAME-001 / NAME-FOLDER-001:** Folder `401` is `misc`. A more descriptive group is inferred from two members, not established by an owner. **Manual review only; no patch.**
- Separate **QA observation**, not an asserted tracking defect: a tag with eventName `lead_submit` references an unfiltered `PAGEVIEW` trigger. Validate intended event semantics before trusting conversion reporting; no trigger logic changes authorized.

## 4. Proposed changes
| Change | Finding | Entity | Draft before → after | Risk | Policy / rollback |
| --- | --- | --- | --- | --- | --- |
| CH-001 | F-001 | tag `101` | `tag 1` → `GA4 - Event - lead_submit` | low | `allowed_candidate`; restore `tag 1` |
| CH-002 | F-002 | trigger `201` | `all` → `PV - All Pages` | low | `allowed_candidate`; restore `all` |

Both are **proposed file-based name-only edits**, not live changes. The replacement tag name is supported by tag type `gaawe` and eventName `lead_submit`; the trigger label assumes `PAGEVIEW` without exported conditions corresponds to All Pages. Human approval and GTM Preview verification remain required.

## 5. Changes applied in optimized JSON
`CH-001` and `CH-002` are reflected in the *draft proposal* `optimized_container.json`. Both are name-only and preserve GTM IDs, references, parameters, fingerprints, folders, and trigger conditions. `optimized_container.json` is a proposed artifact, not a publish-ready guarantee.

## 6. Changes recommended but not applied
- **F-003:** Candidate `CONST - GA4 Measurement ID` for variable `301`; withheld because tag token `{{id}}` would require a coordinated update and external references may exist. Rule `GTM-NAME-001`, agency `NAME-VARIABLE-001`; **manual_review_only**.
- **F-004:** Candidate `GA4 - Lead Measurement` for folder `401`; withheld because grouping purpose is inferred. Rule `GTM-NAME-001`, agency `NAME-FOLDER-001`; **manual_review_only**.
- No deletions, firing-rule changes, value edits, tag payload edits, or consent changes are proposed.

## 7. Validation results
See `validation_report.json` for deterministic checks. Package completeness, parseability, two-name diff scope, and internal ID/token integrity are checked. Warnings cover inferred trigger semantics, withheld variable/folder naming decisions, and unavailable live Preview evidence. **Validation results do not prove tracking correctness, consent behavior, legal compliance, privacy compliance, or production readiness.**

## 8. QA checklist
See `qa_checklist.md` (`QA-001` to `QA-008`). Primary scenarios: verify tag `101` firing and parameters, confirm trigger `201` scope, inspect variable `301` resolution, review folder meaning, evaluate lead event versus pageview expectations, and test rollback. All QA is `todo`.

## 9. Human approval notes
**Human review is required before import, workspace creation, publishing, or production use.** GTM analyst should approve/reject name proposals and confirm external text references; client measurement owner should confirm lead event firing intent. No GTM, GA4, Google Ads, website, API, workspace or production platform was accessed.

## 10. Appendix: entity-level findings

### F-001 — Vague tag name: tag 1
- **Rule:** `GTM-NAME-001`; agency subrule in description. **Severity:** low; **Category:** naming; **Entity:** tag `101` (`tag 1`).
- **Detected facts:** containerVersion.tag[tagId=101].name='tag 1'; type='gaawe'. tag 101 parameter eventName='lead_submit'; firingTriggerId=['201']. Tag 101 measurementId='{{id}}', which resolves by name to variable 301.
- **Inference:** [GTM-NAME-001; NAME-TAG-001] Name obscures platform, tag type, and event; the proposed GA4 event naming is supported by the exported tag type and eventName.
- **Recommended action:** Use 'GA4 - Event - lead_submit' as a draft name-only edit; preserve tag ID, payload and trigger.
- **Change IDs:** CH-001; **Human review:** required.

### F-002 — Vague trigger name: all
- **Rule:** `GTM-NAME-001`; agency subrule in description. **Severity:** low; **Category:** naming; **Entity:** trigger `201` (`all`).
- **Detected facts:** containerVersion.trigger[triggerId=201].name='all'; type='PAGEVIEW'. No filter or condition fields are present on trigger 201; tag 101 references firingTriggerId '201'.
- **Inference:** [GTM-NAME-001; NAME-TRIGGER-001] Name omits trigger type and apparent page scope; all-pages scope is inferred from exported configuration, not live behavior.
- **Recommended action:** Use 'PV - All Pages' as a draft name-only edit; confirm actual trigger scope in GTM Preview.
- **Change IDs:** CH-002; **Human review:** required.

### F-003 — Vague variable name: id
- **Rule:** `GTM-NAME-001`; agency subrule in description. **Severity:** medium; **Category:** naming; **Entity:** variable `301` (`id`).
- **Detected facts:** containerVersion.variable[variableId=301].name='id'; type='c'. Variable 301 has constant value 'G-TEST501'. Tag 101 parameter measurementId='{{id}}' refers to this variable by its name.
- **Inference:** [GTM-NAME-001; NAME-VARIABLE-001] The generic name hides its likely GA4 measurement-ID purpose. Renaming it alone would break the tag's name-based reference.
- **Recommended action:** Manually review a coordinated rename to 'CONST - GA4 Measurement ID' and corresponding tag token replacement, without modifying the constant value.
- **Change IDs:** none (not applied); **Human review:** required.

### F-004 — Vague folder name: misc
- **Rule:** `GTM-NAME-001`; agency subrule in description. **Severity:** medium; **Category:** naming; **Entity:** folder `401` (`misc`).
- **Detected facts:** containerVersion.folder[folderId=401].name='misc'. Tag 101 and variable 301 both have parentFolderId='401'; no other objects refer to this folder.
- **Inference:** [GTM-NAME-001; NAME-FOLDER-001] Folder has an ambiguous grouping purpose. 'GA4 - Lead Measurement' is only a candidate inferred from its contents.
- **Recommended action:** Confirm the business grouping before renaming; candidate 'GA4 - Lead Measurement' is not applied.
- **Change IDs:** none (not applied); **Human review:** required.

**Rule policy:** `GTM-NAME-001` allows low-risk, clearly evidenced name-only candidates; ambiguous, inferred or reference-sensitive renames remain manual-review-only. See `qa_checklist.md` QA-001–QA-008.
