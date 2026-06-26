# Custom GPT Creation Checklist

## Status

Repo checklist for Task 6.1.

This checklist records repo-visible setup evidence for completed Task 6.1 verification.

## Source files to use

- `custom-gpt/configuration.md`
- `custom-gpt/description.md`
- `custom-gpt/share-access-notes.md`

Use `custom-gpt/instructions-draft.md` only as existing draft context. Final detailed instructions are deferred to Task 6.2.

## Before opening the GPT editor

- [x] Confirm the GPT name is `GTM Container Analyst`.
- [x] Confirm the short description matches `custom-gpt/description.md` or a reviewed equivalent.
- [x] Confirm intended access is internal workspace users only.
- [x] Confirm the GPT remains file-in/file-out for the MLP.
- [x] Confirm the GPT must produce the **GTM Container Audit & Patch Package**, not only `optimized_container.json`.

## GPT editor setup

- [x] Create or update the Custom GPT named `GTM Container Analyst`.
- [x] Add the reviewed short description.
- [x] Do not create final detailed instructions in Task 6.1.
- [x] Do not upload or reference final knowledge files in Task 6.1.
- [x] Do not finalize capabilities in Task 6.1.
- [x] Do not finalize conversation starters in Task 6.1.
- [x] Do not configure GPT Actions or API connectors.
- [x] Set sharing to intended internal users only, if the GPT editor supports that setting.

## Verification before Task 6.1 completion

- [x] GPT exists in the GPT editor.
- [x] GPT has the clear name `GTM Container Analyst`.
- [x] GPT description is clear and aligned with the GTM Container Audit & Patch Package.
- [x] GPT access is limited to intended internal users.
- [x] GPT editor version history records the configuration update.
- [x] No public sharing, GPT Actions, API connectors, live GTM access, GA4 access, Google Ads access, or publish-ready wording was added.

## Evidence to record after verification

Non-secret version-history verification notes are recorded in `custom-gpt/configuration.md` and `custom-gpt/task-6.1-verification.md`.

## Later task checklists

Task 6.3 knowledge upload selection and verification are recorded in:

- `custom-gpt/knowledge-files.md`
- `custom-gpt/task-6.3-verification.md`

Task 6.3 also records the GPT Instructions field-limit workaround: upload `custom-gpt/instructions.md` as approved knowledge and keep the GPT Instructions field as a short explicit pointer to that file.

Task 6.4 capability posture and manual editor verification are recorded in:

- `custom-gpt/task-6.4-verification.md`

Task 6.5 final conversation starters and manual editor-entry verification are recorded in:

- `custom-gpt/conversation-starters.md`
- `custom-gpt/task-6.5-verification.md`
