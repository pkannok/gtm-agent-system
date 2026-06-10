# Current Task

Current active task:

- Task 6.1 - Create Custom GPT configuration

Next recommended task:

- Task 6.1 - Create Custom GPT configuration

Next task brief:

- `docs/tasks/TASK-6.1-custom-gpt-configuration.md`

Most recent completed task brief:

- `docs/tasks/TASK-5.3-manual-evaluation-rubric.md`

Most recent completed phase brief:

- `docs/tasks/PHASE-5-goal-build-synthetic-fixtures-and-tests.md`

## Instructions for Codex

Before editing files for a future active task:

1. Read `AGENTS.md`.
2. Read this file.
3. Read the active task brief, if one is listed.
4. Summarize the task goal, expected files changed, files that should not change, and scope-creep risks.

Do not work outside the active task scope.

## Current boundaries

- Do not create Custom GPT configuration files, instructions, knowledge-file copies, capability configuration, or conversation starters unless the active task explicitly requires them.
- Do not create GitHub Actions, API connectors, live API actions, or Custom GPT final UI configuration beyond the active task scope.
- Do not modify the completed Phase 3 Skill package unless the active task explicitly requires it.
- Do not configure live GTM, GA4, or Google Ads API access.
- Treat all generated GTM artifacts as draft proposals for human analyst review.

## Phase 4 progress

- Task 4.1 is complete. `scripts/normalize_gtm_export.py` can normalize a GTM export into a deterministic summary JSON with metadata, counts, lookup maps, preserved entities, warnings, and safety flags.
- Task 4.2 is complete. `scripts/validate_gtm_container.py` can validate JSON parsing, expected GTM sections, tag trigger references, folder references, and detectable variable references.
- Task 4.3 is complete. `scripts/diff_gtm_containers.py` can compare original and optimized GTM exports and output a machine-readable proposed change log.
- Task 4.4 is complete. `scripts/validate_output_package.py` can validate required GTM Container Audit & Patch Package artifacts, schema-backed JSON artifacts, package consistency, safety flags, and validation-report-compatible output.
- Phase 4 is complete.

## Phase 5 progress

- Task 5.1 is complete. `examples/synthetic-gtm-containers/` contains six small, deterministic, synthetic GTM container export fixtures with documented expected issues and no real client data.
- Task 5.2 is complete. `examples/golden-expected-outputs/` contains schema-aligned expected GTM Container Audit & Patch Package shapes for the synthetic fixtures.
- Task 5.3 is complete. `docs/evaluation/manual-evaluation-rubric.md` can be applied to fixture outputs and checks usefulness, safety, clarity, manual-review handling, and unsafe recommendations.
- Phase 5 is complete. Task 6.1 is the next recommended task.

## Phase 6 progress

- Task 6.1 is in progress. Repo configuration fields are being recorded in `custom-gpt/configuration.md`; GPT editor creation, internal access verification, and editor version-history verification are still required before completion.
