# AGENTS.md

## Project

This repository defines and implements a portable GTM Container Audit & Patch Package system for a future Custom GPT + Skill workflow.

The long-term goal is a portable technical marketing analyst system that starts as a file-in/file-out Custom GPT + Skill and can later expand into schemas, validators, scripts, fixture tests, API connectors, and multi-agent workflows.

## Active task source of truth

The active task is defined in `docs/tasks/CURRENT.md`.

Before making changes, read:

- `docs/tasks/CURRENT.md`
- Any active task brief referenced from `docs/tasks/CURRENT.md`
- `docs/roadmap.md`
- `docs/mlp-deliverable.md`
- `docs/decisions/ADR-0001-canonical-mlp-deliverable.md`

Do not work outside the active task scope.

Task-specific constraints, implementation details, and temporary out-of-scope lists belong in `docs/tasks/CURRENT.md` or the referenced task brief, not in this file.

## Canonical MLP deliverable

The canonical MLP deliverable is:

**GTM Container Audit & Patch Package**

It is a file-in/file-out package produced from a Google Tag Manager container export JSON.

It must include `optimized_container.json`, but it must not treat that JSON as the only deliverable.

All generated GTM artifacts are draft proposals and must be reviewed and approved by a human analyst before import, workspace creation, publishing, or production use.

For the full deliverable contract, use `docs/mlp-deliverable.md` and `docs/decisions/ADR-0001-canonical-mlp-deliverable.md`.

## Required Codex workflow

1. Read the active task source and referenced docs before editing.
2. Summarize the intended scope before edits.
3. Keep changes limited to files implied by the active task.
4. Review the diff against the active task after edits.
5. Return a pass/fail against the definition of done.

## Standing working rules

- Keep changes small and reviewable.
- Treat the repository as the system of record.
- Treat the Custom GPT as a user interface, not the system of record.
- Treat the Skill as a reusable package that will later reference repo-defined contracts.
- Prefer plain Markdown for planning and documentation.
- Do not introduce implementation code or artifacts unless the active task explicitly requires them.
- Do not create schemas, validators, scripts, fixtures, recipes, GitHub Actions, API connectors, or full Skill implementation files unless the active task explicitly requires them.
- Do not configure live GTM, GA4, or Google Ads API access unless the active task explicitly requires it.
- Do not imply generated GTM JSON is safe to publish.
- Do not imply the MLP replaces human QA.
- Preserve the exact deliverable name: **GTM Container Audit & Patch Package**.
- Keep all project decisions in repo files, not only in ChatGPT or Custom GPT configuration.
- Do not describe optimized_container.json as the only MLP output.
