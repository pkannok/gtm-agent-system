# Phase 4 Goal - Build deterministic scripts

## Status

Complete

Current progress:

- Task 4.1 is complete.
- Task 4.2 is complete.
- Task 4.3 is complete.
- Task 4.4 is complete.

## Task

Complete Phase 4 of the MLP project plan in VS Code/Codex.

Phase 4 builds deterministic Python scripts that support the **GTM Container Audit & Patch Package** workflow.

Each Phase 4 task must use its own branch and pull request.

Do not complete all Phase 4 tasks on one branch.

## Goal

Create deterministic scripts that parse, normalize, diff, and validate GTM container exports and GTM Container Audit & Patch Package outputs.

## Outcome

The project can validate important package and container properties with repeatable code rather than model reasoning alone.

## Included tasks

1. Task 4.1 — Build `normalize_gtm_export.py`
2. Task 4.2 — Build `validate_gtm_container.py`
3. Task 4.3 — Build `diff_gtm_containers.py`
4. Task 4.4 — Build `validate_output_package.py`

Recommended branches:

```text
task-4.1-normalize-gtm-export
task-4.2-validate-gtm-container
task-4.3-diff-gtm-containers
task-4.4-validate-output-package
```

## Out of scope

- API connectors.
- Live GTM writes.
- Publishing.
- Non-deterministic model generation.
- Full agent orchestration.
