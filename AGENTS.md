# AGENTS.md

## Project

This repository defines and implements a portable GTM Container Audit & Patch Package system for a future Custom GPT + Skill workflow.

The system is being built in phases. The current phase is **Phase 0: Project framing and repository setup**.

The long-term goal is a portable technical marketing analyst system that starts as a file-in/file-out Custom GPT + Skill and can later expand into API-backed tools, validation scripts, and multi-agent workflows.

## Canonical MLP deliverable

The canonical MLP deliverable is:

**GTM Container Audit & Patch Package**

A complete MLP output package includes:

1. `optimized_container.json`
2. `audit_report.md`
3. `audit_report.json`
4. `change_log.json`
5. `validation_report.json`
6. `qa_checklist.md`
7. `run_metadata.json`

A run is incomplete if it only produces `optimized_container.json`.

## Current active task

Active task: Task 0.2 — Create the portable project repository

Primary task brief:

- `docs/tasks/TASK-0.2-repository-structure.md`

Supporting context:

- `docs/roadmap.md`
- `docs/mlp-deliverable.md`
- `docs/decisions/ADR-0001-canonical-mlp-deliverable.md`

Do not work outside the active task scope.

## Project working rules

- Prefer small, reviewable changes.
- Keep all project decisions in repo files, not only in ChatGPT or Custom GPT configuration.
- Use plain Markdown for planning documents.
- Treat the Custom GPT as a user interface, not the system of record.
- Treat the Skill as a reusable package that will later reference the same deliverable contract.
- Preserve the exact deliverable name: GTM Container Audit & Patch Package.
- Do not describe optimized_container.json as the only MLP output.
- Do not imply that any generated GTM JSON is safe to publish without human review.

#### Task 0.2 working rules

- Keep the repository portable.
- Do not rely on Custom GPT configuration as the only source of truth.
- Store instructions, decisions, roadmap, and deliverable definitions in version-controlled files.
- Prefer plain Markdown for planning and documentation.
- Do not create schemas, validators, synthetic fixtures, API connectors, GitHub Actions, or production scripts unless explicitly asked.
- Do not build the full Skill yet.
- Do not configure live API actions yet.
- Keep this task focused on repository structure and source-of-truth documentation.

## Out of scope

- JSON schemas
- Python scripts
- Validators
- Synthetic fixtures
- API connectors
- Full Skill implementation
- Custom GPT creation in ChatGPT UI
