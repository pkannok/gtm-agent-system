# GTM Container Audit & Patch Package — Audit Report

## 1. Executive summary
- **Fixture:** `synthetic-naming-001`; source file `synthetic-naming-issues(2).json`.
- **Container:** Synthetic Naming Issues Container (`GTM-SYN501`).
- **Overall review risk:** medium (ambiguity and linked-name dependency, not evidence of live tracking failure).
- **Findings:** 0 high, 2 medium, 2 low, 0 info.
- **Patch:** 2 proposed name-only edits included; 2 candidates withheld for manual review.
- **Approval:** Required before import, workspace creation, publishing, or production use.
- **Boundary:** All generated GTM artifacts are draft proposals for human review.

## 2. Container inventory
- Account ID `9001`; container ID `5101`; export format version `2`.
- Version name: Synthetic Naming Issues Version.
- Tags: 1; triggers: 1; user-defined variables: 1; folders: 1; built-in variables: 1; custom templates: 0.
- No `zone` section appears. No client profile or override was provided.
- References observed: tag 101 fires on trigger 201; tag 101 `measurementId` references `{{id}}`, the current name of variable 301; tag 101 and variable 301 are in folder 401.
- This is file-based inventory only. No live configuration or behavior was examined.

## 3. Highest-risk findings
No **high-severity** findings were detected from this fixture export. Medium-severity findings are:
- **F-003 (`GTM-NAME-001`):** Variable `301` is named `id`, and tag 101 references `{{id}}`. A name-only update without coordinated reference handling could break the link; withhold automation.
- **F-004 (`GTM-NAME-001`):** Folder `401` is named `misc`. The proposed `GA4 - Measurement` name is inferred from membership and must be confirmed.
Neither finding proves any live issue.

## 4. Proposed changes
- **C-001 / F-001:** Rename tag 101 `tag 1` → `GA4 - Event - lead_submit`. Evidence: type `gaawe`, eventName `lead_submit`; low risk, `allowed_candidate`. Rollback: restore `tag 1`. Human approval required.
- **C-002 / F-002:** Rename trigger 201 `all` → `PV - All Pages`. Evidence: type `PAGEVIEW`, no filter fields in this export; low risk, `allowed_candidate`. Assumption: this represents all-pages scope; verify manually. Rollback: restore `all`. Human approval required.

These are proposed file edits, not live GTM mutations.

## 5. Changes applied in optimized JSON
- `C-001`: **name-only**, tag display name.
- `C-002`: **name-only**, trigger display name.
- All IDs, tag parameters, trigger settings, variable values/references, folder assignments and other source fields are preserved.
- Both candidate edits remain subject to external dependency checks and GTM Preview comparison.

**`optimized_container.json` is a proposed artifact, not a publish-ready guarantee.**

## 6. Changes recommended but not applied
- **F-003 (`GTM-NAME-001`, `NAME-VARIABLE-001`):** Potential rename `id` → `CONST - GA4 Measurement ID`. **Not applied**: the literal `{{id}}` occurs in tag 101's measurementId parameter. Human analyst must decide whether a coordinated reference change is warranted. Merely renaming the object is unsafe.
- **F-004 (`GTM-NAME-001`, `NAME-FOLDER-001`):** Potential rename `misc` → `GA4 - Measurement`. **Not applied**: folder intent is inferred. Confirm grouping purpose with owner before any change.
- Do not alter the `lead_submit` event value, measurementId constant, or PAGEVIEW trigger logic as a naming repair.

## 7. Validation results
- Seven canonical files generated; four JSON package files plus `optimized_container.json` subject to parsing and structural checks in `validation_report.json`.
- Proposed output retains full `exportFormatVersion` and `containerVersion` wrapper and all existing arrays.
- Warnings: two naming proposals were intentionally withheld; external name-based dependencies cannot be verified from export; PAGEVIEW scope needs human confirmation.
- **Validation results do not prove tracking correctness, consent behavior, legal compliance, privacy compliance, or production readiness.**

## 8. QA checklist
See `qa_checklist.md`. Priorities: inspect both name-only diffs, verify `{{id}}` still resolves without altering the original variable, compare trigger 201 evaluation and tag 101 firing on representative page/lead flows, record screenshots and redacted logs, and rehearse rollback. All live/Preview steps are pending human execution.

## 9. Human approval notes
**Human review is required before import, workspace creation, publishing, or production use.** A GTM analyst should validate proposed names and any outside-GTM dependencies, confirm inferred trigger/folder scope, and obtain appropriate change approval. No external platforms or APIs were accessed.

## 10. Appendix: entity-level findings

### F-001 — `tag` 101: `tag 1`
- **Rule:** `GTM-NAME-001` / `NAME-TAG-001`; **severity:** `low`; **category:** naming.
- **Detected facts:** containerVersion.tag[0].type = gaawe; containerVersion.tag[0].parameter[eventName] = lead_submit; containerVersion.tag[0].firingTriggerId[0] = 201.
- **Inference:** The tag name does not identify its GA4 event purpose.
- **Proposed name:** `GA4 - Event - lead_submit` (display name only as a candidate).
- **Recommendation:** Propose name-only rename to GA4 - Event - lead_submit
- **Policy:** `allowed_candidate`; **manual review:** yes.
- **Triggers for review:** Confirm no external name-based dependencies and test before import.
- **Related change IDs:** C-001; **QA:** QA-001.

### F-002 — `trigger` 201: `all`
- **Rule:** `GTM-NAME-001` / `NAME-TRIGGER-001`; **severity:** `low`; **category:** naming.
- **Detected facts:** containerVersion.trigger[0].type = PAGEVIEW; containerVersion.trigger[0] has no filter fields; containerVersion.tag[0].firingTriggerId includes 201.
- **Inference:** The trigger name omits its page-view type and intended scope.
- **Proposed name:** `PV - All Pages` (display name only as a candidate).
- **Recommendation:** Propose name-only rename to PV - All Pages
- **Policy:** `allowed_candidate`; **manual review:** yes.
- **Triggers for review:** Confirm no external name-based dependencies and test before import.
- **Related change IDs:** C-002; **QA:** QA-002.

### F-003 — `variable` 301: `id`
- **Rule:** `GTM-NAME-001` / `NAME-VARIABLE-001`; **severity:** `medium`; **category:** naming.
- **Detected facts:** containerVersion.variable[0].type = c; containerVersion.variable[0].parameter[value] = G-TEST501; containerVersion.tag[0].parameter[measurementId] = {{id}}.
- **Inference:** The constant variable has a vague name; its current name is referenced textually by the tag.
- **Proposed name:** `CONST - GA4 Measurement ID` (display name only as a candidate).
- **Recommendation:** Consider CONST - GA4 Measurement ID only after analyst verification.
- **Policy:** `manual_review_only`; **manual review:** yes.
- **Triggers for review:** Textual {{id}} reference must be preserved or explicitly reviewed before variable rename.
- **Related change IDs:** none — withheld; **QA:** QA-003.

### F-004 — `folder` 401: `misc`
- **Rule:** `GTM-NAME-001` / `NAME-FOLDER-001`; **severity:** `medium`; **category:** naming.
- **Detected facts:** containerVersion.folder[0].name = misc; containerVersion.tag[0].parentFolderId = 401; containerVersion.variable[0].parentFolderId = 401.
- **Inference:** The folder name does not explain the grouping; a GA4 measurement purpose is plausible but inferred.
- **Proposed name:** `GA4 - Measurement` (display name only as a candidate).
- **Recommendation:** Consider GA4 - Measurement only after analyst verification.
- **Policy:** `manual_review_only`; **manual review:** yes.
- **Triggers for review:** Folder grouping purpose is inferred; confirm with owner.
- **Related change IDs:** none — withheld; **QA:** QA-004.
