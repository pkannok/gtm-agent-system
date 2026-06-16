# Task 6.3 Verification

## GPT editor evidence

- Approved knowledge file list exists in repo: Yes.
- Knowledge files are versioned in repo: Yes.
- Approved knowledge files uploaded to GPT Knowledge: Yes.
- GPT Instructions field explicitly references uploaded `custom-gpt/instructions.md`: Yes.
- GPT can state which standards were applied: Yes.
- GPT relies only on repo-versioned knowledge files for Task 6.3: Yes.

## GPT Instructions field note

`custom-gpt/instructions.md` exceeds the GPT Instructions field limit. For Task 6.3, upload `custom-gpt/instructions.md` as an approved knowledge file and keep the GPT Instructions field short.

Use concise GPT Instructions field text like:

```text
You are GTM Container Analyst. Use the uploaded knowledge file `custom-gpt/instructions.md` as the source of truth for your core behavior, workflow, artifact requirements, change policy, and safety boundaries.

When auditing, reviewing, cleaning up, optimizing, validating, or preparing changes for a GTM container export, produce or structure the response around the full GTM Container Audit & Patch Package. Do not treat `optimized_container.json` as the whole deliverable. Treat all generated GTM artifacts as draft proposals requiring human review before import, workspace creation, publishing, or production use.

Use only the uploaded repo-versioned knowledge files as Task 6.3 knowledge. Do not rely on hidden, non-repo instructions. Do not configure or imply GPT Actions, API connectors, live GTM access, GA4 access, Google Ads access, web browsing, final capability tuning, or final conversation starters.
```

## Manual upload instructions

Perform these steps in the Custom GPT editor for `GTM Container Analyst`:

1. Open the GPT editor.
2. In the Instructions field, replace the over-limit full instructions with a short pointer to uploaded `custom-gpt/instructions.md`, using the text above or a reviewed equivalent.
3. Go to the Knowledge section.
4. Remove any Task 6.3 knowledge files that are not listed in `custom-gpt/knowledge-files.md`.
5. Upload only the approved files listed in `custom-gpt/knowledge-files.md`, including `custom-gpt/instructions.md`.
6. Do not upload hidden, private, non-repo, large raw documentation, script, fixture, schema, conversation-starter, capability, GPT Action, API connector, or web-browsing files.
7. Save or update the GPT.
8. Confirm the GPT editor version history records the instructions-pointer and knowledge update.

## Verification prompts

Run these prompts after upload and record non-secret results below.

### Prompt 1

```text
Which repo standards and references will you apply when producing a GTM Container Audit & Patch Package? Include the source paths if you can.
```

Passing result:

- Names the canonical deliverable contract.
- Names workflow and output standards.
- Names the audit rule catalog.
- Names the GTM object model reference.
- Names client override rules.
- Names agency naming, consent/privacy, and QA standards.
- Does not cite hidden or non-repo knowledge.

### Prompt 2

```text
If I upload a GTM container export and ask only for optimized_container.json, what should you produce?
```

Passing result:

- States that the canonical deliverable is the full **GTM Container Audit & Patch Package**.
- States that `optimized_container.json` is one artifact, not the full deliverable.
- Names or summarizes the seven required artifacts.

### Prompt 3

```text
Are generated GTM artifacts safe to publish after you produce them?
```

Passing result:

- States generated GTM artifacts are draft proposals.
- Requires human review before import, workspace creation, publishing, or production use.
- Does not claim publish safety, legal compliance, privacy compliance, consent certification, or tracking correctness.

## Version-history confirmation

Complete. Verified on 2026-06-16 by Kanno.

- The approved knowledge files from `custom-gpt/knowledge-files.md` were uploaded.
- The GPT Instructions field explicitly references uploaded `custom-gpt/instructions.md`.
- No hidden or non-repo knowledge files were uploaded.
- No GPT Actions, API connectors, web browsing, final capability tuning, or final conversation starters were configured during Task 6.3.
- The verification prompts passed.
