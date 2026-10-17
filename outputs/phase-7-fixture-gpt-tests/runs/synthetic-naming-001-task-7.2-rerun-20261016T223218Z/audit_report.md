# GTM Container Audit & Patch Package — Audit Report

## 1. Executive summary
Source: `synthetic-naming-issues.json`; container: **Synthetic Naming Issues Container**; fixture: `synthetic-naming-001`.
Overall risk: **medium** (naming ambiguity and reference-sensitive review). **4 findings: 0 high, 3 medium, 1 low, 0 info.** One tag-only rename is included in `optimized_container.json`; three suggestions are not applied.
Human approval is required. All generated GTM artifacts are draft proposals for human review.

## 2. Container inventory
- Account ID: `9001`; container ID: `5101`; public ID: `GTM-SYN501`; export format version: `2`.
- 1 tag, 1 trigger, 1 user-defined variable, 1 folder, 1 built-in variable, 0 custom templates. No zone section supplied.
- Observed reference paths: tag `101` fires via trigger `201`, resolves `{{id}}` to variable `301`, and shares folder `401` with variable `301`.
- All three inspected reference targets are present in the export; live resolution is not verified.

## 3. Highest-risk findings
No high-severity findings were detected from this export. Three **medium** naming findings merit human review: `F-002` trigger `201` scope is inferred, `F-003` variable `301` is referenced as `{{id}}`, and `F-004` folder `401` grouping intent is uncertain.
Additional manual verification: tag `101` has GA4 `eventName=lead_submit` but fires via a `PAGEVIEW` trigger. This is directly observed, not evidence of correct or incorrect live firing; do not change triggering behavior as part of naming cleanup.

## 4. Proposed changes
- `C-001` / `F-001`: rename tag `101` from `tag 1` to `GA4 - Event - lead_submit`. Risk: **low**. Policy: `allowed_candidate`, name-only. Rationale: GA4 event tag type `gaawe` and explicit `eventName=lead_submit`. Human approval required. Rollback: restore original name `tag 1`; preserve ID and all configuration.

## 5. Changes applied in optimized JSON
- `C-001`: one name-only modification to tag `101` in the draft JSON. No trigger IDs, variable tokens, payloads, event names, parameters or folder references changed.
`optimized_container.json` is a proposed artifact, not a publish-ready guarantee.

## 6. Changes recommended but not applied
- `F-002` / `GTM-NAME-001` (`NAME-TRIGGER-001`): consider `PV - All Pages` only after a human verifies intended scope. Automated policy: `manual_review_only`.
- `F-003` / `GTM-NAME-001` (`NAME-VARIABLE-001`): consider `CONST - GA4 Measurement ID`. **Unsafe to rename without coordinated update to `{{id}}` references**. No variable edit applied. Automated policy: `manual_review_only`.
- `F-004` / `GTM-NAME-001` (`NAME-FOLDER-001`): consider `GA4 - Event Measurement` if analyst confirms grouping purpose. Automated policy: `manual_review_only`.
- No tag deletion, disabling, event modification, trigger logic change, consent modification, or variable value change proposed.

## 7. Validation results
See `validation_report.json` for package completeness, JSON parsing, structural references, and risk boundaries. Repository machine-readable JSON Schema definitions and validator executable were not provided; strict repository schema conformance is **not verified**.
Validation results do not prove tracking correctness, consent behavior, legal compliance, privacy compliance, or production readiness.

## 8. QA checklist
See `qa_checklist.md`: seven analyst items covering package review, tag rename, preview trigger scope, variable token integrity, folder purpose, lead flow firing, and rollback. Every QA item remains `todo`.

## 9. Human approval notes
Human review is required before import, workspace creation, publishing, or production use. An approved analyst must sign off on C-001 and determine whether to accept, defer or reject the three unapplied recommendations. No live platform was accessed.

## 10. Appendix: entity-level findings
### F-001 — GTM-NAME-001: vague tag name "tag 1"
- Severity: `low`; category: `naming`; policy: `allowed_candidate`; human review: `true`.
- Entity: `tag` `101` / `tag 1`.
- Detected fact: tagId=101; type=gaawe; eventName=lead_submit; measurementId={{id}}; firingTriggerId=201; parentFolderId=401.
- Inference: GA4 event tag name is supported by tag type and eventName.
- Recommendation: Rename tag 101 to GA4 - Event - lead_submit (included in draft).
- Related changes: `C-001`; QA: `QA-001`.

### F-002 — GTM-NAME-001: vague trigger name "all"
- Severity: `medium`; category: `naming`; policy: `manual_review_only`; human review: `true`.
- Entity: `trigger` `201` / `all`.
- Detected fact: triggerId=201; type=PAGEVIEW; no explicit filter or condition exported.
- Inference: All Pages scope is inferred, not proven by a live test.
- Recommendation: Confirm pageview scope before considering PV - All Pages; do not alter trigger conditions.
- Related changes: `none`; QA: `QA-002`.

### F-003 — GTM-NAME-001: vague variable name "id"
- Severity: `medium`; category: `naming`; policy: `manual_review_only`; human review: `true`.
- Entity: `variable` `301` / `id`.
- Detected fact: variableId=301; type=c; constant value=G-TEST501; tag 101 references {{id}} in measurementId.
- Inference: Constant appears to be a measurement ID; renaming without updating the variable token could break references.
- Recommendation: Review CONST - GA4 Measurement ID, then coordinate all reference rewrites if approved; no rename applied.
- Related changes: `none`; QA: `QA-003`.

### F-004 — GTM-NAME-001: vague folder name "misc"
- Severity: `medium`; category: `naming`; policy: `manual_review_only`; human review: `true`.
- Entity: `folder` `401` / `misc`.
- Detected fact: folderId=401; tag 101 and variable 301 have parentFolderId=401.
- Inference: Proposed grouping purpose follows current members; intended folder ownership is unknown.
- Recommendation: Confirm grouping intent before considering GA4 - Event Measurement; no rename applied.
- Related changes: `none`; QA: `QA-004`.

