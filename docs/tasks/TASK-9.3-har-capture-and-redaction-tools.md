# Task 9.3 - Build HAR capture and redaction tools

## Status

Future

## Goal

Create Playwright-based HAR capture and redaction tools for future tracking diagnostics.

## How it fits

HAR tooling bridges toward future tracking diagnostics while keeping unredacted data away from agents.

## In scope

- Build HAR capture tooling.
- Build HAR redaction tooling.
- Normalize tracking events after redaction.
- Prevent unredacted HAR artifacts from being sent into agents.

## Out of scope

- Blocking MLP release.
- Sending unredacted sensitive data to agents.
- Live production diagnostics without approval.

## Definition of done for first future version

- [ ] HAR capture works on a test site.
- [ ] Redaction removes cookies, authorization headers, emails, phone numbers, and likely user identifiers.
- [ ] HAR parser outputs normalized tracking events.
- [ ] HAR artifacts are not sent into other agents until redacted.
