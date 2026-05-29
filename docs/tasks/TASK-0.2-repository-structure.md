# Task 0.2 — Create the portable project repository

## Status

Ready for review

## Goal

Create a clean repository structure that can support the Custom GPT, Skill, standards, future schemas, scripts, fixtures, tests, and documentation. The Custom GPT should be treated as a user interface. The repository should contain the portable source materials needed to recreate, inspect, test, and evolve the system.

## In scope

- Repo folders
- README updates
- Roadmap updates
- Placeholder documentation files where useful
- Custom GPT draft folder
- Skill draft folder

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

#### Expected Task 0.2 outputs

Task 0.2 should produce or confirm the following repository structure:

```text
gtm-agent-system/
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

#### Task 0.2 working rules

- Keep the repository portable.
- Do not rely on Custom GPT configuration as the only source of truth.
- Store instructions, decisions, roadmap, and deliverable definitions in version-controlled files.
- Prefer plain Markdown for planning and documentation.
- Do not create schemas, validators, synthetic fixtures, API connectors, GitHub Actions, or production scripts unless explicitly asked.
- Do not build the full Skill yet.
- Do not configure live API actions yet.
- Keep this task focused on repository structure and source-of-truth documentation.

## Expected files changed

- `README.md`
- `AGENTS.md`
- `CHANGELOG.md`
- `docs/roadmap.md`
- `docs/glossary.md`
- `docs/architecture.md`
- `docs/tasks/TASK-0.2-repository-structure.md`
- `custom-gpt/`
- `skills/gtm-container-auditor/`
- `outputs/_template/`

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
- [x] Source-of-truth documentation exists.
