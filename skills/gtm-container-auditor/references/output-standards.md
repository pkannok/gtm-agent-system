# Output Writing Standard

## Purpose

This standard defines how human-readable GTM Container Audit & Patch Package reports should be written.

It is intended for future Custom GPT and Skill workflows that produce `audit_report.md` and related human-readable guidance. It must stay aligned with the canonical package artifacts:

1. `optimized_container.json`
2. `audit_report.md`
3. `audit_report.json`
4. `change_log.json`
5. `validation_report.json`
6. `qa_checklist.md`
7. `run_metadata.json`

The report must help a human analyst review proposed GTM changes. It must not imply that `optimized_container.json` is the only deliverable, safe to publish, production-ready, legally compliant, privacy compliant, or a replacement for GTM Preview and human QA.

## Contents

- Core writing rules
- Fixed report structure
- Severity label definitions
- Statement type rules
- Rules against hiding uncertainty
- Artifact alignment
- Disallowed claims

## Core Writing Rules

- Use plain, direct language.
- Separate detected facts from inferred issues, recommendations, assumptions, and items requiring manual verification.
- Cite audit rule IDs from `skills/gtm-container-auditor/references/audit-rules.md` when describing findings.
- Tie proposed changes back to finding IDs and change IDs when available.
- Make uncertainty visible. Never smooth over missing evidence.
- Use "proposed", "appears", "observed", "requires review", and "manual verification required" when evidence is incomplete.
- Do not claim that validation, naming cleanup, consent review, or rule matching proves tracking correctness, legal compliance, privacy compliance, or production readiness.

## Fixed Report Structure

Every `audit_report.md` should use these sections in this order.

### 1. Executive summary

Purpose:
Give the analyst a short, decision-ready overview.

Include:

- Container name and source filename when available.
- Overall risk level.
- Count of high, medium, low, and info findings.
- Whether human approval is required.
- Whether any proposed changes were included in `optimized_container.json`.
- One clear sentence stating that generated GTM artifacts are draft proposals for human review.

Do not include:

- Claims that the optimized container is safe to publish.
- Legal, privacy, or compliance certification.
- Detailed entity-level findings that belong in the appendix.

### 2. Container inventory

Purpose:
Summarize what the export contains so the analyst understands audit coverage.

Include:

- Account ID, container ID, and container name when present.
- Export format version when present.
- Counts of tags, triggers, variables, folders, templates, zones, and other relevant entities.
- Notable limitations, such as missing sections or malformed data.
- Rule IDs such as `GTM-INV-001` when inventory issues are found.

### 3. Highest-risk findings

Purpose:
Surface the findings most likely to affect tracking quality, consent-sensitive behavior, ecommerce, conversion tracking, or review safety.

Include each high-risk finding with:

- Finding ID.
- Rule ID.
- Severity.
- Affected entity or entities.
- Detected facts.
- Inferred issue, if any.
- Recommended action.
- Manual-review requirement.
- Related change ID, if any.

If no high-risk findings are present, state that no high-risk findings were detected from the export. Do not say the container is safe.

### 4. Proposed changes

Purpose:
Explain all proposed changes in plain language.

Include:

- Change ID.
- Related finding ID.
- Affected entity type, ID, and name.
- What would change.
- Why the change is proposed.
- Risk level.
- Automated change policy from the relevant audit rule.
- Rollback note.
- Human approval requirement.

Make clear that a proposed file-based patch is not a live GTM mutation.

### 5. Changes applied in optimized JSON

Purpose:
List proposed changes reflected in `optimized_container.json`.

Include:

- Change IDs included in `optimized_container.json`.
- Whether each change is name-only, structural, configuration-related, or documentation-only.
- Why the change was considered eligible for inclusion.
- Any remaining manual-review or QA requirements.

Required safety wording:
`optimized_container.json` is a proposed artifact, not a publish-ready guarantee.

### 6. Changes recommended but not applied

Purpose:
Show recommendations that should not be applied automatically.

Include:

- Recommended change or review item.
- Reason it was not applied.
- Manual-review trigger.
- Relevant rule ID.
- Suggested analyst next step.

Examples:

- Consent-sensitive tag changes.
- Custom HTML edits.
- Ecommerce payload changes.
- Deletions or disabling tags.
- Ambiguous reference repairs.

### 7. Validation results

Purpose:
Summarize structural validation and known limitations.

Include:

- Whether required package artifacts appear present.
- Whether JSON artifacts parse or validate when known.
- Warnings and errors from `validation_report.json`.
- Limitations of validation.

Required safety wording:
Validation results do not prove tracking correctness, consent behavior, legal compliance, privacy compliance, or production readiness.

### 8. QA checklist

Purpose:
Point the analyst to the required manual QA work.

Include:

- Summary of the highest-priority QA items from `qa_checklist.md`.
- GTM Preview scenarios.
- Ecommerce or conversion test scenarios.
- Consent-sensitive review scenarios.
- Items requiring legal, privacy, developer, or analyst review where applicable.

Do not imply that the MLP executed QA unless the evidence explicitly says so.

### 9. Human approval notes

Purpose:
Make approval boundaries impossible to miss.

Include:

- Human approval requirement.
- Who should review when known, such as analyst, developer, legal/privacy reviewer, or client stakeholder.
- Import, workspace creation, publishing, and production use boundaries.
- Any high-risk or manual-review-only changes.

Required safety wording:
Human review is required before import, workspace creation, publishing, or production use.

### 10. Appendix: entity-level findings

Purpose:
Provide the full finding detail without cluttering the executive sections.

Each entity-level finding should include:

- Finding ID.
- Rule ID.
- Severity.
- Category.
- Affected entity type.
- Affected entity ID and name, if available.
- Detected facts.
- Inferred issue, if any.
- Evidence.
- Recommendation.
- Automated-change policy.
- Manual-review triggers.
- Related change IDs.
- Related QA item IDs.

## Severity Label Definitions

Use these severity labels consistently in `audit_report.md` and `audit_report.json`.

### Info

Use for context, inventory notes, or neutral observations.

Examples:

- Container has 42 tags.
- A folder groups GA4 measurement tags.
- A validation check was not run.

### Low

Use for low-risk cleanup opportunities.

Examples:

- Clear name-only cleanup with no manual-review trigger.
- Folder organization issue.
- Documentation gap that does not affect firing behavior.

### Medium

Use for issues that may affect tracking quality, review confidence, consent-sensitive behavior, or maintainability.

Examples:

- Likely duplicate tags.
- Ambiguous variable purpose.
- Broken reference without clear production impact.
- Advertising tag requiring consent review.

### High

Use for issues that may affect conversion reporting, ecommerce revenue, consent-sensitive behavior, sensitive data handling, or production trust.

Examples:

- Purchase event missing required ecommerce data.
- Custom HTML sending user identifiers.
- Consent-sensitive tag firing broadly with unclear consent settings.
- Broken reference affecting conversion tracking.

## Statement Type Rules

Every important claim should fit one of these statement types.

### Detected fact

Definition:
Something directly observed in the GTM container export.

Use wording like:

- "The export contains..."
- "Tag `12` is named..."
- "The trigger uses..."

Do not add conclusions that are not supported by evidence.

### Inferred issue

Definition:
A likely issue based on evidence and standards.

Use wording like:

- "This appears to..."
- "This may indicate..."
- "This is likely duplicate because..."

Always include the evidence that supports the inference.

### Recommendation

Definition:
A proposed next step or file-based change.

Use wording like:

- "Recommend renaming..."
- "Recommend manual review..."
- "Recommend testing..."

Tie recommendations to rule IDs and explain whether the recommendation is applied, not applied, or manual-review only.

### Requires manual verification

Definition:
An item the MLP cannot verify from the file export alone.

Use wording like:

- "Manual verification required..."
- "Confirm in GTM Preview..."
- "Review with the appropriate analyst..."

Use this type for consent-sensitive behavior, Custom HTML, ecommerce behavior, external references, live firing behavior, and any uncertain inference.

## Rules Against Hiding Uncertainty

- Do not replace unknown values with polished guesses.
- Do not use confident wording when evidence is partial.
- Do not omit assumptions that affect the recommendation.
- Do not turn a manual-review-only finding into an applied change.
- Do not say "no issue" when the correct statement is "not detected from the export."
- Do not say "works" when the MLP has not observed live behavior.

## Artifact Alignment

`audit_report.md` should align with:

- `audit_report.json` for finding IDs, rule IDs, severities, evidence, and recommendations.
- `change_log.json` for proposed changes, rollback notes, and approval requirements.
- `validation_report.json` for validation status, warnings, errors, and limitations.
- `qa_checklist.md` for manual QA and preview/testing steps.
- `run_metadata.json` for run ID, input files, client ID, standards applied, and version details.

If the report and machine-readable artifacts conflict, flag the conflict in validation results or manual-review notes rather than hiding it.

## Disallowed Claims

Do not write:

- "This optimized container is safe to publish."
- "This change is production-safe."
- "This setup is legally compliant."
- "This consent setup is certified."
- "Validation proves tracking correctness."
- "No human review is required."
- "The MLP published or deployed GTM changes."

Use instead:

- "This output is a draft proposal for human review."
- "Human approval is required before import, workspace creation, publishing, or production use."
- "This finding is based on exported GTM configuration and does not verify live site behavior."
- "Legal or privacy review may be required for consent-sensitive items."
