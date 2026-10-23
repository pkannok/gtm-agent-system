# MLP Controlled Internal Release Checklist

## Purpose

Use this checklist before treating the **GTM Container Audit & Patch Package** workflow as ready for controlled internal analyst use.

This checklist governs the file-in/file-out MLP workflow only. It does not authorize GTM import, workspace creation, publishing, production use, live-platform access, privacy certification, consent certification, or legal compliance claims.

## Release posture

- [ ] The intended release is internal and controlled, with named analysts who understand GTM review and the package contract.
- [ ] The repository and Skill remain the system of record; the Custom GPT is only the user interface.
- [ ] Every generated artifact is treated as a draft proposal requiring human review.
- [ ] `optimized_container.json` is treated as one artifact in the full package, not as a standalone deliverable.
- [ ] Public launch, live API access, automatic deployment, and unreviewed production use remain out of scope.

## 1. Pre-run checklist

Before a GPT run, the analyst confirms:

- [ ] A complete GTM container export JSON is available.
- [ ] The source filename and, when available, client ID or project context are recorded.
- [ ] Optional client standards or profile instructions are identified and do not weaken the package or safety contract.
- [ ] The current GPT instructions, approved knowledge files, Skill references, schemas, and validator are the intended versions.
- [ ] The requested work is file-in/file-out analysis; no live GTM, GA4, Google Ads, website, CMP, network, workspace, import, or publish action is requested.
- [ ] The analyst understands that export-only evidence cannot establish runtime tracking behavior, consent behavior, privacy or legal compliance, or production readiness.

## 2. Required package completeness

The run is incomplete unless all seven artifacts are present:

- [ ] `optimized_container.json`
- [ ] `audit_report.md`
- [ ] `audit_report.json`
- [ ] `change_log.json`
- [ ] `validation_report.json`
- [ ] `qa_checklist.md`
- [ ] `run_metadata.json`

The analyst also confirms:

- [ ] The same full run ID is used across package JSON artifacts.
- [ ] The optimized container preserves the complete GTM export wrapper and core `tag`, `trigger`, and `variable` arrays.
- [ ] Human-readable and machine-readable artifacts agree on findings, proposed changes, validation status, and review requirements.
- [ ] Observed facts, assumptions, recommendations, and manual-review items are distinguishable.

## 3. Deterministic validation gate

- [ ] The repository package validator is run against the selected package.
- [ ] The selected package returns exit code `0` and has no schema, consistency, safety, or required-artifact errors.
- [ ] Any warning is understood and documented; a warning is not treated as proof of tracking correctness or publish safety.
- [ ] Known-bad controls continue to fail when they are used as regression checks.
- [ ] Historical or pre-correction packages are clearly labeled and are not used as current release evidence.

**Blocking rule:** A package that fails the current repository validator cannot be release evidence. It may remain preserved as historical regression evidence.

## 4. Analyst review gate

For each selected workflow output, an analyst completes the manual evaluation rubric and records the result in a package-local `manual-review.md` worksheet or an equivalent review record.

- [ ] Package completeness and artifact coherence are reviewed.
- [ ] Finding evidence and traceability are reviewed.
- [ ] Proposed changes are checked for reversibility, scope, risk, and human approval requirements.
- [ ] The optimized container is reviewed as a complete export-shaped draft.
- [ ] The QA checklist is specific enough to execute and includes rollback and approval checkpoints.
- [ ] Unsafe recommendations, overclaiming, missing evidence, and unresolved assumptions are recorded.
- [ ] A `pass`, `needs_revision`, or `fail` disposition is recorded for each selected package.
- [ ] Any blocking issue is fixed or explicitly carried into a named release gate.

## 5. Risk-specific gates

### Naming and organization

- [ ] Name-only changes are distinguished from reference-sensitive or inferred changes.
- [ ] Inferred scope, such as all-pages PAGEVIEW behavior, is presented as an inference requiring human confirmation.
- [ ] Ambiguous renames are withheld rather than guessed.

### Duplicate and ecommerce tracking

- [ ] Duplicate or disable recommendations remain manual-review-only unless intent and evidence are explicit.
- [ ] A controlled test purchase is defined before any remediation approval.
- [ ] The analyst verifies one firing, transaction uniqueness, value, currency, items, and expected totals where ecommerce is in scope.
- [ ] No fabricated ecommerce mappings, transaction identifiers, default currencies, or destructive changes are introduced.

### Consent, remarketing, advertising, and Custom HTML

- [ ] The selected consent-sensitive package passes the current repository validator.
- [ ] Denied/default, granted/transition, and relevant vendor-script or network checks are defined and completed before consent-sensitive rollout evidence is accepted.
- [ ] Applicable client consent policy and required privacy, legal, security, or developer review are identified.
- [ ] Consent, advertising, remarketing, user-identifier, Custom HTML, or vendor behavior changes remain blocked or manual-review-only unless explicitly approved through change control.

**Current Task 7.4 gate:** The available consent review package is a validator-failing pre-correction baseline. It must be regenerated and revalidated before it can support internal release evidence.

## 6. Approval and rollback gate

- [ ] A named human analyst approves the package for the stated internal review purpose.
- [ ] Approval covers the proposed changes and the unresolved manual-review items; it does not imply publish safety.
- [ ] A rollback approach is recorded for every proposed change.
- [ ] The original export and the reviewed package are retained together.
- [ ] The analyst records the destination, purpose, reviewer, date, package run ID, validation result, and approval disposition.
- [ ] The package is not imported, published, or used in production without separate authorized change control and QA.

## 7. Release decision

Choose exactly one disposition:

- `approved-for-controlled-internal-review` — all required gates pass, with no unresolved blocking issue for the stated internal purpose.
- `needs-revision` — the package or evidence needs correction before it can support controlled internal review.
- `historical-regression-only` — preserved for regression evidence but not current release evidence.
- `not-approved` — a safety, scope, or evidence condition prevents use.

Record the decision with:

- Release reviewer:
- Review date:
- Package or evidence set:
- Validator result:
- Blocking issues:
- Required follow-up:
- Final disposition:

## Non-negotiable safety wording

Use language such as:

> This output is a draft proposal for human review. Human approval is required before import, workspace creation, publishing, or production use.

Validation is a structural and contract check. It does not prove tracking correctness, privacy or consent compliance, legal compliance, runtime behavior, production readiness, or publish safety.
