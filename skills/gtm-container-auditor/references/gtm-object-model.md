# GTM Object Model Reference

## Purpose

This reference summarizes the GTM object types and relationships the `gtm-container-auditor` Skill needs for the **GTM Container Audit & Patch Package** MLP.

Use it to inspect a GTM container export JSON, describe evidence, and reason about proposed file-based changes. Do not use it as a claim that the MLP can verify live GTM behavior, publish changes, or replace human QA.

## Contents

- Container-level objects
- Entity types
- Relationship map
- Reference integrity checks
- Manual-review boundaries

## Container-Level Objects

A GTM container export may include:

- Container metadata, such as account ID, container ID, container name, export format version, and public ID.
- Tags.
- Triggers.
- Variables.
- Folders.
- Templates.
- Zones.
- Built-in variables.
- Consent settings or consent-related configuration when present.

Not every export includes every section. Missing or malformed sections should be recorded as audit limitations, not silently filled with guesses.

## Entity Types

### Tags

Tags define tracking or vendor behavior. They may reference triggers, variables, templates, consent settings, sequencing, and tag parameters.

Inspect:

- Tag ID and name.
- Tag type or template signal.
- Firing trigger references.
- Blocking trigger references.
- Parameters and variable references.
- Consent settings when present.
- Sequencing and setup/teardown relationships when present.

Manual review is required for Custom HTML, custom templates, advertising tags, remarketing tags, enhanced conversions, user identifiers, sensitive data, and ambiguous vendor behavior.

### Triggers

Triggers define when tags fire. They may reference variables, built-in variables, filter conditions, event names, page conditions, click conditions, form conditions, timers, or other trigger-specific configuration.

Inspect:

- Trigger ID and name.
- Trigger type.
- Event name or firing condition.
- Filter variables and operators.
- References to variables or built-in variables.
- Scope, such as all pages, selected pages, custom event, click, form, timer, or scroll.

Do not change trigger logic in the MLP unless the active task explicitly permits it. Trigger edits can alter production behavior and require manual review.

### Variables

Variables provide values used by tags, triggers, templates, and other variables. They may represent dataLayer keys, constants, URLs, cookies, custom JavaScript, lookup tables, regex tables, or DOM values.

Inspect:

- Variable ID and name.
- Variable type.
- Referenced dataLayer key, cookie name, URL component, selector, or code body.
- Whether other entities reference it.
- Whether it appears to carry user identifiers, contact fields, ecommerce values, or consent-sensitive data.

Name-only cleanup may be low risk when evidence is clear, but changing variable values, keys, code, lookup behavior, or selectors is manual-review only for the MLP.

### Folders

Folders group GTM entities for organization. They usually do not control firing behavior.

Inspect:

- Folder ID and name.
- Entities assigned to the folder.
- Whether folder names imply status, approval, consent, archive, or ownership.

Folder rename proposals should use neutral review-status wording and must not imply production readiness or publish approval.

### Templates

Templates define reusable tag or variable behavior. They can hide meaningful implementation details and may include permissions, code, vendor endpoints, or data access patterns.

Inspect:

- Template ID and name.
- Tags or variables using the template.
- Vendor or platform signal.
- Permissions and visible data access patterns when available in the export.

Template edits are out of scope for the MLP. Template-related findings should require manual review.

### Zones

Zones can constrain or delegate container behavior when present. They may affect where tags can fire or what linked containers can do.

Inspect:

- Zone ID and name.
- Boundaries, linked containers, and trigger conditions when present.
- Related tags or configuration restrictions.

Zone changes are manual-review only in the MLP.

## Relationship Map

Use these relationships when gathering evidence:

- Tags fire on trigger references.
- Tags may be blocked by blocking trigger references.
- Tags may include variable references in parameters.
- Tags may use custom templates.
- Triggers may reference variables or built-in variables in filter conditions.
- Variables may reference dataLayer keys, cookies, URLs, custom code, lookup tables, or other variables.
- Folders group tags, triggers, and variables but usually do not determine firing.
- Templates may be referenced by tags or variables.
- Consent settings may be attached to tags, triggers, or consent-related entities depending on the export.

When a relationship is inferred rather than directly observed, label it as an inference in `audit_report.md` and `audit_report.json`.

## Reference Integrity Checks

For each referenced entity:

- Confirm the referenced ID or name exists in the export.
- Record the source entity, reference location, referenced target, and whether the target was found.
- Flag unresolved or ambiguous references under `GTM-REF-001`.
- Treat reference repair as manual-review only unless a later task authorizes deterministic repair.

Reference integrity checks do not prove that live tracking works. They only inspect the exported configuration.

## Manual-Review Boundaries

Require manual review when an object or relationship involves:

- Custom HTML or custom templates.
- Custom JavaScript variables.
- Advertising or remarketing vendors.
- Enhanced conversions.
- User identifiers, email, phone, address, or other sensitive data signals.
- Ecommerce purchase, value, currency, item, or transaction ID mappings.
- Consent settings or consent-sensitive firing behavior.
- Trigger logic changes.
- Variable value, code, selector, dataLayer key, or lookup behavior changes.
- Deletion, disabling, or archive decisions.
- Any object whose meaning is inferred from partial evidence.
