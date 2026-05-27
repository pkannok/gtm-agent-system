# Roadmap

## Project goal

Build a portable Custom GPT + Skill system for technical marketing analytics workflows, starting with a file-in/file-out GTM Container Audit & Patch Package MLP.

The system should begin as a practical Custom GPT + Skill workflow and evolve toward a more structured architecture with schemas, validators, test fixtures, API connectors, and eventually orchestrated specialist agents.

## Canonical MLP deliverable

The first MLP deliverable is:

**GTM Container Audit & Patch Package**

A complete MLP output package includes:

1. `optimized_container.json`
2. `audit_report.md`
3. `audit_report.json`
4. `change_log.json`
5. `validation_report.json`
6. `qa_checklist.md`
7. `run_metadata.json`

The MLP does not produce optimized GTM JSON as the only deliverable.

---

# Phase 0 — Project framing and repository setup

## Goal

Create the durable project foundation before building schemas, scripts, fixtures, the full Skill, or the Custom GPT configuration.

The repository should become the system of record for the Custom GPT + Skill system.

## Tasks

### Task 0.1 — Define the canonical MLP deliverable

Status: Complete.

Outcome:

The project has defined the canonical MLP deliverable as:

**GTM Container Audit & Patch Package**

Required output artifacts:

1. `optimized_container.json`
2. `audit_report.md`
3. `audit_report.json`
4. `change_log.json`
5. `validation_report.json`
6. `qa_checklist.md`
7. `run_metadata.json`

Completed artifacts:

- `docs/decisions/ADR-0001-canonical-mlp-deliverable.md`
- `docs/mlp-deliverable.md`
- `custom-gpt/instructions-draft.md`
- `skills/gtm-container-auditor/references/deliverable-contract.md`
- `outputs/_template/README.md`

Definition of done:

- Complete.

---

### Task 0.2 — Create the portable project repository

Status: Ready for review.

Goal:

Create a clean repository structure that can support the Custom GPT, Skill, standards, future schemas, scripts, fixtures, tests, and documentation.

Why this matters:

The Custom GPT should be easy to recreate or move. The repository should hold the durable source materials so the system is portable across ChatGPT instances, OpenAI API workflows, future agent runtimes, or other model environments.

Expected outputs:

```text
README.md
AGENTS.md
CHANGELOG.md
docs/
  roadmap.md
  glossary.md
  architecture.md
  mlp-deliverable.md
  decisions/
    ADR-0001-canonical-mlp-deliverable.md
  tasks/
    TASK-0.2-repository-structure.md
custom-gpt/
  instructions-draft.md
  description.md
  conversation-starters.md
  test-prompts.md
skills/
  gtm-container-auditor/
    references/
      deliverable-contract.md
outputs/
  _template/
    README.md
```

## Definition of done

- [x] The repository has a clear, stable folder structure.
- [x] `README.md` explains the project and current MLP direction.
- [x] `AGENTS.md` points to the active task.
- [x] `docs/roadmap.md` exists and tracks phases/tasks.
- [x] `CHANGELOG.md` exists or is intentionally deferred with a note.
- [x] `skills/gtm-container-auditor/` exists for future Skill work.
- [x] `outputs/_template/README.md` documents the expected output package shape.
- [x] Repo can be cloned or copied without losing core project context.
- [x] No schemas, scripts, fixtures, API connectors, GitHub Actions, production scripts, or live API actions were created.

## Out of scope

- JSON schemas
- Python scripts
- Validators
- Synthetic fixtures
- API connectors
- Full Skill implementation
- Custom GPT creation in ChatGPT UI
- GitHub Actions
- Production scripts
- Live API actions
