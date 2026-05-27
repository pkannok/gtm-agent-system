# GTM Agent System

This repository defines a portable Custom GPT + Skill system for technical marketing analytics workflows.

## Current milestone

Task 0.2: Establish the portable project repository.

Task 0.1 status: complete. The canonical MLP deliverable is defined and accepted in ADR-0001.

## Canonical MLP deliverable

The first MLP deliverable is:

**GTM Container Audit & Patch Package**

It is produced from a Google Tag Manager container export JSON and optional client standards.

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

## Repository structure

- `docs/` - Product decisions, MLP deliverable documentation, architecture notes, glossary, and roadmap.
- `docs/tasks/` - Detailed task scope and acceptance criteria.
- `custom-gpt/` - Custom GPT instructions, draft instructions, description, conversation starters, and test prompts.
- `skills/gtm-container-auditor/` - Future reusable Skill package, including references, schemas, scripts, agents, and recipes.
- `outputs/_template/` - Expected output folder shape for the GTM Container Audit & Patch Package.

Some Task 0.2 files may be scaffolds until their corresponding implementation tasks are started.
