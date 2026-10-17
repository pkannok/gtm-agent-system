# GTM Container Audit & Patch Package — Audit Report

## 1. Executive summary
- **Fixture:** `synthetic-consent-001`; **source:** `synthetic-consent-risk-remarketing.json`.
- **Container:** Synthetic Consent Risk Container (`GTM-SYN506`).
- **Overall risk:** **high**. **Findings:** 2 high, 1 medium, 0 low, 0 info.
- **Human approval:** mandatory. **Changes applied in optimized JSON:** 0; source configuration preserved.
- This output is a **draft proposal for human review**, not a publish-ready artifact.

## 2. Container inventory
- Account `9001`, container `5106`, format version `2`.
- Tags **2**; triggers **1**; user-defined variables **1**; built-in variables **1**; folders **1**; custom templates **0**; zones **0** (zone section not present).
- Tag `106` is `Google Ads - Remarketing - All Pages` (`sp`); tag `107` is `Custom HTML - Vendor Pixel` (`html`). Both reference trigger `206`, `PV - All Pages` (`PAGEVIEW`).
- Variable `306`, `CONST - Google Ads Conversion ID`, resolves the variable name used by tag `106`. Both tags reference folder `406`, `Ads - Consent Review Required`.
- All observed tag-to-trigger, folder and explicit variable-name references resolve in the export. No explicit consentSettings or blockingTriggerId field appears on either tag. This is **not proof of absent runtime consent enforcement**.

## 3. Highest-risk findings
### F-001 · GTM-CONSENT-001 · HIGH
- **Affected:** tag `106`, trigger `206`, variable `306`.
- **Detected:** Google Ads remarketing tag type `sp`, using `{{CONST - Google Ads Conversion ID}}`, fires on broad `PV - All Pages` pageview trigger. No explicit tag-level `consentSettings` or `blockingTriggerId` exported.
- **Inference:** Risk of consent-sensitive firing without adequate gating; live behavior unknown.
- **Recommendation:** Human consent policy, GTM Preview and network review, including denied and granted states.
- **Automated-change policy:** `blocked`; manual and consent reviews required. **QA:** QA-002, QA-003. **Change:** none.

### F-002 · GTM-CONSENT-001 · HIGH
- **Affected:** tag `107`, trigger `206`.
- **Detected:** Custom HTML loads `<script src="https://vendor.example.test/pixel.js"></script>` on trigger `206`; no explicit tag-level consent or blocking fields.
- **Inference:** Remotely loaded code may collect or transmit data not visible in the export.
- **Recommendation:** Developer/vendor code and network inspection; analyst/privacy review across consent states.
- **Automated-change policy:** `blocked`; manual and consent reviews required. **QA:** QA-002, QA-004. **Change:** none.

### F-003 · GTM-QA-001 · MEDIUM
- **Affected:** tags `106`, `107`; trigger `206`.
- **Detected:** Both share broad pageview scope; no runtime evidence supplied.
- **Inference:** GTM Preview verification is essential before relying on the setup.
- **Recommendation:** Document consent initialization, denied/granted behavior and request payloads in approved non-production testing.
- **Automated-change policy:** `blocked`. **QA:** QA-002, QA-003, QA-004. **Change:** none.

## 4. Proposed changes
No automated file-based configuration changes proposed. Consent-related adjustments, HTML edits, trigger rewiring, disabling/removal and payload modifications are **blocked** by agency standards until human decisions. `change_log.json` has an empty `changes` list and records unapplied review recommendations.

## 5. Changes applied in optimized JSON
**None.** `optimized_container.json` retains the full original export wrapper, tags, triggers, variable, folder, built-in variable and custom template array unchanged. The file exists as a draft review artifact only. `optimized_container.json` is a proposed artifact, not a publish-ready guarantee.

## 6. Changes recommended but not applied
- **F-001:** Evaluate client-approved consent settings, consent initialization and remarketing scope; do not add consent checks or change trigger `206` automatically.
- **F-002:** Inspect vendor code and requests; do not rewrite HTML or disable/delete tag `107` automatically.
- **F-003:** Perform approved QA and obtain stakeholder decisions before proposing later changes.
- Relevant catalog rules: `GTM-CONSENT-001`, `GTM-QA-001`. Any future remediation should receive its own reviewed change ID, scope and rollback notes.

## 7. Validation results
JSON structure and references are checked locally. Package contains seven artifacts; optimized JSON is structurally identical to the input. No missing internal referenced trigger, folder or named variable detected.
Warnings: consent gating is unproven; external vendor script code is not provided; no live QA, schema validator, site or API access was used. See `validation_report.json`.
**Validation results do not prove tracking correctness, consent behavior, legal compliance, privacy compliance, or production readiness.**

## 8. QA checklist
See `qa_checklist.md`: package inventory, denied/default consent, granted/transition consent, vendor script inspection, measurement-scope check and rejection/rollback approval. All require human completion; blocked tests need approved isolated context.

## 9. Human approval notes
Human review is required before import, workspace creation, publishing, or production use. GTM analyst, privacy/legal reviewer and developer/vendor reviewer should resolve F-001 and F-002. This analysis neither accesses nor changes live platforms.

## 10. Appendix: entity-level findings
- **F-001:** tag `106` → trigger `206`; conversion-ID variable `306`; folder `406`. Consent fields absent in tag record; risk inference only. Rule `GTM-CONSENT-001`, high, blocked, QA-002/003.
- **F-002:** tag `107` → trigger `206`; external domain `vendor.example.test`; folder `406`. Source HTML visible, external script behavior unknown. Rule `GTM-CONSENT-001`, high, blocked, QA-002/004.
- **F-003:** tags `106` and `107` → trigger `206`. No live consent evidence. Rule `GTM-QA-001`, medium, blocked, QA-002/003/004.
- **Related change IDs:** none for all findings because no automated patch was permitted.
