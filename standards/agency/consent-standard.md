# Consent and Privacy Review Standard

## Purpose

This agency standard defines how the GTM Container Audit & Patch Package should flag consent-sensitive tags, triggers, variables, and proposed changes.

The MLP is a file-in/file-out review workflow. It can identify consent and privacy risk signals in a GTM container export, but it cannot verify live site behavior, certify legal compliance, certify privacy compliance, or replace human analyst, legal, privacy, or GTM Preview review.

## Core Safety Rules

- All consent and privacy findings are risk flags, not compliance certifications.
- Any advertising or remarketing vendor tag requires consent review.
- Any Custom HTML tag requires manual review.
- Any tag, variable, or template that appears to transmit email, phone, user ID, enhanced conversion data, or other sensitive data requires manual review.
- The MLP must not claim that consent is working on the live site.
- The MLP must not claim legal, privacy, or compliance certification.
- The MLP must not publish GTM changes, create GTM workspaces, or call GTM, GA4, or Google Ads APIs.
- Generated GTM artifacts remain draft proposals that require human review before import, workspace creation, publishing, or production use.

## Review Outcomes

Use these review outcomes in audit findings, proposed changes, and report text:

- `manual_review_required`: A human analyst must inspect the item before trusting or using the recommendation.
- `consent_review_required`: A human analyst must confirm consent expectations, GTM consent settings, and client policy before use.
- `blocked_for_automation`: The MLP may flag the issue but must not apply an automated proposed change.
- `low_risk_note`: The item appears low risk from file evidence, but the MLP still does not certify live behavior.

## Advertising Vendor Review Rules

Advertising vendor tags require consent review because they may set cookies, transmit identifiers, or support paid media optimization.

Examples of advertising vendors and platforms:

- Google Ads
- Google Floodlight
- Microsoft Advertising
- Meta
- LinkedIn
- TikTok
- Pinterest
- Snapchat
- X
- Reddit
- Criteo
- Amazon Ads

Flag these GTM signals:

- Tag names or types containing `Google Ads`, `Ads Conversion`, `Floodlight`, `Conversion Linker`, `Meta Pixel`, `LinkedIn Insight`, `TikTok Pixel`, or similar paid media labels.
- Custom templates for advertising vendors.
- Custom HTML that loads ad platform scripts or pixels.
- Variables that appear to hold click IDs, conversion labels, account IDs, pixel IDs, or user identifiers.

Required handling:

- Set `consent_review_required` to true.
- Require manual review before applying any proposed change.
- Do not claim that the tag is properly gated by consent.
- Evidence should include tag ID, tag name, vendor signal, tag type or template name, relevant consent settings if present, and any related trigger names.

## Remarketing Vendor Review Rules

Remarketing and audience-building tags require consent review because they may track site behavior for audience creation or ad personalization.

Flag these GTM signals:

- Tag names containing `remarketing`, `retargeting`, `audience`, `pixel`, `ad personalization`, or `conversion linker`.
- Vendor tags that fire on broad page view triggers such as `PV - All Pages`.
- Tags that combine advertising vendors with page view, scroll, video, or click behavior.
- Variables or parameters that appear to send audience, segment, product, cart, or user attributes to an ad platform.

Required handling:

- Set `consent_review_required` to true.
- Set `manual_review_required` to true.
- Treat broad all-pages remarketing as at least medium risk unless the container has clear consent gating evidence.
- Do not remove or modify remarketing tags automatically.

## Custom HTML Review Rules

Any Custom HTML tag requires manual review, even when the code appears simple.

Flag these GTM signals:

- GTM tag type is Custom HTML.
- Tag body loads external scripts.
- Tag body references cookies, local storage, session storage, URL parameters, forms, user identifiers, or dataLayer values.
- Tag body sends data with `fetch`, `XMLHttpRequest`, image pixels, script URLs, iframe URLs, or vendor endpoints.

Required handling:

- Set `manual_review_required` to true.
- Set `blocked_for_automation` to true for code edits.
- The MLP may summarize visible risk signals but must not certify what the code does.
- The MLP may recommend human code review, GTM Preview testing, network inspection, and consent verification.

Evidence should include tag ID, tag name, visible external domains, referenced variable names, code patterns observed, and any trigger names.

## Enhanced Conversions Review Rules

Enhanced conversion implementations require manual review because they may transmit hashed or transformed user-provided data.

Flag these GTM signals:

- Tag names containing `enhanced conversion`, `EC`, `user provided data`, `UPD`, `lead enhanced`, or similar labels.
- Google Ads conversion tags with enhanced conversion fields.
- Variables named for email, phone, first name, last name, address, user ID, customer ID, or normalized contact data.
- Custom JavaScript variables that normalize, hash, trim, lowercase, or otherwise transform user contact data.

Required handling:

- Set `manual_review_required` to true.
- Set `consent_review_required` to true.
- Do not claim that hashing or normalization makes the implementation compliant.
- Do not automatically add, remove, or modify enhanced conversion data fields.

Evidence should include tag ID, tag name, variable names, visible field names, transformation indicators, and the related trigger.

## Sensitive Data Review Rules

Sensitive data risk must be flagged when the GTM export appears to collect, transform, store, or transmit personal or sensitive values.

Flag these values and patterns:

- Email address fields, including `email`, `user_email`, `sha256_email`, and `hashed_email`.
- Phone fields, including `phone`, `telephone`, `mobile`, and `normalized_phone`.
- User identifiers, including `user_id`, `customer_id`, `client_id`, `external_id`, `member_id`, and `subscriber_id`.
- Address or identity fields, including `first_name`, `last_name`, `address`, `zip`, `postal_code`, and `date_of_birth`.
- Query parameters, cookies, or dataLayer variables that may contain user identifiers.
- Custom JavaScript that reads forms, URL parameters, cookies, local storage, or session storage.

Required handling:

- Set `manual_review_required` to true.
- Set `consent_review_required` to true when the data appears connected to advertising, remarketing, analytics identity, or conversion measurement.
- Do not include raw sensitive values in report text.
- Do not infer that a value is safe because it appears hashed.

Evidence should describe the field or variable name and location without exposing real user data.

## User Identifier Review Rules

User identifier handling requires manual review because identifiers can connect behavior across events, sessions, devices, or platforms.

Flag these GTM signals:

- Variables or parameters named `user_id`, `customer_id`, `external_id`, `member_id`, `subscriber_id`, `uid`, or similar.
- Tags that send identifiers to analytics, advertising, CRM, CDP, or data warehouse endpoints.
- Custom HTML or custom JavaScript that reads identifiers from cookies, local storage, session storage, forms, or URL parameters.
- Lookup or regex tables that map user attributes to vendor payload values.

Required handling:

- Set `manual_review_required` to true.
- Set `consent_review_required` to true for advertising, remarketing, audience, or cross-platform use.
- Do not claim that the identifier is allowed, compliant, or properly scoped.
- Do not automatically add identifiers to tags or remove identifiers from tags.

## Consent Settings Review Rules

Consent settings in an exported GTM container are useful evidence, but they are not proof of live consent behavior.

Inspect these signals when present:

- Built-in consent checks.
- Additional consent checks.
- Consent initialization triggers.
- Consent mode tags.
- CMP or consent platform tags.
- Trigger sequencing related to consent.
- Exceptions or blocking triggers intended to prevent early firing.

Required handling:

- If consent settings are missing on advertising or remarketing tags, flag for manual review.
- If consent settings are present, describe them as observed configuration, not proof that consent works on the live site.
- If a consent setup appears inconsistent, mark the finding as manual-review required.
- Do not modify consent settings automatically in the MLP.

## Manual-Review Criteria

Manual review is required when any of these are true:

- Advertising or remarketing vendor tag is present.
- Custom HTML tag is present.
- Enhanced conversion fields or user-provided data fields are present.
- User identifier, email, phone, address, or sensitive data variable is present.
- Custom JavaScript reads or transforms user data.
- Consent settings are missing, unclear, inconsistent, or attached to a risky tag.
- The tag fires on all pages and is connected to advertising, remarketing, audience, or user identity.
- The system is unsure whether a tag is consent-sensitive.

When uncertain, the MLP should mark the item as manual-review required instead of treating it as low risk.

## Audit Finding Requirements

Consent and privacy findings should include:

- Rule ID from this standard.
- Affected entity type.
- Affected entity ID and name, if available.
- Vendor or platform signal.
- Consent/risk category.
- Observed facts from the GTM export.
- Inferences, clearly labeled as inferences.
- Manual-review requirement.
- Whether automated changes are allowed, blocked, or manual-review only.
- Related output artifact, usually `audit_report.json`, `audit_report.md`, `change_log.json`, or `qa_checklist.md`.

## Rule IDs

Use these initial rule IDs until Task 2.3 defines the full audit rule catalog:

| Rule ID | Category | Trigger |
| --- | --- | --- |
| `CONSENT-ADS-001` | Advertising | Advertising vendor tag or variable detected |
| `CONSENT-REM-001` | Remarketing | Remarketing, retargeting, audience, or broad pixel behavior detected |
| `CONSENT-HTML-001` | Custom HTML | Custom HTML tag detected |
| `CONSENT-EC-001` | Enhanced conversions | Enhanced conversion or user-provided data signal detected |
| `CONSENT-DATA-001` | Sensitive data | Email, phone, address, user ID, or similar data signal detected |
| `CONSENT-ID-001` | User identifiers | Persistent or cross-platform user identifier detected |
| `CONSENT-CONFIG-001` | Consent configuration | Missing, unclear, or inconsistent consent configuration detected |

## Automated Change Policy

- Allowed candidate: none for consent-sensitive changes in the MLP.
- Manual-review only: naming, documentation, or report recommendations for consent-sensitive entities.
- Blocked in Phase 2: adding consent settings, removing tags, changing triggers, changing payloads, editing Custom HTML, adding or removing user identifiers, changing enhanced conversion fields, or claiming consent behavior is valid.

## Approved Wording

Use wording like:

- "This tag appears consent-sensitive and requires human review."
- "The export shows consent settings, but the MLP cannot verify live site behavior."
- "This finding flags risk; it does not certify legal, privacy, or compliance status."
- "Review in GTM Preview and with the appropriate analyst, legal, or privacy reviewer before import or production use."

Avoid wording like:

- "This tag is compliant."
- "Consent is working."
- "This container is certified."
- "This optimized container is safe to publish."
- "This change can be deployed without review."
