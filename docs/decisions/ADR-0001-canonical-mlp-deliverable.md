# ADR-0001: Canonical MLP Deliverable

## Status

Accepted

## Date

2026-05-27

## Decision

The first minimum lovable product deliverable will be called:

**GTM Container Audit & Patch Package**

The MLP will not produce only an optimized GTM JSON file. It will produce a package of human-readable and machine-readable artifacts that allow an analyst to review findings, understand proposed changes, validate the output, and perform manual QA before any GTM changes are used.

## Context

The long-term system is intended to support a suite of technical marketing analyst agents. Early versions will be file-in/file-out only. Later versions may support read-only API connections and approval-gated pre-production write actions, such as creating a GTM workspace.

The first MLP needs to create useful value quickly while establishing artifact contracts that future agents can reuse.

## Considered options

### Option 1: Optimized GTM JSON only

Pros:

- Fastest apparent output.
- Easy for a user to understand.
- Directly addresses GTM cleanup.

Cons:

- Not enough traceability.
- Hard to review safely.
- Does not explain what changed or why.
- Poor foundation for later agents.
- Higher risk of users treating the output as publish-ready.

### Option 2: GTM Container Audit & Patch Package

Pros:

- Includes optimized GTM JSON.
- Provides audit findings, change log, validation results, and QA checklist.
- Safer for analyst review.
- Better foundation for future agents.
- Supports client-specific standards and overrides.
- Creates reusable artifacts for later API and orchestration workflows.

Cons:

- Slightly more work than JSON-only output.
- Requires more consistency in file naming and report structure.

## Chosen option

Option 2: GTM Container Audit & Patch Package.

## Required output files for the MLP

The MLP package must include:

1. `optimized_container.json`
2. `audit_report.md`
3. `audit_report.json`
4. `change_log.json`
5. `validation_report.json`
6. `qa_checklist.md`
7. `run_metadata.json`

## Non-goals for the MLP

The MLP will not:

- Publish GTM changes.
- Connect directly to GTM, GA4, or Google Ads APIs.
- Claim that the optimized container is safe to publish.
- Produce optimized GTM JSON as the only deliverable.
- Delete GTM entities automatically unless a later task explicitly changes this policy.
- Replace human QA.

## Consequences

All future Custom GPT instructions, Skill references, schemas, validators, fixtures, and tests must use the same deliverable name and output file list.

The Custom GPT should describe the deliverable to users.

The Skill should reference the deliverable contract when deciding what to produce.

Future scripts and validators should validate the full package, not just `optimized_container.json`.

## Definition of done for this decision

This ADR is accepted when:

- The status is changed from `Proposed` to `Accepted`.
- The required output files are reviewed and approved.
- The same deliverable name appears in the Custom GPT instruction draft.
- The same deliverable name appears in the Skill deliverable contract.
- JSON-only output is explicitly listed as out of scope.
