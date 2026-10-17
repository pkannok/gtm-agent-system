# GTM Container Audit & Patch Package — synthetic-naming-001-20261016

## 1. Executive summary

**Source:** `synthetic-naming-issues(1).json`. **Container:** Synthetic Naming Issues Container (`9001` / `5101`). **Overall finding severity:** medium. **Findings:** 0 high, 4 medium, 1 low, 0 info. Human approval required. One name-only patch is included; three proposed names remain unapplied. This output is a draft proposal for human review.

## 2. Container inventory

Export version `2`, container public ID `GTM-SYN501`; 1 tag, 1 trigger, 1 user-defined variable, 1 folder, 0 custom templates, 1 built-in variable. No zones section provided. `tag 101` references trigger `201`, folder `401`, and variable token `{{id}}`, resolved to variable `301` in this fixture. No broken observed internal references.

## 3. Highest-risk findings

No high-severity findings were detected from the file. **F-005 / GTM-QA-001 (medium):** the GA4 `lead_submit` event tag (`101`) references the `PAGEVIEW` trigger (`201`), with no visible conditions. This may fire on ordinary page views rather than actual lead submissions. Manual Preview testing is required; no firing-logic changes have been applied. Other medium-severity findings are F-002, F-003 and F-004, each involving inferred naming or variable-token dependencies.

## 4. Proposed changes

**C-001 / F-001 / GTM-NAME-001:** Tag `101`, `tag 1` → `GA4 - Event - lead_submit`. Low-risk, `allowed_candidate`, name-only. The exported tag type `gaawe` and `eventName=lead_submit` support the replacement. **Rollback:** restore tag `101` name to `tag 1`. Human approval required.

## 5. Changes applied in optimized JSON

Only **C-001** is reflected in `optimized_container.json`; all IDs, references, parameters, variable values, trigger logic, folder membership and other fields are preserved. The patch is a proposal, not a live change. **`optimized_container.json` is a proposed artifact, not a publish-ready guarantee.**

## 6. Changes recommended but not applied

- **F-002 / GTM-NAME-001:** trigger `201`, `all` → `PV - All Pages` (tentative). Policy `manual_review_only`; verify that its no-filter `PAGEVIEW` configuration matches this scope.
- **F-003 / GTM-NAME-001:** variable `301`, `id` → `CONST - GA4 Measurement ID` (tentative). Policy `manual_review_only`; tag `101` uses literal `{{id}}`. Renaming the variable alone risks a broken reference; coordinated token changes require separate review.
- **F-004 / GTM-NAME-001:** folder `401`, `misc` → `GA4 - Measurement Components` (tentative). Policy `manual_review_only`; grouping intent is inferred from tag and variable membership.
- **F-005 / GTM-QA-001:** do not change lead conversion firing logic automatically. Confirm expected behavior in Preview.

No deletions, disables, consent edits, payload changes, or trigger edits are proposed.

## 7. Validation results

All seven output artifacts are represented. Machine-readable JSON parsed successfully and offline relationship/diff checks were performed. No repository JSON Schema files or deterministic repo validator were supplied, so full repository-schema conformance is **not verified**. See `validation_report.json`. **Validation results do not prove tracking correctness, consent behavior, legal compliance, privacy compliance, or production readiness.**

## 8. QA checklist

Review naming C-001 and external references; verify trigger scope; inspect variable token dependencies; confirm folder taxonomy; perform isolated GTM Preview of ordinary page views vs lead-submit flow; record redacted evidence and test rollback. All QA items remain `todo`. See `qa_checklist.md`.

## 9. Human approval notes

**Human review is required before import, workspace creation, publishing, or production use.** The assigned GTM analyst should approve or reject C-001 and independently review the three deferred names and the potential lead-event scope issue. No GTM, GA4, Ads, API, website or production connection was used.

## 10. Appendix: entity-level findings

### F-001 — GTM-NAME-001: Vague tag name

- Severity: `low`; category: `naming`; human review required: **yes**.
- Entity IDs: tag 101 (`tag 1`).
- Detected evidence: tag ID 101 has name "tag 1" in containerVersion.tag[0].name. Tag type gaawe and eventName lead_submit explicitly identify a GA4 event. Tag 101 type gaawe; eventName is lead_submit; firingTriggerId is ["201"].
- Interpretation/review: The tag name "tag 1" does not identify its intended role. Proposed label: "GA4 - Event - lead_submit". Rule GTM-NAME-001; supporting agency rule NAME-TAG-001.
- Recommendation: Review proposed name "GA4 - Event - lead_submit" and confirm it matches client terminology. Do not change GTM configuration, values, event names, or firing logic.
- Applied change: C-001.
- Related QA: QA-001, QA-006.

### F-002 — GTM-NAME-001: Vague trigger name

- Severity: `medium`; category: `naming`; human review required: **yes**.
- Entity IDs: trigger 201 (`all`).
- Detected evidence: trigger ID 201 has name "all" in containerVersion.trigger[0].name. PAGEVIEW type and absence of filters suggest all pages, but the intended scope is inferred.
- Interpretation/review: The trigger name "all" does not identify its intended role. Proposed label: "PV - All Pages". Rule GTM-NAME-001; supporting agency rule NAME-TRIGGER-001.
- Recommendation: Review proposed name "PV - All Pages" and confirm it matches client terminology. Do not change GTM configuration, values, event names, or firing logic.
- Applied change: none (manual review only).
- Related QA: QA-002.

### F-003 — GTM-NAME-001: Vague variable name

- Severity: `medium`; category: `naming`; human review required: **yes**.
- Entity IDs: variable 301 (`id`).
- Detected evidence: variable ID 301 has name "id" in containerVersion.variable[0].name. Constant variable holds G-TEST501 and is referenced by literal {{id}} in tag 101; token replacement would be required for a working rename. Tag 101 parameter measurementId contains "{{id}}"; variable ID 301 has type "c" and a constant value "G-TEST501".
- Interpretation/review: The variable name "id" does not identify its intended role. Proposed label: "CONST - GA4 Measurement ID". Rule GTM-NAME-001; supporting agency rule NAME-VARIABLE-001.
- Recommendation: Review proposed name "CONST - GA4 Measurement ID" and confirm it matches client terminology. Do not change GTM configuration, values, event names, or firing logic.
- Applied change: none (manual review only).
- Related QA: QA-003.

### F-004 — GTM-NAME-001: Vague folder name

- Severity: `medium`; category: `naming`; human review required: **yes**.
- Entity IDs: folder 401 (`misc`).
- Detected evidence: folder ID 401 has name "misc" in containerVersion.folder[0].name. Folder contains tag 101 and variable 301, but the intended grouping label is inferred. Tag 101 and variable 301 both use parentFolderId "401".
- Interpretation/review: The folder name "misc" does not identify its intended role. Proposed label: "GA4 - Measurement Components". Rule GTM-NAME-001; supporting agency rule NAME-FOLDER-001.
- Recommendation: Review proposed name "GA4 - Measurement Components" and confirm it matches client terminology. Do not change GTM configuration, values, event names, or firing logic.
- Applied change: none (manual review only).
- Related QA: QA-004.

### F-005 — GTM-QA-001: Lead event on broad page-view trigger requires verification

- Severity: `medium`; category: `qa`; human review required: **yes**.
- Entity IDs: tag 101 (`tag 1`), trigger 201 (`all`).
- Detected evidence: tag 101 eventName=lead_submit and firingTriggerId=["201"]. trigger 201 type=PAGEVIEW; no filter fields are present.
- Interpretation/review: Tag 101 is configured with eventName lead_submit and references trigger 201 of type PAGEVIEW with no visible conditions. This suggests a broad firing scope; export-only evidence does not establish intended behavior.
- Recommendation: Perform manual GTM Preview on an ordinary page view and genuine lead submission. Do not alter trigger conditions or tag payload automatically.
- Applied change: none (manual review only).
- Related QA: QA-005.

