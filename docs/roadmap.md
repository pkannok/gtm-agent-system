# Roadmap

## Canonical MLP deliverable

The canonical MLP deliverable is:

**GTM Container Audit & Patch Package**

It is a file-in/file-out package produced from a GTM container export JSON. It must include `optimized_container.json`, but it must not treat that JSON as the only deliverable.

A complete MLP output package includes:

1. `optimized_container.json`
2. `audit_report.md`
3. `audit_report.json`
4. `change_log.json`
5. `validation_report.json`
6. `qa_checklist.md`
7. `run_metadata.json`

---

# Phase 0 — Project framing and repository setup

Status: Complete.

## Goal

Create the durable project foundation before building schemas, scripts, fixtures, the full Skill, or the Custom GPT configuration.

## Tasks

### Task 0.1 — Define the canonical MLP deliverable

Status: Complete.

Outcome:
The project has defined the canonical MLP deliverable as **GTM Container Audit & Patch Package**.

### Task 0.2 — Create the portable project repository

Status: Complete.

Outcome:
The repository will become the system of record for project documentation, task briefs, future Custom GPT drafts, future Skill files, and output package definitions.

### Task 0.3 — Define project terminology

Status: Complete.

Outcome:
The project will have a shared glossary for GTM concepts, artifact concepts, Custom GPT concepts, Skill concepts, and future validation/testing concepts.

---

# Phase 1 — Output contracts and schemas

Status: Complete.

## Goal

Define the GTM Container Audit & Patch Package artifact contracts before building intelligence, validators, scripts, fixtures, recipes, API connectors, or workflow automation.

## Tasks

### Task 1.1 - Create `gtm_patch_package.schema.json`

Status: Complete.

Outcome:
Defines the top-level machine-readable contract for the full GTM Container Audit & Patch Package, ensuring every MLP run can be represented as a consistent, schema-valid package that includes optimized container output, audit findings, change log, validation results, QA guidance, run metadata, and human-review requirements.

### Task 1.2 - Create `gtm_audit_report.schema.json`

Status: Complete.

Outcome:
Defines the machine-readable audit report contract for the GTM Container Audit & Patch Package, ensuring future agents, validators, tests, and automation workflows can consume structured audit findings with consistent container summary data, severity, category, affected entities, evidence, recommended actions, automated-change indicators, and manual-review requirements.

### Task 1.3 - Create `gtm_change_log.schema.json`

Status: Complete.

Outcome:
Defines the machine-readable proposed change log contract for the GTM Container Audit & Patch Package, including proposed change IDs, affected GTM entities, reasons, risk levels, rollback notes, related findings, and human-approval requirements.

### Task 1.4 - Create `validation_report.schema.json`

Status: Complete.

Outcome:
Defines the machine-readable validation report contract for the GTM Container Audit & Patch Package, including validation status, checks, errors, warnings, and explicit publish-safety fields.

### Task 1.5 - Create `client_profile.schema.json`

Status: Complete.

Outcome:
Defines the optional client profile contract for client-specific standards, overrides, consent requirements, and manual-review rules.

---

# Phase 2 - Agency standards and audit rules

Status: In Progress.

## Goal

Define the agency standards and audit rules that teach the GTM Container Audit & Patch Package workflow what "good" looks like for GTM organization, naming, consent-sensitive review, audit findings, and human-readable reporting.

## Tasks

### Task 2.1 - Create agency naming conventions

Status: Complete.

Outcome:
Defines default naming standards for GTM tags, triggers, variables, folders, and recipes, including examples, anti-examples, safe rename guidance, manual-review rename guidance, and audit-finding requirements.

### Task 2.2 - Create consent and privacy review standard

Status: Upcoming.

Outcome:
Will define consent and privacy review standards for advertising, remarketing, Custom HTML, enhanced conversions, user identifiers, and sensitive data.

### Task 2.3 - Create GTM audit rule catalog

Status: Upcoming.

Outcome:
Will define initial GTM audit rules with rule IDs, evidence requirements, severity guidance, recommended actions, automated-change policy, and manual-review triggers.

### Task 2.4 - Create output writing standard

Status: Upcoming.

Outcome:
Will define human-readable report structure, severity labels, uncertainty handling, and output writing standards for the GTM Container Audit & Patch Package.
