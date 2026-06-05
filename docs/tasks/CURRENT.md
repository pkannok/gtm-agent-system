# Current Task

Current active task:

- None.

Next recommended task:

- Task 4.3 - Build `diff_gtm_containers.py`

Next task brief:

- `docs/tasks/TASK-4.3-diff-gtm-containers-script.md`

Most recent completed task brief:

- `docs/tasks/TASK-4.2-validate-gtm-container-script.md`

Most recent completed phase brief:

- `docs/tasks/PHASE-3-goal-build-skill-package.md`

## Instructions for Codex

Before editing files for a future active task:

1. Read `AGENTS.md`.
2. Read this file.
3. Read the active task brief, if one is listed.
4. Summarize the task goal, expected files changed, files that should not change, and scope-creep risks.

Do not work outside the active task scope.

## Current boundaries

- Do not start Task 4.3 implementation unless it is explicitly requested as the active task.
- Do not create the Task 4.3 diff script or Task 4.4 package validator unless the active task explicitly requires them.
- Do not create the full Phase 5 synthetic fixture suite or golden tests.
- Do not create GitHub Actions, API connectors, or Custom GPT final UI configuration.
- Do not modify the completed Phase 3 Skill package unless the active task explicitly requires it.
- Do not configure live GTM, GA4, or Google Ads API access.
- Treat all generated GTM artifacts as draft proposals for human analyst review.

## Phase 4 progress

- Task 4.1 is complete. `scripts/normalize_gtm_export.py` can normalize a GTM export into a deterministic summary JSON with metadata, counts, lookup maps, preserved entities, warnings, and safety flags.
- Task 4.2 is complete. `scripts/validate_gtm_container.py` can validate JSON parsing, expected GTM sections, tag trigger references, folder references, and detectable variable references.
- Task 4.3 is the next recommended task.
