# GTM Container Audit & Patch Package

## 1. Executive summary

Source fixture: `synthetic-unused-legacy-entities.json`
Fixture ID: `synthetic-unused-001`
Container: `Synthetic Unused Legacy Version` (`GTM-SYN504`)
Overall risk level: **medium**

The export contains orphaned legacy trigger, variable, and folder candidates matching expected rule `GTM-UNUSED-001`. No high-risk findings were detected from the export, but this does **not** mean the container is safe to publish.

Finding counts:

| Severity | Count |
| --- | ---: |
| High | 0 |
| Medium | 2 |
| Low | 1 |
| Info | 3 |

Human approval is required. No cleanup changes were applied to `optimized_container.json`; it preserves the source export because deletion, disabling, and archive decisions for unused or legacy entities are unsafe without analyst review.

This output is a draft proposal for human review.

## 2. Container inventory

Rule: `GTM-INV-001`

| Field | Value |
| --- | --- |
| Account ID | `9001` |
| Container ID | `5104` |
| Container name | `Synthetic Unused Legacy Version` |
| Public ID | `GTM-SYN504` |
| Export format version | `2` |
| Export time | `2026-06-09 00:00:00` |

Entity counts:

| Entity type | Count |
| --- | ---: |
| Tags | 1 |
| Triggers | 2 |
| Variables | 2 |
| Folders | 2 |
| Built-in variables | 1 |
| Custom templates | 0 |
| Zones | 0 |

Observed working references:

- Tag `105` (`GA4 - Event - sign_up`) fires on trigger `205` (`CE - sign_up`).
- Tag `105` references variable `{CONST - GA4 Measurement ID}`, which exists as variable `305`.
- Tag `105` is assigned to folder `405` (`GA4 - Core`).

## 3. Highest-risk findings

No high-risk findings were detected from this export.

Medium-risk findings requiring manual review:

### F-002 — Legacy trigger is not referenced by any exported tag

Rule ID: `GTM-UNUSED-001`
Severity: medium
Affected entity: trigger `204`, `legacy - do not delete`

Detected facts:

- Trigger `204` is a `CUSTOM_EVENT` trigger.
- No tag references trigger `204` in `firingTriggerId` or `blockingTriggerId`.
- The name contains `legacy` and `do not delete`.

Inferred issue: this appears to be an orphaned legacy trigger candidate, but warning language makes automated cleanup unsafe.

Recommended action: retain as-is until a human analyst confirms whether it is intentionally preserved.

Manual review required: yes.

### F-003 — Data layer variable is not referenced by exported tags, triggers, or variables

Rule ID: `GTM-UNUSED-001`
Severity: medium
Affected entity: variable `306`, `DLV - legacy_unused_value`

Detected facts:

- Variable `306` is a data layer variable (`type: v`).
- Its dataLayer key parameter is `legacy_unused_value`.
- No exported tag, trigger, or variable references `{DLV - legacy_unused_value}`.

Inferred issue: this appears to be an unused legacy variable candidate, but external references or planned usage cannot be ruled out from the export alone.

Recommended action: retain as-is until the analyst confirms the dataLayer contract.

Manual review required: yes.

## 4. Proposed changes

No changes were applied to the optimized JSON.

Recommended but not applied:

| Recommendation ID | Related finding | Entity | Recommendation | Risk | Reason not applied |
| --- | --- | --- | --- | --- | --- |
| REC-001 | F-002 | trigger `204` | Review retention of `legacy - do not delete` | Medium | Deletion/archive decisions are blocked and the name includes warning language. |
| REC-002 | F-003 | variable `306` | Review whether `legacy_unused_value` is still needed | Medium | Variable deletion or value/key changes are blocked without analyst approval. |
| REC-003 | F-004 | folder `404` | Review whether empty archive folder should be retained | Low | Folder cleanup is a manual-review decision. |

## 5. Changes applied in optimized JSON

`optimized_container.json` is unchanged from the source export.

Applied change count: `0`.

`optimized_container.json` is a proposed artifact, not a publish-ready guarantee.

## 6. Changes recommended but not applied

### Trigger `204` — `legacy - do not delete`

Not applied because `GTM-UNUSED-001` blocks automated deletion and the entity name contains explicit manual-review warning terms.

Suggested analyst next step: confirm whether this trigger is referenced in another workspace, planned implementation, external documentation, or client QA process.

### Variable `306` — `DLV - legacy_unused_value`

Not applied because the export cannot prove the dataLayer key is obsolete outside the visible container references.

Suggested analyst next step: review the dataLayer contract and any developer documentation before cleanup.

### Folder `404` — `Archive - Legacy Review`

Not applied because the folder appears intentionally named for archive or legacy review.

Suggested analyst next step: decide whether to keep it as a review placeholder or remove it in a reviewed cleanup.

## 7. Validation results

Validation status: `passed_with_warnings`.

Structural checks passed:

- Source JSON parsed successfully.
- GTM-like export structure is present.
- All seven required package artifacts were generated.
- `optimized_container.json` is parseable.
- Direct references from tag `105` resolve to existing trigger, variable, and folder entities.
- Unsafe cleanup was blocked.

Warnings:

- Unused/orphaned candidates were detected but not changed.
- Validation is file-based only.

Validation results do not prove tracking correctness, consent behavior, legal compliance, privacy compliance, or production readiness.

## 8. QA checklist

Highest-priority QA items:

- Confirm all seven artifacts are present.
- Review trigger `204`, variable `306`, and folder `404` before any cleanup decision.
- In a safe review context only, use GTM Preview to verify `sign_up` behavior for tag `105`, trigger `205`, and variable `305`.
- Capture review evidence and rejection/rollback decisions before import or use.

See `qa_checklist.md` for concrete manual QA steps.

## 9. Human approval notes

Human review is required before import, workspace creation, publishing, or production use.

This package did not connect to, inspect, change, import, publish, or verify any live GTM, GA4, Google Ads, API, workspace, website, or production platform.

The generated artifacts are draft proposals only.

## 10. Appendix: entity-level findings

### F-001 — Container inventory captured from source export

Rule ID: `GTM-INV-001`
Severity: info
Category: inventory
Affected entity: container `5104`, `Synthetic Unused Legacy Version`
Recommendation: use the inventory as the audit scope baseline.
Related QA items: `QA-001`

### F-002 — Legacy trigger is not referenced by any exported tag

Rule ID: `GTM-UNUSED-001`
Severity: medium
Category: unused or orphaned entities
Affected entity: trigger `204`, `legacy - do not delete`
Evidence: reference count from export is `0`; name contains `legacy` and `do not delete`.
Recommendation: retain until analyst review.
Automated-change policy: blocked.
Manual-review triggers: unused trigger, legacy warning, do-not-delete warning, deletion/archive decision.
Related QA items: `QA-002`

### F-003 — Data layer variable is not referenced by exported tags, triggers, or variables

Rule ID: `GTM-UNUSED-001`
Severity: medium
Category: unused or orphaned entities
Affected entity: variable `306`, `DLV - legacy_unused_value`
Evidence: reference count from export is `0`; dataLayer key is `legacy_unused_value`.
Recommendation: retain until analyst/developer review.
Automated-change policy: blocked.
Manual-review triggers: unused variable, legacy naming signal, possible external reference.
Related QA items: `QA-003`

### F-004 — Archive folder has no exported entity assignments

Rule ID: `GTM-UNUSED-001`
Severity: low
Category: unused or orphaned entities
Affected entity: folder `404`, `Archive - Legacy Review`
Evidence: assignment count from export is `0`; name indicates archive/legacy review.
Recommendation: retain until analyst review.
Automated-change policy: blocked.
Manual-review triggers: unused folder, archive/legacy review naming signal, deletion/archive decision.
Related QA items: `QA-004`

### F-005 — No unresolved direct references detected in exported configuration

Rule ID: `GTM-REF-001`
Severity: info
Category: reference integrity
Affected entities: tag `105`, trigger `205`, variable `305`, folder `405`
Evidence: tag `105` references existing trigger `205`, variable `305`, and folder `405`.
Recommendation: no reference repair proposed.
Related QA items: `QA-005`

### F-006 — Manual QA is required before using any generated artifact

Rule ID: `GTM-QA-001`
Severity: info
Category: QA
Affected entity: package `run_synthetic-unused-001_20260626T215120Z`
Evidence: file-in/file-out review only; no live platform verification.
Recommendation: complete manual QA and approval before import, workspace creation, publishing, or production use.
Related QA items: `QA-001`, `QA-002`, `QA-003`, `QA-004`, `QA-005`, `QA-006`
