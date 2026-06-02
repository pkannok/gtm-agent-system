# Task 9.2 - Build synthetic container generator

## Status

Future

## Goal

Create a CLI that generates small GTM containers with controlled problems.

## How it fits

Generated fixtures accelerate regression testing and make expected findings easier to maintain.

## In scope

- Build `tools/generate_synthetic_gtm_container.py`.
- Generate at least five fixture types.
- Include expected findings.
- Keep generated containers small and deterministic.

## Out of scope

- Blocking MLP release.
- Real client data.
- Live GTM API use.

## Definition of done for first post-MLP version

- [ ] Generates at least five fixture types.
- [ ] Each fixture includes expected findings.
- [ ] Generated containers are small and deterministic.
- [ ] Fixtures are committed to `tests/fixtures/containers`.
