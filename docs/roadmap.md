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

Status: Complete.

## Goal

Define the agency standards and audit rules that teach the GTM Container Audit & Patch Package workflow what "good" looks like for GTM organization, naming, consent-sensitive review, audit findings, and human-readable reporting.

## Tasks

### Task 2.1 - Create agency naming conventions

Status: Complete.

Outcome:
Defines default naming standards for GTM tags, triggers, variables, folders, and recipes, including examples, anti-examples, safe rename guidance, manual-review rename guidance, and audit-finding requirements.

### Task 2.2 - Create consent and privacy review standard

Status: Complete.

Outcome:
Defines consent and privacy review standards for advertising, remarketing, Custom HTML, enhanced conversions, user identifiers, sensitive data, consent configuration evidence, manual-review criteria, and non-certification wording.

### Task 2.3 - Create GTM audit rule catalog

Status: Complete.

Outcome:
Defines initial GTM audit rules for inventory, reference integrity, duplicates, unused entities, naming, ecommerce, consent/risk, and QA, including rule IDs, evidence requirements, severity guidance, recommended actions, automated-change policy, manual-review triggers, and related output artifacts.

### Task 2.4 - Create output writing standard

Status: Complete.

Outcome:
Defines human-readable report structure, severity labels, uncertainty handling, QA checklist guidance, human approval notes, and output writing standards for the GTM Container Audit & Patch Package.

---

# Phase 3 - Build the Skill package

Status: Complete.

## Goal

Create the reusable GTM Container Auditor Skill package that stores the repeatable workflow and references repo-defined contracts, schemas, standards, and audit rules.

## Tasks

### Task 3.1 - Create the Skill directory and `SKILL.md`

Status: Complete.

Outcome:
Creates the concise Skill entrypoint with valid frontmatter, UI metadata, workflow and safety rules, and links to supporting reference files.

### Task 3.2 - Create Skill reference files

Status: Complete.

Outcome:
Adds focused reference documents for workflow, audit rules, GTM object model guidance, client overrides, deliverable contract, and output standards while keeping `SKILL.md` concise.

### Task 3.3 - Add schemas to the Skill

Status: Complete.

Outcome:
Makes Phase 1 schema contracts available from the Skill without creating divergent schema definitions.

### Task 3.4 - Add initial recipe files

Status: Complete.

Outcome:
Adds initial reusable recipe files for MLP-safe GTM cleanup or tracking patterns with risk and manual-review guidance.

---

# Phase 4 - Build deterministic scripts

Status: Complete.

## Goal

Create deterministic scripts that parse, normalize, diff, and validate GTM container exports and GTM Container Audit & Patch Package outputs.

## Tasks

### Task 4.1 - Build `normalize_gtm_export.py`

Status: Complete.

Outcome:
Builds a deterministic script that normalizes GTM container exports for repeatable analysis and diffing, including metadata, counts, lookup maps, and minimal smoke-test verification.

### Task 4.2 - Build `validate_gtm_container.py`

Status: Complete.

Outcome:
Builds a deterministic script that validates basic GTM container export structure, expected sections, and detectable tag trigger, folder, and variable references.

### Task 4.3 - Build `diff_gtm_containers.py`

Status: Complete.

Outcome:
Builds a deterministic script that compares a source GTM export and `optimized_container.json`, detects entity-level changes, and outputs a machine-readable proposed change log.

### Task 4.4 - Build `validate_output_package.py`

Status: Complete.

Outcome:
Builds a deterministic script that validates a full GTM Container Audit & Patch Package, including required artifacts, schema-backed JSON artifacts, package consistency, safety flags, and validation-report-compatible output.

---

# Phase 5 - Build synthetic fixtures and tests

Status: Complete.

## Goal

Create synthetic GTM container fixtures, expected outputs, and a manual evaluation rubric for repeatable MLP testing.

## Tasks

### Task 5.1 - Create synthetic GTM container fixtures

Status: Complete.

Outcome:
Creates six small, deterministic, synthetic GTM container export fixtures with known expected issues and no real client data.

### Task 5.2 - Create golden expected outputs

Status: Complete.

Outcome:
Creates schema-aligned expected package shapes for the synthetic fixtures, including finding summaries, change posture, validation status, risk summaries, and QA checklist coverage.

### Task 5.3 - Create manual evaluation rubric

Status: Complete.

Outcome:
Creates a manual rubric for analysts to evaluate MLP output usefulness, safety, clarity, unsafe recommendations, and fixture-output alignment.

---

# Phase 6 - Build the Custom GPT wrapper

Status: In Progress.

## Goal

Create the Custom GPT wrapper for early file-in/file-out agency use while keeping the repository and Skill as the system of record.

## Tasks

### Task 6.1 - Create Custom GPT configuration

Status: Complete.

Outcome:
Records the repo source-of-truth Custom GPT name, description, intended access, scope boundaries, GPT editor creation checklist, share/access notes, and editor verification checklist.

### Task 6.2 - Write Custom GPT instructions

Status: Complete.

Outcome:
Writes the core behavior instructions for the GTM Container Analyst Custom GPT.

### Task 6.3 - Add knowledge files to the GPT

Status: Complete.

Outcome:
Identifies and uploads MLP reference documents and standards as Custom GPT knowledge, including the `custom-gpt/instructions.md` field-limit workaround.

### Task 6.4 - Configure GPT capabilities

Status: Upcoming.

Outcome:
Configures MLP-safe GPT capabilities without live API actions.

### Task 6.5 - Create conversation starters

Status: Upcoming.

Outcome:
Creates conversation starters aligned with the file-in/file-out GTM Container Audit & Patch Package workflow.
