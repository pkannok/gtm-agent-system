# Current Task

Current active task:

- None

Next recommended task:

- Task 7.1 - Run fixture-based GPT tests

Next task brief:

- `docs/tasks/TASK-7.1-fixture-based-gpt-tests.md`

Most recent completed task brief:

- `docs/tasks/TASK-6.5-conversation-starters.md`

Most recent completed phase brief:

- `docs/tasks/PHASE-6-goal-build-custom-gpt-wrapper.md`

## Instructions for Codex

Before editing files for a future active task:

1. Read `AGENTS.md`.
2. Read this file.
3. Read the active task brief, if one is listed.
4. Summarize the task goal, expected files changed, files that should not change, and scope-creep risks.

Do not work outside the active task scope.

## Current boundaries

- Do not create knowledge-file copies, capability configuration, or conversation starters unless the active task explicitly requires them.
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
- Phase 5 is complete.

## Phase 6 progress

- Task 6.1 is complete. `custom-gpt/configuration.md`, `custom-gpt/create-gpt-checklist.md`, `custom-gpt/share-access-notes.md`, and `custom-gpt/task-6.1-verification.md` record the Custom GPT configuration, manual creation evidence, internal sharing status, and editor version-history verification.
- Task 6.2 is complete. `custom-gpt/instructions.md` stores the core GPT behavior instructions, and `custom-gpt/task-6.2-verification.md` records GPT editor copy and response-section verification.
- Task 6.3 is complete. `custom-gpt/knowledge-files.md` records the approved MLP-relevant, repo-versioned Custom GPT knowledge upload set, including the `custom-gpt/instructions.md` field-limit workaround, and `custom-gpt/task-6.3-verification.md` records completed manual upload and verification evidence.
- Task 6.4 is complete. `custom-gpt/task-6.4-verification.md` records the approved capability posture, manual GPT editor steps, and verification prompts.
- Task 6.5 is complete. `custom-gpt/conversation-starters.md` records the final starter set, and `custom-gpt/task-6.5-verification.md` records the manual editor entry and version-history verification.

## Phase 7 progress

- Not yet started.
