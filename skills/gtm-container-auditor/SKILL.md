---
name: gtm-container-auditor
description: audit, validate, and improve google tag manager container export json files for technical marketing analytics workflows. use when a user uploads or references a gtm container export and asks for cleanup, optimization, audit findings, tracking qa, tag/trigger/variable review, client-standard compliance, or a proposed optimized container json.
---

# GTM Container Auditor

Use this Skill to produce a file-in/file-out **GTM Container Audit & Patch Package** from a Google Tag Manager container export JSON. Keep `SKILL.md` concise; load supporting references only when they are needed for the user's request.

## Core Workflow

1. Confirm the input is a GTM container export JSON.
2. Load agency standards and optional client profile.
3. Parse and summarize the container.
4. Apply the audit rule catalog.
5. Create findings with evidence.
6. Propose safe changes as low-risk, reversible file-based proposals when allowed; never treat them as publish-ready.
7. Generate `optimized_container.json`.
8. Generate `change_log.json`.
9. Run validation.
10. Return the full GTM Container Audit & Patch Package.

## Required Package Artifacts

Return the full package, not only optimized JSON:

1. `optimized_container.json`
2. `audit_report.md`
3. `audit_report.json`
4. `change_log.json`
5. `validation_report.json`
6. `qa_checklist.md`
7. `run_metadata.json`

## Safety Rules

- Do not claim changes are safe to publish.
- Prefer reversible changes.
- Do not delete entities in the MLP unless explicitly requested.
- Flag Custom HTML, advertising tags, consent-sensitive tags, enhanced conversions, and user identifier handling for manual review.
- Require human review before import, workspace creation, publishing, or production use.
- Do not call live GTM, GA4, Google Ads, or other production APIs.
- Treat `optimized_container.json` as a proposed artifact, not the complete deliverable.

## Supporting References

- Use `references/deliverable-contract.md` to preserve the canonical deliverable name, required artifact list, and completion rules.
- Use `references/audit-rules.md` when findings need rule IDs, evidence requirements, severity guidance, automated-change policy, or manual-review triggers.
- Use `references/output-standards.md` when writing `audit_report.md`, QA guidance, severity labels, uncertainty notes, or human approval notes.
- Use agency standards and client profiles when they are bundled with the Skill, supplied by the user, or available in the repository.
- Use schema files when they are bundled with the Skill or available in the repository to keep machine-readable artifacts aligned with the project contracts.
