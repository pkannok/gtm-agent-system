# Task 10.4 - Add read-only Google Ads reporting connector

## Status

Future

## Goal

Allow future agents to pull Google Ads performance and conversion reporting data through approved read-only report templates.

## How it fits

This future task supports later GA4-versus-Google-Ads reconciliation without changing the GTM Container Audit & Patch Package contract.

## In scope

- Run approved Google Ads report templates only.
- Record query, customer ID, date range, and metric definitions.
- Define output compatible with a future `google_ads_report_result.schema.json`.
- Keep the connector read-only.

## Out of scope

- Google Ads configuration writes.
- Campaign, conversion action, budget, or account changes.
- Broad ad hoc reporting without approved templates.
- Publishing or applying GTM changes.

## Definition of done for future phase

- [ ] Connector supports approved report templates only.
- [ ] Connector output conforms to `google_ads_report_result.schema.json`.
- [ ] Connector stores query, customer ID, date range, and metric definitions.
- [ ] Connector is read-only.
