# Changelog

All notable project changes will be documented in this file.

## Unreleased

### Added

- Defined the canonical MLP deliverable as **GTM Container Audit & Patch Package**.
- Added project roadmap.
- Marked Phase 0 complete after defining the canonical deliverable, repository foundation, and project terminology.
- Added `docs/glossary.md` with project terminology for GTM concepts, artifact concepts, Custom GPT concepts, Skill concepts, and future validation/testing concepts.
- Added Codex guidance through `AGENTS.md`.
- Added task-brief workflow under `docs/tasks/`.
- Added initial placeholders for future Custom GPT configuration files.
- Added initial placeholder structure for the future `gtm-container-auditor` Skill.
- Added the Phase 1 schema layer under `schemas/`.
- Added `schemas/gtm_patch_package.schema.json` as the top-level JSON Schema contract for the full GTM Container Audit & Patch Package.
- Added `schemas/gtm_audit_report.schema.json` for machine-readable audit findings.
- Added `schemas/gtm_change_log.schema.json` for proposed GTM change logs.
- Added `schemas/validation_report.schema.json` for package validation summaries.
- Added `schemas/client_profile.schema.json` for optional client-specific standards and overrides.
- Added matching minimal sample files under `examples/schema-validation/` for all five Phase 1 schemas.

### Changed

- Updated `docs/tasks/CURRENT.md`, `docs/roadmap.md`, and `README.md` to reflect Phase 1 completion.
- Moved the top-level package schema contract from the repository root to `schemas/` so all Phase 1 schema contracts live together.
- Kept `schemas/` contract-only and placed schema validation samples under `examples/schema-validation/`.
