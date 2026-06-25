# Custom GPT Configuration

## Status

Repo configuration documentation and manual creation evidence completed for Task 6.1.

GPT editor creation, intended internal access, editor version-history verification, instruction pointer, knowledge upload verification, and capability verification are recorded as complete.

## Related Custom GPT files

- `custom-gpt/description.md` - GPT name, short description, intended users, and MLP scope.
- `custom-gpt/create-gpt-checklist.md` - GPT editor creation and verification checklist.
- `custom-gpt/share-access-notes.md` - Intended internal sharing and access notes.
- `custom-gpt/instructions.md` - Final Task 6.2 Custom GPT instructions. Uploaded as Task 6.3 knowledge because the full file exceeds the GPT Instructions field limit.
- `custom-gpt/knowledge-files.md` - Approved Task 6.3 Custom GPT knowledge upload set.
- `custom-gpt/task-6.3-verification.md` - Task 6.3 manual knowledge-upload and verification notes.
- `custom-gpt/task-6.4-verification.md` - Task 6.4 capability posture, manual editor checks, and verification notes.
- `custom-gpt/instructions-draft.md` - Superseded draft context retained for project history.
- `custom-gpt/task-6.2-verification.md` - Record of manual GPT instruction-copy and response-section verification.
- `custom-gpt/task-6.1-verification.md` - Record of manual GPT setup evidence and test GPT queries and responses.

## GPT identity

Name:
`GTM Container Analyst`

Short description:
Audits Google Tag Manager container export JSON files, applies agency and client standards, proposes reviewable cleanup changes, and returns a GTM Container Audit & Patch Package with optimized JSON, audit findings, change log, validation report, QA checklist, and run metadata.

Purpose:
This GPT is the initial user-facing wrapper for the GTM Container Audit & Patch Package MLP.

The GPT is file-in/file-out only. It is designed for users who upload GTM container export JSON files and optional client profile files.

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

## Initial configuration scope

Task 6.1 creates the GPT shell and records the configuration.

Detailed behavior instructions were written in Task 6.2 and are stored in `custom-gpt/instructions.md`.

Knowledge file selection is recorded in `custom-gpt/knowledge-files.md`. Manual GPT editor upload and verification are complete and recorded in `custom-gpt/task-6.3-verification.md`.

Capability configuration is complete for Task 6.4. The approved capability posture and manual GPT editor verification are recorded in `custom-gpt/task-6.4-verification.md`.

Conversation starters are deferred to Task 6.5.

## Required safety boundaries

- Do not claim generated GTM JSON is publish-ready.
- Do not imply the MLP can publish GTM changes.
- Do not create GTM workspaces.
- Do not call GTM, GA4, Google Ads, or other live platform APIs.
- Do not replace human analyst QA.
- Treat all generated GTM artifacts as draft proposals requiring human review before import, workspace creation, publishing, or production use.

## GPT editor field plan

| GPT editor field      | Task 6.1 value or status                                                            |
| --------------------- | ----------------------------------------------------------------------------------- |
| Name                  | `GTM Container Analyst`                                                             |
| Description           | Use the short description in `custom-gpt/description.md` or a reviewed equivalent.  |
| Instructions          | Short pointer to uploaded `custom-gpt/instructions.md` because the full file exceeds the GPT Instructions field limit. |
| Knowledge             | Completed in Task 6.3. Upload set is recorded in `custom-gpt/knowledge-files.md`, including `custom-gpt/instructions.md`. |
| Capabilities          | Completed in Task 6.4. File uploads and data analysis/code interpreter are enabled only for file-in/file-out MLP use; GPT Actions, API connectors, live platform access, web browsing, and image generation remain out of scope. |
| Conversation starters | Deferred to Task 6.5. Do not finalize conversation starters yet.                    |
| Actions               | Out of scope. Do not configure GPT Actions or API connectors.                       |
| Visibility/access     | Internal workspace users only, following `custom-gpt/share-access-notes.md`.        |

## GPT editor verification checklist

Task 6.1 was marked complete after a human with GPT editor access verified:

- [x] A Custom GPT exists with the name `GTM Container Analyst`.
- [x] The GPT description matches the short description in this file or a reviewed equivalent.
- [x] GPT access is limited to intended internal users.
- [x] The GPT editor version history records the configuration update.
- [x] No API actions, live GTM access, GA4 access, Google Ads access, web browsing requirement, or public release setting was added.

## Version history log

| Date       | Source        | Change                                                                                            | Verification status              |
| ---------- | ------------- | ------------------------------------------------------------------------------------------------- | -------------------------------- |
| 2026-06-10 | Repo Task 6.1 | Drafted repo source-of-truth configuration fields for the Custom GPT.                             | Superseded by completed Task 6.1 verification. |
| 2026-06-11 | Repo Task 6.1 | Added Task 6.1 creation checklist and share/access notes; clarified deferred Task 6.2-6.5 fields. | Superseded by completed Task 6.1 verification. |
| 2026-06-11 | Manual GPT setup | Recorded manual GPT creation notes, internal sharing status, Task 6.1 verification prompts, and GPT editor version-history verification. | Complete. |
| 2026-06-16 | Manual GPT knowledge setup | Uploaded the approved Task 6.3 knowledge set, configured the short Instructions-field pointer to `custom-gpt/instructions.md`, and verified applied-standards responses. | Complete. |
| 2026-06-25 | Manual GPT capability setup | Verified file upload, data analysis/code interpreter, approved knowledge continuity, absent Actions/API/live platform capabilities, and capability-response prompts. | Complete. |
