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
- Added `standards/agency/naming-conventions.md` with default GTM naming standards for tags, triggers, variables, folders, and future recipes.
- Added `standards/agency/consent-standard.md` with consent and privacy risk review standards for advertising, remarketing, Custom HTML, enhanced conversions, user identifiers, and sensitive data.
- Added `skills/gtm-container-auditor/references/audit-rules.md` with initial GTM audit rule IDs, severity guidance, evidence requirements, automated-change policies, and manual-review triggers.
- Added `skills/gtm-container-auditor/references/output-standards.md` with report structure, severity labels, uncertainty handling, and human approval wording standards.
- Added `standards/agency/qa-standard.md` with human QA checklist standards for the GTM Container Audit & Patch Package.
- Added `skills/gtm-container-auditor/SKILL.md` as the concise Skill entrypoint for the GTM Container Audit & Patch Package workflow.
- Added `skills/gtm-container-auditor/agents/openai.yaml` with UI metadata for the GTM Container Auditor Skill.
- Added `skills/gtm-container-auditor/references/workflow.md` with the Skill's end-to-end file-in/file-out workflow and stopping conditions.
- Added `skills/gtm-container-auditor/references/gtm-object-model.md` with GTM entity and reference relationship guidance for audit evidence.
- Added `skills/gtm-container-auditor/references/client-overrides.md` with client profile, override, and safety-priority rules.
- Added mirrored Phase 1 schema contracts under `skills/gtm-container-auditor/schemas/` for portable Skill use.
- Added `skills/gtm-container-auditor/recipes/ga4-basic-cleanup.yaml` with optional GA4 cleanup and QA guidance.
- Added `skills/gtm-container-auditor/recipes/google-ads-conversion-basic.yaml` with optional Google Ads conversion review and QA guidance.
- Added `scripts/normalize_gtm_export.py` to produce deterministic GTM container export summary JSON with metadata, counts, lookup maps, preserved entities, warnings, and safety flags.
- Added `examples/script-smoke-tests/valid-basic-container.json` as minimal smoke-test input for Task 4.1 script verification.
- Added `scripts/validate_gtm_container.py` to validate JSON parsing, expected GTM sections, and detectable tag trigger, folder, and variable references.
- Added Task 4.2 failure fixtures under `examples/script-smoke-tests/` for broken references, missing sections, and invalid JSON.
- Added `scripts/diff_gtm_containers.py` to compare original and optimized GTM exports and output a deterministic proposed change log.
- Added `examples/script-smoke-tests/valid-basic-container-renamed.json` as optimized smoke-test input for Task 4.3 diff verification.
- Added `scripts/validate_output_package.py` to validate full GTM Container Audit & Patch Package directories and produce `validation_report.json`-compatible output.
- Added minimal Task 4.4 smoke-test output packages for valid, known-bad, and missing-file validation paths.
- Added six Task 5.1 synthetic GTM container export fixtures under `examples/synthetic-gtm-containers/` with documented expected issues and no real client data.
- Added Task 5.2 golden expected package shapes under `examples/golden-expected-outputs/` for the six synthetic fixtures.
- Added `docs/evaluation/manual-evaluation-rubric.md` for analyst review of MLP fixture outputs.
- Added `custom-gpt/configuration.md` as the repo source-of-truth Custom GPT configuration record for Task 6.1.
- Added `custom-gpt/create-gpt-checklist.md` for Task 6.1 GPT editor creation and verification.
- Added `custom-gpt/share-access-notes.md` for Task 6.1 intended internal access and sharing boundaries.
- Added `custom-gpt/task-6.1-verification.md` for non-secret manual GPT creation and verification notes.
- Added `custom-gpt/instructions.md` as the repo source-of-truth Custom GPT instructions draft for Task 6.2.
- Added `custom-gpt/task-6.2-verification.md` for non-secret manual GPT instruction-copy and response-section verification notes.
- Added `custom-gpt/knowledge-files.md` for the approved Task 6.3 Custom GPT knowledge upload set.
- Added `custom-gpt/task-6.3-verification.md` for Task 6.3 manual knowledge-upload instructions and verification notes.
- Added `custom-gpt/task-6.4-verification.md` for Task 6.4 Custom GPT capability posture, manual editor checks, and verification prompts.

### Changed

- Updated `docs/tasks/CURRENT.md`, `docs/roadmap.md`, and `README.md` to reflect Phase 1 completion.
- Marked Phase 2 complete after adding naming, consent/privacy, audit-rule, output-writing, and QA standards.
- Updated `README.md` and `docs/roadmap.md` to reflect Phase 2 completion and the upcoming Phase 3 Skill package work.
- Marked Phase 3 in progress and Task 3.1 complete.
- Marked Task 3.2 complete and updated `SKILL.md` reference navigation for the Skill reference files.
- Added contents lists and current-purpose wording to existing Skill references.
- Marked Task 3.3 complete and documented bundled Skill schema paths while preserving root schemas as the source of truth.
- Marked Task 3.4 and Phase 3 complete.
- Updated `SKILL.md` to reference optional recipes as reviewable aids, not live configuration behavior.
- Updated README, roadmap, current-task handoff, and Phase 3 goal documentation to reflect Phase 3 completion and the upcoming Phase 4 deterministic script work.
- Marked ADR-0001 accepted now that the canonical MLP deliverable decision is reflected in the project docs, Custom GPT instruction draft, and Skill deliverable contract.
- Marked Phase 4 in progress, Task 4.1 complete, and updated the README/current-task handoff after normalizer verification passed.
- Marked Task 4.2 complete after the GTM container validator passed all definition-of-done checks.
- Marked Task 4.3 complete after the GTM container diff script passed syntax, help, smoke, invalid-input, safety, and scope checks.
- Marked Task 4.4 complete after package-validator smoke checks passed.
- Marked Phase 4 complete after all four deterministic script tasks were finished.
- Marked Phase 5 in progress and Task 5.1 complete after fixture documentation and validation checks passed.
- Marked Task 5.2 complete after expected package shapes passed schema-alignment checks.
- Marked Task 5.3 and Phase 5 complete after rubric scope and safety checks passed.
- Marked Phase 6 and Task 6.1 in progress while GPT editor verification remains pending.
- Updated Task 6.1 Custom GPT configuration documentation while keeping final instructions, knowledge files, capabilities, conversation starters, and GPT Actions deferred to later tasks.
- Recorded Task 6.1 manual GPT creation, internal sharing, and GPT editor version-history verification evidence.
- Marked Task 6.1 complete after manual GPT creation, internal sharing, and GPT editor version-history verification were recorded.
- Marked Task 6.2 in progress and began the core GPT behavior instructions.
- Marked Task 6.2 complete after GPT editor instruction copy and required package-section response verification were recorded.
- Marked Task 6.3 in progress and documented the Custom GPT knowledge-file selection and pending manual verification workflow.
- Documented the Task 6.3 GPT Instructions field-limit workaround: upload `custom-gpt/instructions.md` as approved knowledge and use a short Instructions-field pointer.
- Marked Task 6.3 complete after approved knowledge files were uploaded and GPT applied-standards verification passed.
- Marked Task 6.4 ready for manual verification and documented MLP-safe Custom GPT capability settings.
- Marked Task 6.4 complete after manual capability verification passed and recorded Task 6.5 as the next recommended task.
- Moved the top-level package schema contract from the repository root to `schemas/` so all Phase 1 schema contracts live together.
- Kept `schemas/` contract-only and placed schema validation samples under `examples/schema-validation/`.
