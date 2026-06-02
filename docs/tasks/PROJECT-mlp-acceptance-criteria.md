# MLP Acceptance Criteria

## Status

Planning reference

## Purpose

Define the high-level acceptance criteria for the full GTM Container Audit & Patch Package MLP.

## Functional

- User can upload a GTM container export JSON.
- System produces a GTM Container Audit & Patch Package.
- Package includes optimized container JSON, audit report, audit JSON, change log, validation report, QA checklist, and metadata.

## Quality

- Outputs are consistent across repeated runs.
- Findings include evidence and affected entities.
- Changes are reversible or clearly marked for manual review.
- Custom HTML and advertising or consent-sensitive tags are flagged.

## Validation

- JSON outputs parse.
- Output artifacts conform to schemas.
- Change log matches the difference between original and optimized JSON.
- Validator catches at least one intentionally broken fixture.

## Safety

- System does not claim changes are safe to publish.
- System does not recommend live deployment without human review.
- Deletions are avoided unless explicitly requested.
- No live API actions are configured for the MLP.

## Portability

- Repo contains prompts, standards, schemas, scripts, fixtures, and Skill files needed to recreate the workflow.
- Skill can be packaged and moved.
- Custom GPT instructions are stored in the repo.
- Another instance can be recreated from the repo.
