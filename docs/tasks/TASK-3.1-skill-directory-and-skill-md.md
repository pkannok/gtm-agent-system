# Task 3.1 - Create the Skill directory and `SKILL.md`

## Status

Complete

## Goal

Create the reusable `gtm-container-auditor` Skill with a concise `SKILL.md` manifest and workflow entrypoint.

## How it fits

The Skill stores the portable, repeatable workflow that the Custom GPT can call into while the repository remains the system of record.

## In scope

- Create or update the Skill folder.
- Create `SKILL.md` with valid frontmatter.
- Create `agents/openai.yaml` with minimal UI metadata.
- Include concise workflow and safety rules.
- Point to supporting reference files.

## Out of scope

- Live API connectors.
- Full application orchestration.
- Packaging the Skill zip.
- Publishing GTM changes.

## Definition of done for MLP

- [x] Skill folder exists.
- [x] `SKILL.md` has valid frontmatter.
- [x] `agents/openai.yaml` exists with UI metadata.
- [x] `SKILL.md` is concise and points to supporting files.
- [x] Skill can be zipped and moved to another environment.
- [x] No placeholder/example files remain.
