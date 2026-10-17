# Manual QA Checklist — synthetic-naming-001

All items are **todo**; no live or human QA was performed. Human approval is required before import, workspace creation, publishing, or production use.

### QA-001 — Confirm rename and external text dependencies

- Status: `todo`; reviewer: GTM analyst (unassigned).
- Related finding: `F-001`; rule: `GTM-NAME-001`; related change: `C-001`.
- Entity: tag 101.
- Scenario: Confirm rename and external text dependencies.
- Steps: Compare original vs draft tag 101 fields; search offline QA docs and any custom references for literal tag name.
- Expected: Only tag name changes; references and event parameters remain identical.
- Evidence to capture: JSON diff and reviewer notes.

### QA-002 — Confirm PAGEVIEW scope and proposed naming

- Status: `todo`; reviewer: GTM analyst (unassigned).
- Related finding: `F-002`; rule: `GTM-NAME-001`; related change: `—`.
- Entity: trigger 201.
- Scenario: Confirm PAGEVIEW scope and proposed naming.
- Steps: In isolated review environment inspect trigger conditions and test ordinary page views; do not apply proposed rename yet.
- Expected: Analyst either approves PV - All Pages or supplies an accurate scoped label.
- Evidence to capture: Trigger screenshot and Preview event timeline.

### QA-003 — Assess variable rename dependency

- Status: `todo`; reviewer: GTM analyst (unassigned).
- Related finding: `F-003`; rule: `GTM-NAME-001`; related change: `—`.
- Entity: variable 301 and tag 101.
- Scenario: Assess variable rename dependency.
- Steps: Inspect measurementId token {{id}} and constant value; review any cross-reference and external name usage.
- Expected: No rename until all tokens are mapped and coordinated in a separately approved proposal.
- Evidence to capture: Reference map and approval decision.

### QA-004 — Confirm folder grouping name

- Status: `todo`; reviewer: GTM analyst (unassigned).
- Related finding: `F-004`; rule: `GTM-NAME-001`; related change: `—`.
- Entity: folder 401.
- Scenario: Confirm folder grouping name.
- Steps: Inspect members tag 101 and variable 301 and client taxonomy.
- Expected: Proposed folder label reflects verified grouping without approval implications.
- Evidence to capture: Folder membership screenshot/review notes.

### QA-005 — Verify lead_submit firing behavior

- Status: `todo`; reviewer: GTM analyst (unassigned).
- Related finding: `F-005`; rule: `GTM-NAME-001` / `GTM-QA-001`; related change: `—`.
- Entity: tag 101 / trigger 201.
- Scenario: Verify lead_submit firing behavior.
- Steps: In safe human-controlled GTM Preview, observe ordinary page view and real test lead submission; inspect GA4 event name and measurement ID variable, confirm non-firing where appropriate.
- Expected: Business-approved expected fire and non-fire cases match Preview; no double-counted lead events.
- Evidence to capture: Preview timeline, fired/not-fired tags, redacted parameters, analyst sign-off.

### QA-006 — Rollback or reject patch

- Status: `todo`; reviewer: GTM analyst (unassigned).
- Related finding: `F-001`; rule: `GTM-NAME-001`; related change: `C-001`.
- Entity: tag 101.
- Scenario: Rollback or reject patch.
- Steps: Reject by using original export or restore tag 101 name tag 1; compare all other fields byte-equivalently after JSON normalization.
- Expected: Baseline tag name returns and configuration remains unchanged.
- Evidence to capture: Before/after diff and approver decision.

### QA-007 — Review completeness and controls

- Status: `todo`; reviewer: GTM analyst (unassigned).
- Related finding: `—`; rule: `GTM-NAME-001`; related change: `—`.
- Entity: full package.
- Scenario: Review completeness and controls.
- Steps: Verify seven files, JSON parse, finding/change traceability, no live modification, and approval gating.
- Expected: All seven present; draft status and review limits remain explicit.
- Evidence to capture: File list, check results and analyst approval record.

## Approval boundary

Do not treat structural checks as Preview validation, consent verification, tracking correctness, or production readiness. Obtain stakeholder and analyst approval before any import or subsequent GTM action.
