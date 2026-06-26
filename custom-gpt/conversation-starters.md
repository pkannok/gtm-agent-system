# Custom GPT Conversation Starters

## Status

Task 6.5 conversation starters are complete.

Manual GPT editor entry and version-history verification are recorded in `custom-gpt/task-6.5-verification.md`.

## Purpose

These conversation starters are for the `GTM Container Analyst` Custom GPT.

They are designed for the MLP file-in/file-out workflow, where a user uploads a Google Tag Manager container export JSON file and receives a draft **GTM Container Audit & Patch Package** for human analyst review.

## Final conversation starters

1. Upload a GTM container export JSON and create a draft GTM Container Audit & Patch Package with all required artifacts.

2. Review this uploaded GTM export for duplicate tags, unused variables, naming issues, broken references, and proposed cleanup.

3. Audit this uploaded GTM container export for consent-sensitive tags, remarketing risk, risky Custom HTML, and manual-review flags.

4. Apply this optional client profile to my uploaded GTM export and produce reviewable audit findings, proposed changes, and QA notes.

5. Generate the full GTM Container Audit & Patch Package for this uploaded export, including optimized JSON, reports, change log, validation, QA, and metadata.

6. Create a human QA checklist and analyst review notes for this uploaded GTM container export before any implementation decisions.

7. Review the proposed cleanup changes for this uploaded GTM export and explain what a human analyst must verify before use.

8. Tell me which files to upload for a file-in/file-out GTM container audit and what draft artifacts I should expect back.

## GPT editor entry notes

The Custom GPT editor may limit the number or length of conversation starters. If not all eight fit, use the first four as the minimum recommended set.

Recommended priority order:

1. Full uploaded-export package starter.
2. Cleanup review starter.
3. Consent/privacy-sensitive review starter.
4. Client profile starter.
5. Full artifact-list starter.
6. QA checklist starter.
7. Proposed-change review starter.
8. Upload guidance starter.

## Safety review

- [x] Starters require or imply uploaded GTM container export files.
- [x] Starters point users toward the **GTM Container Audit & Patch Package**.
- [x] Starters reflect real MLP tasks: audit, cleanup, consent/privacy review, client profile application, QA, and proposed-change review.
- [x] Starters do not mention live API access.
- [x] Starters do not mention GTM workspace creation.
- [x] Starters do not mention GTM import or publishing.
- [x] Starters do not mention GA4, Google Ads, web browsing, GPT Actions, Apps, or external platform connectors.
- [x] Starters do not imply generated artifacts are production-ready or safe to publish.
- [x] Starters reinforce draft artifacts and human analyst review.

## Manual verification

- [x] Final starters are copied into the `GTM Container Analyst` GPT editor.
- [x] Starters display correctly in the GPT UI.
- [x] Starters guide users toward uploading GTM container export JSON files.
- [x] Starters set expectations for draft artifacts requiring human analyst review.
- [x] Starters do not mention live GTM, workspace creation, import, publish, GA4, Google Ads, web browsing, GPT Actions, API connectors, Apps, or production deployment.
- [x] GPT editor version history records the conversation-starter update.
