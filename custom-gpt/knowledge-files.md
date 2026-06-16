# Custom GPT Knowledge Files

## Status

Task 6.3 knowledge file selection is complete.

This file is the repo source of truth for the approved Custom GPT knowledge upload set. Upload status and completed manual GPT verification are recorded in `custom-gpt/task-6.3-verification.md`.

## Selection rules

- Use only MLP-relevant, repo-versioned files.
- Use concise, text-forward reference files.
- Because `custom-gpt/instructions.md` exceeds the GPT Instructions field limit, upload it as a knowledge file and explicitly reference it from the GPT Instructions field.
- Keep the GPT Instructions field short: it should point to `custom-gpt/instructions.md` as the source of truth for core behavior and preserve the MLP safety boundaries.
- Do not upload hidden, non-repo knowledge.
- Do not upload large raw documentation dumps.
- Do not upload API connector, GPT Action, web browsing, capability, or conversation-starter material for Task 6.3.
- Do not imply generated GTM artifacts are safe to publish.
- Do not treat `optimized_container.json` as the whole deliverable.

## Approved knowledge upload set

| File                                                              | Purpose                                                                                                                                                                                                |
| ----------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `custom-gpt/instructions.md`                                      | Provides the full core GPT behavior instructions. This file is uploaded as knowledge because it exceeds the GPT Instructions field limit, and the GPT Instructions field must explicitly reference it. |
| `docs/mlp-deliverable.md`                                         | Defines the canonical **GTM Container Audit & Patch Package**, required inputs, seven required outputs, package behavior, and MLP non-goals.                                                           |
| `docs/decisions/ADR-0001-canonical-mlp-deliverable.md`            | Records the accepted decision that the MLP produces the full package, not optimized GTM JSON alone.                                                                                                    |
| `docs/glossary.md`                                                | Provides shared terminology for MLP, GTM exports, optimized containers, manual review, Custom GPT, Skill, validation, fixtures, and related concepts.                                                  |
| `skills/gtm-container-auditor/references/deliverable-contract.md` | Provides the compact Skill-facing package contract, completion rule, and safety rule.                                                                                                                  |
| `skills/gtm-container-auditor/references/workflow.md`             | Defines the file-in/file-out execution workflow, output assembly rules, validation boundaries, QA boundaries, and stopping conditions.                                                                 |
| `skills/gtm-container-auditor/references/output-standards.md`     | Defines report structure, severity labels, uncertainty handling, artifact alignment, and disallowed claims.                                                                                            |
| `skills/gtm-container-auditor/references/audit-rules.md`          | Provides audit rule IDs, severity guidance, automated-change policy values, evidence requirements, and manual-review triggers.                                                                         |
| `skills/gtm-container-auditor/references/gtm-object-model.md`     | Summarizes GTM entity types, relationships, reference-integrity checks, and manual-review boundaries.                                                                                                  |
| `skills/gtm-container-auditor/references/client-overrides.md`     | Defines how to apply client profiles, overrides, and current-run user instructions without weakening package or safety requirements.                                                                   |
| `standards/agency/naming-conventions.md`                          | Defines agency naming conventions and safe/manual-review rename guidance for GTM entities.                                                                                                             |
| `standards/agency/consent-standard.md`                            | Defines consent and privacy risk review standards, manual-review triggers, blocked automation, and approved wording.                                                                                   |
| `standards/agency/qa-standard.md`                                 | Defines human QA checklist structure, evidence expectations, status language, and QA categories.                                                                                                       |

## Files intentionally excluded from Task 6.3 knowledge

| File or area                                                                                                        | Reason                                                                                                                      |
| ------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| `custom-gpt/instructions-draft.md`                                                                                  | Superseded draft retained for project history.                                                                              |
| `custom-gpt/conversation-starters.md`                                                                               | Belongs to Task 6.5.                                                                                                        |
| `custom-gpt/test-prompts.md`                                                                                        | Testing aid, not runtime MLP reference knowledge.                                                                           |
| `custom-gpt/task-6.1-verification.md`, `custom-gpt/task-6.2-verification.md`, `custom-gpt/task-6.3-verification.md` | Verification records, not GPT knowledge.                                                                                    |
| `docs/tasks/`                                                                                                       | Project task-management docs, not runtime MLP reference knowledge.                                                          |
| `README.md` and `CHANGELOG.md`                                                                                      | Repository status/history docs, not runtime MLP reference knowledge.                                                        |
| `schemas/*.json`                                                                                                    | Machine-readable contracts, but not concise text-forward knowledge for Task 6.3.                                            |
| `skills/gtm-container-auditor/schemas/*.json`                                                                       | Mirrored schema contracts excluded for the same reason as root schemas.                                                     |
| `examples/`                                                                                                         | Fixtures and expected outputs are testing assets, not initial GPT knowledge.                                                |
| `scripts/`                                                                                                          | Deterministic local tooling, not Custom GPT knowledge.                                                                      |
| `skills/gtm-container-auditor/recipes/`                                                                             | Optional recipe patterns are not required for Task 6.3 knowledge and may imply implementation behavior beyond the core MLP. |
| GPT Actions, API connector docs, live-platform setup notes, or web-browsing material                                | Out of scope for Task 6.3 and the MLP wrapper.                                                                              |

## Applied standards answer requirement

After the approved knowledge files are uploaded, the GPT should be able to answer which standards and references it applies. A passing answer should include the same source paths and should distinguish:

- Canonical deliverable contract.
- Workflow and output standards.
- Audit rule catalog.
- GTM object model reference.
- Client override rules.
- Agency naming, consent/privacy, and QA standards.

The GPT should also state that all generated GTM artifacts are draft proposals requiring human review before import, workspace creation, publishing, or production use.
