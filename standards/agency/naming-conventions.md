# Agency Naming Conventions

## Purpose

These default agency standards define how GTM tags, triggers, variables, folders, and recipes should be named for the GTM Container Audit & Patch Package.

They are reusable agency standards for future Custom GPT knowledge files and Skill references. They support audit findings and proposed changes, but they do not make generated GTM JSON safe to publish. All generated GTM artifacts remain draft proposals that require human analyst review before import, workspace creation, publishing, or production use.

## General Rules

- Names should be scannable in GTM without opening the entity.
- Names should start with the platform, entity purpose, or variable type.
- Names should use ` - ` as the main separator.
- Names should use title case for human-readable labels unless the value is a literal event name, dataLayer key, or code identifier.
- Names should not hide uncertainty. If the system cannot infer a purpose, it should flag the entity for manual review instead of inventing a polished name.
- Naming cleanup must not change dataLayer event names, ecommerce parameter names, vendor IDs, trigger conditions, tag payloads, consent settings, or live GTM configuration.

## Tag Naming

Pattern:

```text
{Platform} - {Tag Type} - {Purpose or Event}
```

Examples:

- `GA4 - Event - purchase`
- `Google Ads - Conversion - Lead Form Submit`
- `Meta - Pixel - PageView`
- `LinkedIn - Insight - Lead`
- `Hotjar - Base - Sitewide`

Anti-examples:

- `tag 1`
- `GA4`
- `conversion`
- `pixel new`
- `DO NOT DELETE`

Rules:

- Use the vendor or platform as the first segment.
- Use a tag type that explains what the tag does, such as `Event`, `Config`, `Conversion`, `Pixel`, `Base`, or `Remarketing`.
- Use the business event, page type, or conversion name as the final segment.
- Do not encode implementation uncertainty as if it were known. Use a finding instead.

Audit support:

- Rule ID: `NAME-TAG-001`
- A future audit finding may cite this rule when a tag name does not identify platform, tag type, and purpose.
- Evidence should include the tag ID, current tag name, detected vendor or tag type, and the proposed replacement name.

## Trigger Naming

Pattern:

```text
{Trigger Type Prefix} - {Condition or Event}
```

Default prefixes:

- `PV` for page view triggers.
- `CE` for custom event triggers.
- `Click` for click triggers.
- `Form` for form submission triggers.
- `Timer` for timer triggers.
- `Scroll` for scroll depth triggers.
- `YT` for YouTube video triggers.

Examples:

- `CE - purchase`
- `PV - All Pages`
- `Click - CTA - Header Demo`
- `Form - Lead - Contact Us`
- `Scroll - 75 Percent`

Anti-examples:

- `trigger 1`
- `all`
- `click`
- `event`
- `purchase tag trigger`

Rules:

- The trigger name should describe the trigger condition, not the tag that uses it.
- Custom event trigger names may include the literal event name, but naming cleanup must not change the event value itself.
- Page view trigger names should identify the page scope, such as `All Pages`, `Checkout`, or `Blog`.
- Click trigger names should identify the interaction target and placement when known.

Audit support:

- Rule ID: `NAME-TRIGGER-001`
- A future audit finding may cite this rule when a trigger name does not identify trigger type and condition.
- Evidence should include trigger ID, current trigger name, trigger type, key filter values, and proposed replacement name.

## Variable Naming

Pattern:

```text
{Variable Type Prefix} - {Value or Purpose}
```

Default prefixes:

- `DLV` for data layer variables.
- `CONST` for constant variables.
- `JS` for custom JavaScript variables.
- `REGEX` for regular expression table variables.
- `LOOKUP` for lookup table variables.
- `1P` for first-party cookie variables.
- `URL` for URL variables.
- `DOM` for DOM element variables.

Examples:

- `DLV - ecommerce.transaction_id`
- `CONST - GA4 Measurement ID`
- `JS - normalize phone`
- `REGEX - paid traffic source`
- `LOOKUP - event name to conversion label`

Anti-examples:

- `var 1`
- `dl`
- `id`
- `custom js`
- `test variable`

Rules:

- Use the variable type prefix as the first segment.
- Keep literal dataLayer keys and parameter names exact, including case and punctuation.
- Do not rename a variable if the name is referenced as text in Custom HTML, templates, external documentation, or client QA instructions without manual review.
- Naming cleanup must not change the variable value, dataLayer key, cookie name, selector, JavaScript code, or lookup behavior.

Audit support:

- Rule ID: `NAME-VARIABLE-001`
- A future audit finding may cite this rule when a variable name does not identify variable type and purpose.
- Evidence should include variable ID, current variable name, variable type, referenced key or purpose, and proposed replacement name.

## Folder Naming

Pattern:

```text
{Area or Platform} - {Grouping Purpose}
```

Examples:

- `GA4 - Core Measurement`
- `Ads - Conversion Tracking`
- `Consent - Review Required`
- `QA - Temporary Review`
- `Archive - Do Not Use`

Anti-examples:

- `folder`
- `misc`
- `old`
- `new stuff`
- `client`

Rules:

- Folder names should describe why entities are grouped.
- Folder names should not imply an entity is safe or approved unless a human analyst has confirmed that status.
- Use `Consent - Review Required` for groupings that need consent or privacy review.
- Use `Archive - Do Not Use` only when the folder is clearly for inactive or deprecated entities; do not delete entities as a naming cleanup.

Audit support:

- Rule ID: `NAME-FOLDER-001`
- A future audit finding may cite this rule when folder names are vague, misleading, or inconsistent.
- Evidence should include folder ID, folder name, grouped entity examples, and proposed replacement name.

## Recipe Naming

Pattern:

```text
{Platform or Pattern} - Recipe - {Use Case}
```

Examples:

- `GA4 - Recipe - Ecommerce Purchase`
- `Google Ads - Recipe - Lead Form Conversion`
- `Consent - Recipe - Ads Gating`
- `QA - Recipe - Preview Checklist`

Anti-examples:

- `recipe`
- `setup`
- `tracking`
- `client recipe`

Rules:

- Recipe names are placeholders for future reusable implementation patterns.
- A recipe name should identify the platform or pattern and the use case.
- Recipes must not be treated as complete GTM containers.
- Recipe naming can be audited, but recipe implementation belongs to a later phase.

Audit support:

- Rule ID: `NAME-RECIPE-001`
- A future audit finding may cite this rule when a recipe name is too vague for reuse.
- Evidence should include recipe name, intended use case if known, and proposed replacement name.

## Safe Rename Guidance

A proposed rename is usually low risk when all of the following are true:

- The change is name-only.
- The GTM entity ID and configuration remain unchanged.
- The proposed name follows the relevant standard above.
- There is no evidence that the name is referenced as text in Custom HTML, custom templates, external documentation, QA instructions, or client reporting workflows.
- The rename does not change dataLayer keys, event values, selectors, vendor IDs, consent settings, or payload fields.

For low-risk name-only changes, the MLP may propose the rename in `change_log.json` and reflect it in `optimized_container.json`, but the change still requires human analyst review before import or production use.

## Manual-Review Rename Guidance

A proposed rename requires manual review when any of the following are true:

- The entity is a Custom HTML tag, custom template, or custom JavaScript variable.
- The name may be referenced as text in Custom HTML, documentation, QA scripts, or client reports.
- The entity is related to consent, advertising, remarketing, enhanced conversions, user identifiers, or sensitive data.
- The proposed rename is inferred from partial evidence.
- The existing name contains warnings such as `do not delete`, `legacy`, `hold`, `legal`, `consent`, `privacy`, `client approved`, or `vendor managed`.
- The rename might be confused with changing a dataLayer event name, ecommerce parameter, trigger condition, or tag payload.

Manual-review rename findings should state what is known, what is inferred, and what a human analyst must verify.

## Audit Finding Requirements

When the GTM Container Audit & Patch Package flags a naming issue, the finding should include:

- Rule ID from this standard.
- Affected entity type.
- Affected entity ID, if available.
- Current name.
- Proposed name or naming pattern.
- Evidence used to infer platform, type, or purpose.
- Risk level.
- Whether the proposed change is name-only.
- Whether manual review is required.
- Related proposed change ID, if a change is included in `change_log.json`.

## Automated Change Policy

- Allowed candidate: low-risk name-only cleanup with clear evidence and no manual-review trigger.
- Manual-review only: ambiguous names, consent-sensitive entities, Custom HTML, custom templates, custom JavaScript variables, or names with client/vendor warnings.
- Blocked in Phase 2: live GTM renaming, API writes, publishing, deleting entities, changing trigger logic, changing variable values, changing tag payloads, or claiming naming validation proves tracking correctness.
