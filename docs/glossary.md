# Glossary

This glossary defines project-specific terms for the GTM Container Audit & Patch Package system.

## GTM Container Audit & Patch Package

Definition:
The canonical MLP deliverable for this project.

Project usage:
The complete file-in/file-out package produced from a GTM container export and optional standards.

Not to be confused with:
`optimized_container.json` alone, a live GTM workspace, or a publish-ready GTM version.

## MLP

Definition:
Minimum lovable product.

Project usage:
The first MLP is the file-in/file-out GTM Container Audit & Patch Package.

Not to be confused with:
An optimized JSON-only output or production automation.

## GTM container

Definition:
A Google Tag Manager container that contains tags, triggers, variables, folders, templates, and related configuration.

Project usage:
The source object being audited by the MLP.

Not to be confused with:
A live GTM workspace or a published GTM version.

## GTM container export

Definition:
A JSON file exported from Google Tag Manager that represents a container or workspace configuration.

Project usage:
The required input for the file-in/file-out MLP.

Not to be confused with:
A direct API connection to GTM.

## Workspace

Definition:
A GTM editing context where changes can be prepared before versioning or publishing.

Project usage:
Out of scope for the MLP. Later versions may create pre-production workspaces after human approval.

Not to be confused with:
The file-based optimized container produced by the MLP.

## Optimized container

Definition:
A complete proposed GTM container export JSON after the system applies cleanup or improvement recommendations.

Project usage:
Represented by `optimized_container.json`.

Not to be confused with:
A publish-ready or production-safe GTM container.

## `optimized_container.json`

Definition:
The required output JSON artifact containing proposed reviewable optimizations.

Project usage:
One artifact in the GTM Container Audit & Patch Package.

Not to be confused with:
The full deliverable, a live GTM change, or a file that is safe to publish without human approval.

## Audit

Definition:
A structured review of a GTM container export to identify issues, risks, inconsistencies, and improvement opportunities.

Project usage:
One of the main activities performed by the MLP.

Not to be confused with:
A legal, privacy, or compliance certification.

## Finding

Definition:
A specific issue, risk, inconsistency, or improvement opportunity identified during an audit.

Project usage:
Findings appear in `audit_report.md` and `audit_report.json`.

Not to be confused with:
A proposed change. A finding explains the issue; a proposed change explains what to do about it.

## Evidence

Definition:
The observed facts that support a finding.

Project usage:
Evidence should reference affected GTM entities, names, IDs, settings, or structural patterns.

Not to be confused with:
Assumptions or guesses.

## Proposed change

Definition:
A recommended modification to the GTM container export.

Project usage:
Proposed changes are tracked in `change_log.json` and may be applied to `optimized_container.json`.

Not to be confused with:
A live GTM change.

## Patch

Definition:
A proposed file-based set of changes represented by the optimized container and change log.

Project usage:
The MLP patch is not a live API mutation.

Not to be confused with:
A direct GTM API update or workspace publish.

## Change log

Definition:
A machine-readable list of differences between the source GTM export and `optimized_container.json`.

Project usage:
Stored in `change_log.json`.

Not to be confused with:
A human-readable audit summary.

## Validation report

Definition:
A machine-readable report describing whether the output package and GTM-like JSON structure passed defined checks.

Project usage:
Stored in `validation_report.json`.

Not to be confused with:
Proof that the container is safe to publish.

## Human-readable artifact

Definition:
An output intended for analyst reading and decision-making.

Project usage:
Examples include `audit_report.md` and `qa_checklist.md`.

Not to be confused with:
Machine-readable JSON artifacts or human approval.

## Machine-readable artifact

Definition:
An output intended for tools, validators, future agents, dashboards, or tests.

Project usage:
Examples include `audit_report.json`, `change_log.json`, `validation_report.json`, and `run_metadata.json`.

Not to be confused with:
Narrative analyst documentation or proof that changes are safe.

## QA checklist

Definition:
A human-readable checklist for analyst review and manual GTM preview/testing.

Project usage:
Stored in `qa_checklist.md`.

Not to be confused with:
Automated validation.

## Run metadata

Definition:
Machine-readable information about a specific MLP run.

Project usage:
Stored in `run_metadata.json`.

Not to be confused with:
Audit findings or validation results.

## Client profile

Definition:
A structured file that captures client-specific standards, preferences, and overrides.

Project usage:
Optional input for the MLP and future workflows.

Not to be confused with:
Agency-wide standards.

## Client override

Definition:
A client-specific rule that changes or narrows the default agency standard.

Project usage:
Client overrides take precedence over agency defaults when explicitly provided.

Not to be confused with:
A one-off user instruction unless the user explicitly says it should become reusable.

## Agency standard

Definition:
A default rule, convention, or best practice used across clients.

Project usage:
Used when no client override exists.

Not to be confused with:
Platform vendor documentation.

## Recipe

Definition:
A reusable implementation pattern for a tracking or analytics task.

Project usage:
Future phases may use recipes to generate or validate GTM changes.

Not to be confused with:
A complete GTM container.

## Manual review

Definition:
A required human inspection before trusting or using a recommendation.

Project usage:
Required for risky changes, Custom HTML, consent-sensitive tags, and uncertain findings.

Not to be confused with:
Human approval for a live or pre-production write action.

## Human approval

Definition:
An explicit human decision to allow a risky or future write action.

Project usage:
Required in later phases before creating pre-production GTM workspaces or making API-backed changes.

Not to be confused with:
General manual review.

## Publish

Definition:
The GTM action that makes a container version live.

Project usage:
The MLP does not publish GTM changes or claim outputs are safe to publish.

Not to be confused with:
Producing `optimized_container.json`.

## Pre-production change

Definition:
A change prepared before going live, such as a future GTM workspace update.

Project usage:
Out of scope for the MLP but relevant to later architecture.

Not to be confused with:
Publishing.

## File-in/file-out workflow

Definition:
A workflow where the user provides files as input and receives files or file-like artifacts as output.

Project usage:
The MLP workflow.

Not to be confused with:
Direct API access to GTM, GA4, or Google Ads.

## Custom GPT

Definition:
A configured ChatGPT experience with fields such as name, description, conversation starters, instructions, knowledge, capabilities, and optional actions.

Project usage:
The user-facing interface for the MLP.

Not to be confused with:
The repository system of record.

## Skill

Definition:
A reusable bundle of instructions and files with a `SKILL.md` manifest.

Project usage:
The future portable workflow package for GTM container audit behavior.

Not to be confused with:
A full application or live API connector.

## Validator

Definition:
A deterministic tool or process that checks structure, required files, references, or schema compliance.

Project usage:
Future phases will add validators.

Not to be confused with:
The model’s reasoning or a human analyst’s judgment.

## Fixture

Definition:
A controlled sample input used for testing.

Project usage:
Future phases will create GTM container fixtures with known issues.

Not to be confused with:
A real client container.

## Golden test

Definition:
A test with expected outputs used to detect regressions.

Project usage:
Future phases will compare system outputs against expected findings.

Not to be confused with:
A one-time manual review.
