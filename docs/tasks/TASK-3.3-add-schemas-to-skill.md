# Task 3.3 - Add schemas to the Skill

## Status

Complete

## Goal

Make Phase 1 schema contracts available inside or from the Skill package.

## How it fits

The Skill should reference the same schema contracts used by the repository so outputs stay portable and consistent.

## In scope

- Add GTM Container Audit & Patch Package schemas to the Skill.
- Ensure schema paths are documented.
- Avoid duplicate divergent schema definitions.
- Keep the root repository schema contracts authoritative.

## Out of scope

- Creating new schema contracts beyond active scope.
- Validator scripts.
- Fixture catalogs.
- API connectors.

## Definition of done for MLP

- [x] Skill has access to all Phase 1 schemas.
- [x] Schema paths are documented in the Skill references.
- [x] No duplicate schema contract diverges from the repo source of truth.
- [x] Skill instructions reference schema-aligned outputs.
