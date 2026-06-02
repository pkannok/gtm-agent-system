# Deliverable Contract: GTM Container Audit & Patch Package

## Contract name

GTM Container Audit & Patch Package

## Purpose

This reference defines the required artifact contract for the **GTM Container Audit & Patch Package** inside the `gtm-container-auditor` Skill.

Use it to confirm package completeness, preserve the canonical deliverable name, and avoid treating `optimized_container.json` as the only output.

## Contract status

Canonical MLP deliverable contract.

## When this contract applies

Use this contract when the user asks to audit, clean up, optimize, review, or prepare proposed changes for a Google Tag Manager container export JSON file.

## Required package artifacts

The package must include:

1. `optimized_container.json`
2. `audit_report.md`
3. `audit_report.json`
4. `change_log.json`
5. `validation_report.json`
6. `qa_checklist.md`
7. `run_metadata.json`

## Completion rule

The deliverable is incomplete if it only includes `optimized_container.json`.

## Safety rule

The package is a proposal for analyst review. It must not claim that changes are safe to publish.

Human review is required before import, workspace creation, publishing, or production use.

The MLP does not publish GTM changes, create GTM workspaces, call GTM APIs, or certify legal, privacy, consent, tracking, or production readiness.

## Future compatibility

This contract should be referenced by:

- Custom GPT instructions.
- Skill instructions.
- Output schemas.
- Validation scripts.
- Golden tests.
- Future API or Agents SDK workflows.
