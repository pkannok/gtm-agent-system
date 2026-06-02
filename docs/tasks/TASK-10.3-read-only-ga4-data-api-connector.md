# Task 10.3 - Add read-only GA4 Data API connector

## Status

Future

## Goal

Allow future agents to pull GA4 report data for reconciliation through approved read-only report templates.

## How it fits

This future task supports later Google Analytics data querying and tracking triage workflows without changing the MLP deliverable.

## In scope

- Run a limited set of approved GA4 report templates.
- Record property ID, date range, dimensions, metrics, filters, and API method.
- Define output compatible with a future `ga4_report_result.schema.json`.
- Keep the connector read-only.

## Out of scope

- Modifying GA4 configuration.
- Broad ad hoc reporting queries without approved templates.
- Sending unbounded raw analytics data into agents.
- Publishing or applying GTM changes.

## Definition of done for future phase

- [ ] Connector can run a limited set of approved report templates.
- [ ] Connector records property ID, date range, dimensions, metrics, filters, and API method.
- [ ] Connector output conforms to a `ga4_report_result.schema.json`.
- [ ] Connector is read-only.
