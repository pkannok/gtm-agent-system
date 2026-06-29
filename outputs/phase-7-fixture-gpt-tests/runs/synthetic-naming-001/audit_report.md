# GTM Container Audit & Patch Package

## 1. Executive summary

Source file: `synthetic-naming-issues.json`
Fixture ID: `synthetic-naming-001`
Container: `Synthetic Naming Issues Container` (`GTM-SYN501`)
Overall risk level: **Low**
Finding counts: **0 high**, **0 medium**, **4 low**, **1 info**.

The expected issue category was confirmed from the export: vague tag, trigger, variable, and folder names. The applicable audit rule is `GTM-NAME-001`.

Proposed changes were included in `optimized_container.json`. They are draft, file-based proposals for human review. Human approval is required before import, workspace creation, publishing, or production use.

## 2. Container inventory

| Field | Observed value |
| --- | --- |
| Account ID | `9001` |
| Container ID | `5101` |
| Container name | `Synthetic Naming Issues Container` |
| Public ID | `GTM-SYN501` |
| Export format version | `2` |
| Export time | `2026-06-09 00:00:00` |

| Entity type | Count |
| --- | ---: |
| Tags | 1 |
| Triggers | 1 |
| Variables | 1 |
| Folders | 1 |
| Built-in variables | 1 |
| Custom templates | 0 |
| Zones | 0 |

Inventory note: source structure was sufficient for this file-based audit. No malformed top-level GTM sections were detected from the fixture.

## 3. Highest-risk findings

No high-risk findings were detected from the exported fixture. This does not mean the container is safe to publish or that live tracking works.

## 4. Proposed changes

| Change ID | Related finding | Affected entity | Proposed change | Risk | Policy |
| --- | --- | --- | --- | --- | --- |
| `CHG-NAME-001` | `F-NAME-001` | Tag `101`, `tag 1` | Rename to `GA4 - Event - lead_submit` | Low | `allowed_candidate` |
| `CHG-NAME-002` | `F-NAME-002` | Trigger `201`, `all` | Rename to `PV - All Pages` | Low | `allowed_candidate` |
| `CHG-NAME-003` | `F-NAME-003` | Variable `301`, `id` | Rename to `CONST - GA4 Measurement ID` | Low | `allowed_candidate` |
| `CHG-NAME-004` | `F-NAME-004` | Folder `401`, `misc` | Rename to `GA4 - Core Measurement` | Low | `allowed_candidate` |
| `CHG-REF-001` | `F-NAME-003` | Tag `101` measurement ID token | Update `{{id}}` to `{{CONST - GA4 Measurement ID}}` to preserve the renamed variable reference | Low | `allowed_candidate` |

These changes are proposed file-based edits only. They do not represent a live GTM mutation.

## 5. Changes applied in optimized JSON

The following proposed changes are reflected in `optimized_container.json`:

- `CHG-NAME-001`: tag display-name cleanup.
- `CHG-NAME-002`: trigger display-name cleanup.
- `CHG-NAME-003`: variable display-name cleanup.
- `CHG-NAME-004`: folder display-name cleanup.
- `CHG-REF-001`: variable-token maintenance required by the proposed variable rename.

`optimized_container.json` is a proposed artifact, not a publish-ready guarantee.

## 6. Changes recommended but not applied

No deletion, disabling, trigger-logic change, tag-payload change, consent-setting change, ecommerce-payload change, or live-platform change was recommended or applied.

Manual review remains required for all proposed changes because old GTM names may be referenced outside the exported file, such as in documentation, QA scripts, reports, or analyst workflows.

## 7. Validation results

Validation status: `passed_with_warnings`.

Observed structural validation results:

- Source JSON parsed successfully.
- Source contains `exportFormatVersion` and `containerVersion`.
- Source references resolved: tag `101` references trigger `201`; tag `101` uses variable token `{{id}}`; folder `401` exists.
- Optimized references resolved after rename: tag `101` references trigger `201`; tag `101` uses variable token `{{CONST - GA4 Measurement ID}}`; folder `401` exists.
- Entity IDs, tag type, trigger type, `eventName`, constant value, folder IDs, fingerprints, and built-in variables are preserved.

Validation results do not prove tracking correctness, consent behavior, legal compliance, privacy compliance, or production readiness.

## 8. QA checklist

Highest-priority QA items:

- Confirm the package includes all seven required artifacts.
- Review every proposed rename before import or use.
- Confirm the GA4 event tag still resolves the measurement ID variable after the variable rename.
- Use a safe review context and GTM Preview before any production decision.
- Capture evidence for tag `101`, trigger `201`, variable `301`, and folder `401`.

See `qa_checklist.md` for the full manual checklist.

## 9. Human approval notes

Human review is required before import, workspace creation, publishing, or production use.

No live GTM, GA4, Google Ads, API, workspace, website, or production platform was connected to, inspected, changed, imported, published, or verified.

## 10. Appendix: entity-level findings

### `F-INV-001` — Container inventory summarized from export

- Rule ID: `GTM-INV-001`
- Severity: Info
- Category: Inventory
- Affected entity: container `5101`, `Synthetic Naming Issues Container`
- Detected facts: export format version is `2`; public ID is `GTM-SYN501`; the export contains 1 tag, 1 trigger, 1 variable, 1 folder, 1 built-in variable, and 0 custom templates.
- Recommendation: Use as audit coverage context.
- Automated-change policy: `blocked`
- Related QA item: `QA-001`

### `F-NAME-001` — Vague tag name

- Rule ID: `GTM-NAME-001`
- Severity: Low
- Category: Naming
- Affected entity: tag `101`, `tag 1`
- Detected facts: tag type is `gaawe`; event name is `lead_submit`; firing trigger ID is `201`; parent folder ID is `401`.
- Inferred issue: the tag name does not identify platform, tag type, or event purpose.
- Recommendation: rename to `GA4 - Event - lead_submit`.
- Automated-change policy: `allowed_candidate`
- Manual review: required.
- Related change: `CHG-NAME-001`
- Related QA item: `QA-002`

### `F-NAME-002` — Vague trigger name

- Rule ID: `GTM-NAME-001`
- Severity: Low
- Category: Naming
- Affected entity: trigger `201`, `all`
- Detected facts: trigger type is `PAGEVIEW`.
- Inferred issue: the trigger name does not identify trigger type or page scope clearly.
- Recommendation: rename to `PV - All Pages`.
- Automated-change policy: `allowed_candidate`
- Manual review: required.
- Related change: `CHG-NAME-002`
- Related QA item: `QA-003`

### `F-NAME-003` — Vague variable name

- Rule ID: `GTM-NAME-001`
- Severity: Low
- Category: Naming
- Affected entity: variable `301`, `id`
- Detected facts: variable type is `c`; value is `G-TEST501`; tag `101` references it through measurement ID token `{{id}}`.
- Inferred issue: the variable name does not identify variable type or purpose.
- Recommendation: rename to `CONST - GA4 Measurement ID` and maintain the tag token reference as `{{CONST - GA4 Measurement ID}}`.
- Automated-change policy: `allowed_candidate`
- Manual review: required.
- Related changes: `CHG-NAME-003`, `CHG-REF-001`
- Related QA item: `QA-004`

### `F-NAME-004` — Vague folder name

- Rule ID: `GTM-NAME-001`
- Severity: Low
- Category: Naming
- Affected entity: folder `401`, `misc`
- Detected facts: folder `401` contains tag `101` and variable `301`.
- Inferred issue: the folder name does not identify grouping purpose.
- Recommendation: rename to `GA4 - Core Measurement`.
- Automated-change policy: `allowed_candidate`
- Manual review: required.
- Related change: `CHG-NAME-004`
- Related QA item: `QA-005`
