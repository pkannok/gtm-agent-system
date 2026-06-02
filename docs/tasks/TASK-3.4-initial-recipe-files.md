# Task 3.4 - Add initial recipe files

## Status

Complete

## Goal

Create initial reusable recipe files for common GTM cleanup or tracking patterns.

## How it fits

Recipes let the system propose consistent implementation patterns without hard-coding one-off prompt behavior.

## In scope

- Create `skills/gtm-container-auditor/recipes/ga4-basic-cleanup.yaml`.
- Create `skills/gtm-container-auditor/recipes/google-ads-conversion-basic.yaml`.
- Document when each recipe applies.
- Include risk and manual-review notes.
- Include required recipe fields: `recipe_id`, `version`, `platform`, `target`, `purpose`, `requires`, `recommended_parameters`, `manual_review`, `outputs`, and `qa_steps`.
- Keep recipe changes proposed and reversible.

## Out of scope

- Large recipe catalog.
- Automated live implementation.
- Publishing or workspace writes.
- Vendor-specific API connectors.

## Definition of done for MLP

- [x] Initial recipe files exist.
- [x] Each recipe states its purpose and when it applies.
- [x] Each recipe includes risk and manual-review guidance.
- [x] Each recipe includes required inputs, outputs, recommended parameters, manual-review flags, and QA guidance.
- [x] Recipes do not imply live GTM changes.
