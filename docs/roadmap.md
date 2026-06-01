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

## Goal

Define the GTM Container Audit & Patch Package artifact contracts before building intelligence, validators, scripts, fixtures, recipes, API connectors, or workflow automation.

## Tasks

### Task 1.1 - Create `gtm_patch_package.schema.json`

Status: Complete.

Outcome:
Defines the top-level machine-readable contract for the full GTM Container Audit & Patch Package, ensuring every MLP run can be represented as a consistent, schema-valid package that includes optimized container output, audit findings, change log, validation results, QA guidance, run metadata, and human-review requirements.

### Task 1.2 - Create `gtm_audit_report.schema.json`

Status: Upcoming.

Outcome:
Defines the machine-readable audit report contract for the GTM Container Audit & Patch Package, ensuring future agents, validators, tests, and automation workflows can consume structured audit findings with consistent container summary data, severity, category, affected entities, evidence, recommended actions, automated-change indicators, and manual-review requirements.
