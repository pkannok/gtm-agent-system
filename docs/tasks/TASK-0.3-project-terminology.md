# Task 0.3 — Define project terminology

## Status

Upcoming

## Goal

Create a shared project glossary so the Custom GPT, Skill, validators, scripts, analysts, and future agents use the same terms consistently.

## Background

The project combines GTM concepts, analytics implementation concepts, software artifact concepts, and agent-system concepts.

Ambiguous terms create risk. For example, an "optimized container" must not be treated as a publish-ready GTM workspace. A "patch" in the MLP means a proposed file-based change package, not a live API mutation.

## In scope

- Create `docs/glossary.md`.
- Define required project terms.
- Distinguish GTM platform terms from project artifact terms.
- Distinguish proposed artifacts from live GTM changes.
- Clarify human-readable versus machine-readable artifacts.
- Update `docs/roadmap.md` status if Task 0.3 becomes active or complete.

## Out of scope

- JSON schemas.
- Python scripts.
- Validators.
- Fixtures.
- Recipe catalog.
- Full Custom GPT setup.
- Full Skill implementation.
- API connectors.
- New architecture decisions unless a terminology decision requires one.

## Required glossary terms

At minimum, define:

- GTM container
- GTM container export
- Workspace
- Optimized container
- Audit
- Finding
- Evidence
- Proposed change
- Patch
- Change log
- Validation report
- QA checklist
- Run metadata
- Client profile
- Client override
- Agency standard
- Recipe
- Manual review
- Human approval
- Publish
- Pre-production change
- File-in/file-out workflow
- Custom GPT
- Skill
- Validator
- Fixture
- Golden test

## Glossary style

Each term should include:

```
Term

Definition:

Project usage:

Not to be confused with:
```

## Expected files changed

```text
docs/glossary.md
docs/roadmap.md
docs/tasks/CURRENT.md
AGENTS.md
```

## Definition of done

- [ ] `docs/glossary.md` exists.
- [ ] All required terms are defined.
- [ ] Definitions are project-specific and operational.
- [ ] The glossary distinguishes proposed artifacts from live GTM changes.
- [ ] The glossary says `optimized_container.json` is not a publish-ready guarantee.
- [ ] The glossary says the MLP does not publish GTM changes.
- [ ] The glossary can be referenced by future Custom GTP instructions, Skill references, schemas, validators, and analyst documentation.
