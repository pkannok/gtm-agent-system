# Task 10.6 - Add approval-gated pre-production GTM writes

## Status

Future

## Goal

Allow future system versions to create or modify GTM workspaces after explicit approval, without allowing agents to publish.

## How it fits

This future task supports a controlled path from proposed file-based changes to pre-production GTM workspace changes while preserving the no-publish risk posture.

## In scope

- Keep write actions disabled by default.
- Require human approval before workspace creation or workspace modification.
- Create or update tags, triggers, and variables only in approved pre-production workspaces.
- Generate preview links or preview instructions where possible.
- Attach rollback notes to every write action.

## Out of scope

- Publishing GTM versions.
- Deleting live resources.
- Changing permissions.
- Running writes without explicit human approval.
- Treating `optimized_container.json` as publish-ready.

## Definition of done for future phase

- [ ] Write actions are disabled by default.
- [ ] Human approval is required before workspace creation.
- [ ] Publish is unavailable to the agent.
- [ ] Every write action has rollback notes.
- [ ] Workspace changes are validated before handoff.
