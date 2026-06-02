# Client Overrides Reference

## Purpose

This reference explains how the `gtm-container-auditor` Skill should apply agency standards, optional client profiles, client overrides, and user task instructions when producing a **GTM Container Audit & Patch Package**.

Client overrides can narrow or clarify recommendations. They must not remove required package artifacts, bypass human review, authorize live GTM changes, or imply that generated GTM JSON is safe to publish.

## Contents

- Override sources
- Priority order
- Conflict handling
- Recording applied standards
- Manual-review rules

## Override Sources

The Skill may receive client-specific direction from:

- A `client_profile` artifact that follows the project schema.
- A client standards document supplied by the user.
- A user instruction in the current task.
- A previously agreed client override stored in the repository.

Treat client-specific direction as reusable only when the user clearly presents it as a client standard or client override. A one-off task instruction should influence the current run but should not become a reusable client override by itself.

## Priority Order

Apply rules in this order:

1. Non-negotiable project safety constraints.
2. Canonical deliverable contract.
3. Active user task instruction for the current run.
4. Explicit client profile or client override.
5. Agency standards.
6. Audit rule catalog.
7. Model inference from the exported GTM configuration.

Project safety constraints always win. A client override cannot allow the MLP to publish GTM changes, create a workspace, call live APIs, skip human review, treat `optimized_container.json` as the only deliverable, or remove required artifacts from the package.

## Conflict Handling

When sources conflict:

- Prefer the stricter safety requirement.
- Preserve the seven required MLP artifacts.
- Mark the conflict in `audit_report.md` or `audit_report.json`.
- Add a manual-review item when the correct action is unclear.
- Do not silently choose a client override that weakens consent, privacy, QA, or human approval boundaries.

Examples:

- If a client naming convention differs from the agency convention, use the client naming convention when it is explicit and does not weaken safety.
- If a client asks to ignore consent review for advertising tags, keep consent review required and record the conflict for manual review.
- If a user asks for only `optimized_container.json`, explain that the GTM Container Audit & Patch Package requires the full artifact set.
- If a client wants Custom HTML edited automatically, keep the edit blocked or manual-review only unless a later approved task changes that policy.

## Recording Applied Standards

Record applied standards and overrides in machine-readable artifacts when the schema or artifact allows it.

Use clear source labels such as:

- `agency_standard`
- `client_profile`
- `client_override`
- `user_intent`

For each applied standard or override, capture:

- Standard or override ID when available.
- Name or short description.
- Source.
- Version when available.
- Any assumption needed to apply it.

If the source is missing an ID, create a temporary run-local label and state that it is not a durable repository standard.

## Manual-Review Rules

Require manual review when:

- A client override conflicts with project safety constraints.
- A client override conflicts with agency consent, privacy, or QA standards.
- A client instruction affects advertising, remarketing, enhanced conversions, user identifiers, sensitive data, Custom HTML, custom templates, or ecommerce values.
- A client preference would change trigger logic, variable values, tag payloads, consent settings, or deletion behavior.
- A client standard is ambiguous, incomplete, or inferred from examples rather than stated explicitly.

When uncertain, preserve the exported GTM configuration, document the ambiguity, and recommend human analyst review.

## Out-of-Scope Override Effects

Client overrides must not:

- Publish GTM changes.
- Create GTM workspaces.
- Call GTM, GA4, Google Ads, or other live APIs.
- Claim legal compliance, privacy compliance, consent certification, or production readiness.
- Remove human review before import, workspace creation, publishing, or production use.
- Treat schema validation as tracking QA.
- Treat `optimized_container.json` as a complete deliverable by itself.
