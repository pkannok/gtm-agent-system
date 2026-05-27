# Architecture

## Current Architecture

The project is a portable file-in/file-out Custom GPT + Skill workflow.

The repository is the source of truth for project decisions, deliverable definitions, roadmap, task scope, and reusable reference material. The Custom GPT is treated as a user interface that should be recreatable from version-controlled files.

## Current Boundaries

Task 0.2 only establishes repository structure and source-of-truth documentation. Schemas, validators, scripts, fixtures, API connectors, GitHub Actions, production scripts, live API actions, and the full Skill implementation are deferred to later tasks.

## Core Package

The first MLP deliverable is the GTM Container Audit & Patch Package. Its canonical contract is documented in `docs/mlp-deliverable.md` and `skills/gtm-container-auditor/references/deliverable-contract.md`.

