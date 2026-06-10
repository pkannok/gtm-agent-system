# Custom GPT Configuration

## Status

Repo configuration drafted for Task 6.1.

GPT editor setup and verification are required before Task 6.1 can be marked complete.

## GPT identity

Name:
`GTM Container Analyst`

Short description:
Audits Google Tag Manager container export JSON files and helps produce a GTM Container Audit & Patch Package with optimized JSON, audit findings, change log, validation report, QA checklist, and run metadata.

Category:
Internal technical marketing analytics assistant.

Primary user interface role:
The Custom GPT is the user-facing wrapper for the file-in/file-out MLP workflow. The repository and Skill remain the system of record.

## Intended access

Audience:
Internal agency users only.

Intended users:

- Technical marketing analysts.
- Analytics engineers.
- GTM implementation specialists.
- Agency team members reviewing client tracking containers.

Sharing setting:
Internal workspace access only, if the GPT editor supports that setting for the workspace.

Public access:
Do not publish publicly for the MLP.

## MLP scope

The GPT is file-in/file-out only.

It accepts Google Tag Manager container export JSON files and guides users toward the canonical deliverable:

**GTM Container Audit & Patch Package**

The deliverable is incomplete if it only includes `optimized_container.json`.

## Required safety boundaries

- Do not claim generated GTM JSON is publish-ready.
- Do not imply the MLP can publish GTM changes.
- Do not create GTM workspaces.
- Do not call GTM, GA4, Google Ads, or other live platform APIs.
- Do not replace human analyst QA.
- Treat all generated GTM artifacts as draft proposals requiring human review before import, workspace creation, publishing, or production use.

## GPT editor field plan

| GPT editor field | Task 6.1 value or status |
| --- | --- |
| Name | `GTM Container Analyst` |
| Description | Use the short description above. |
| Instructions | Deferred to Task 6.2. Use `custom-gpt/instructions-draft.md` only as existing draft context until Task 6.2 creates the final instructions file. |
| Knowledge | Deferred to Task 6.3. Do not upload hidden or non-repo knowledge. |
| Capabilities | Deferred to Task 6.4. Do not enable web browsing, image generation, API actions, or live platform access for the MLP. |
| Conversation starters | Deferred to Task 6.5. |
| Actions | Out of scope for Phase 6 MLP configuration. Do not configure API actions. |
| Visibility/access | Internal workspace users only. |

## GPT editor verification checklist

Task 6.1 can be marked complete only after a human with GPT editor access verifies:

- [ ] A Custom GPT exists with the name `GTM Container Analyst`.
- [ ] The GPT description matches the short description in this file or a reviewed equivalent.
- [ ] GPT access is limited to intended internal users.
- [ ] The GPT editor version history records the configuration update.
- [ ] No API actions, live GTM access, GA4 access, Google Ads access, web browsing requirement, or public release setting was added.

## Version history log

| Date | Source | Change | Verification status |
| --- | --- | --- | --- |
| 2026-06-10 | Repo Task 6.1 | Drafted repo source-of-truth configuration fields for the Custom GPT. | GPT editor verification pending. |
