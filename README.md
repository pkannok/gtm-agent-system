# GTM Agent System

This repository defines a portable Custom GPT + Skill system for technical marketing analytics workflows.

## Current milestone

Task 0.1: Define the canonical MLP deliverable.

## Canonical MLP deliverable

The first MLP deliverable is:

**GTM Container Audit & Patch Package**

It is produced from a GTM container export JSON and optional client standards.

## Required MLP output files

A complete package includes:

1. `optimized_container.json`
2. `audit_report.md`
3. `audit_report.json`
4. `change_log.json`
5. `validation_report.json`
6. `qa_checklist.md`
7. `run_metadata.json`

## Key product decision

The MLP will not produce optimized GTM JSON as the only deliverable.

The optimized JSON must be accompanied by audit findings, change log, validation report, QA checklist, and run metadata.

## Current files

- `docs/decisions/ADR-0001-canonical-mlp-deliverable.md`
- `docs/mlp-deliverable.md`
- `custom-gpt/instructions-draft.md`
- `skills/gtm-container-auditor/references/deliverable-contract.md`
- `outputs/_template/README.md`
