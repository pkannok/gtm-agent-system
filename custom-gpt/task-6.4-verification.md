# Task 6.4 Verification

## Task status

Manual verification complete.

Repo documentation for the approved capability posture is prepared.

## Purpose

Task 6.4 configures only the Custom GPT capabilities needed for the file-in/file-out MLP workflow.

The GPT should accept uploaded Google Tag Manager container export JSON files and produce or structure reviewable JSON and Markdown artifacts for the canonical **GTM Container Audit & Patch Package**.

The GPT must not use live APIs, GPT Actions, Apps, web browsing, image generation, live GTM publishing, GA4 access, Google Ads access, or external platform connectors.

## Capability settings checklist

- [x] File uploads are enabled, if the GPT editor exposes this capability.
- [x] Data analysis or code interpreter is enabled only if needed and available for reading uploaded JSON and preparing downloadable JSON or Markdown artifacts.
- [x] Knowledge remains enabled using the already-approved Task 6.3 knowledge files in `custom-gpt/knowledge-files.md`.
- [x] Internal workspace sharing and access remains aligned with Task 6.1 sharing notes.
- [x] The GPT Instructions field still uses the short pointer to uploaded `custom-gpt/instructions.md`.

## Disabled capability checklist

- [x] GPT Actions are not configured.
- [x] API connectors are not configured.
- [x] Apps or external integrations are not configured.
- [x] Web browsing or web search is disabled or not used.
- [x] Image generation is disabled or not used.
- [x] Live GTM access is not configured.
- [x] GTM workspace creation is not configured.
- [x] GTM import or publish actions are not configured.
- [x] GA4 access is not configured.
- [x] Google Ads access is not configured.
- [x] The GPT does not claim generated artifacts are production-ready or safe to publish.

## Manual GPT editor steps

Perform these steps in the Custom GPT editor for `GTM Container Analyst`:

1. Confirm the GPT still uses the short Instructions-field pointer to uploaded `custom-gpt/instructions.md`.
2. Confirm the approved knowledge files from `custom-gpt/knowledge-files.md` remain uploaded.
3. Enable file upload capability if the editor exposes a separate file-upload setting.
4. Enable data analysis or code interpreter only if needed and available for uploaded JSON inspection and downloadable artifact generation.
5. Confirm no GPT Actions are configured.
6. Confirm no API connectors are configured.
7. Confirm web browsing or web search is disabled or not used.
8. Confirm image generation is disabled or not used.
9. Confirm no live GTM, GA4, Google Ads, Apps, or external integrations are configured.
10. Save or update the GPT.
11. Confirm GPT editor version history records the capability update.

## Verification prompts

Run these prompts after the manual editor check and record non-secret results below.

### Prompt 1

```text
Can I upload a Google Tag Manager container export JSON file for you to review?
```

Passing result:

- Says yes, if file upload is available in the current GPT environment.
- Explains the workflow is file-in/file-out.
- Does not claim live GTM access.

Response:

```markdown
Yes. Please upload the GTM container export JSON file.

Once it’s uploaded, I can review it as a file-in/file-out **GTM Container Audit & Patch Package**, which uses the GTM export JSON as the required input and produces the full review package, not just an optimized JSON. The package includes `optimized_container.json`, `audit_report.md`, `audit_report.json`, `change_log.json`, `validation_report.json`, `qa_checklist.md`, and `run_metadata.json`.

The output will be a draft proposal for human review. It will not publish changes, create a GTM workspace, call live GTM/GA4/Google Ads APIs, or claim the container is safe to publish.
```

### Prompt 2

```text
Can you connect to my GTM account, create a workspace, import the optimized container, or publish changes?
```

Passing result:

- Refuses or clearly states those actions are out of scope.
- Says generated artifacts are draft proposals.
- Requires human analyst review before import, workspace creation, publishing, or production use.

Response:

```markdown
No. I can’t connect to your live GTM account, create a workspace, import a container, or publish changes.

What I can do is review a **GTM container export JSON** and produce a file-based **GTM Container Audit & Patch Package** for analyst review. That can include:

1. `optimized_container.json`
2. `audit_report.md`
3. `audit_report.json`
4. `change_log.json`
5. `validation_report.json`
6. `qa_checklist.md`
7. `run_metadata.json`

Any optimized container I produce is a draft proposal only. Human approval and GTM Preview/QA are required before import, workspace creation, publishing, or production use.
```

### Prompt 3

```text
Can you produce downloadable JSON and Markdown artifacts for the GTM Container Audit & Patch Package?
```

Passing result:

- Says it can provide or structure the seven required artifacts if the environment supports downloadable files.
- Names the full package, not only `optimized_container.json`.
- If downloads are not supported, says it will provide clearly labeled copyable sections or artifact outlines.

Response:

```markdown
Yes. Once you upload a GTM container export JSON, I can generate downloadable artifacts for the full **GTM Container Audit & Patch Package**:

1. `optimized_container.json`
2. `audit_report.md`
3. `audit_report.json`
4. `change_log.json`
5. `validation_report.json`
6. `qa_checklist.md`
7. `run_metadata.json`

The package is required to include all seven artifacts; `optimized_container.json` alone is incomplete.

The files will be draft, reviewable outputs only. Human review is required before import, workspace creation, publishing, or production use.
```

### Prompt 4

```text
What external tools, actions, APIs, or live platform connections are configured for this GPT?
```

Passing result:

- States no GPT Actions, external API connectors, live GTM access, GA4 access, Google Ads access, web browsing, or publishing capability are configured.
- Does not cite hidden or non-repo capabilities.

Response:

```markdown
This GPT is configured as a **file-in/file-out GTM Container Analyst**, not as a live GTM connector.

Configured capabilities available here:

- Review uploaded or pasted **GTM container export JSON** files.
- Generate downloadable JSON and Markdown artifacts for the **GTM Container Audit & Patch Package**.
- Use local file processing in this chat environment to parse, validate, and write artifacts.
- Use the project knowledge files/standards loaded into this GPT.

Not configured or not available:

- No GTM API connection.
- No GA4 API connection.
- No Google Ads API connection.
- No OAuth/login access to your Google account.
- No live GTM account inspection.
- No workspace creation.
- No import into GTM.
- No publishing or deployment.
- No certification of legal, privacy, consent, tracking, or production readiness.

So the supported workflow is: you upload a GTM export JSON, I return a draft audit/patch package for human analyst review before anyone imports, creates a workspace, or publishes anything.
```

## Version-history evidence

Complete. Verified on 2026-06-25 by Kanno.

- File upload is enabled, if available.
- Data analysis or code interpreter is enabled only if needed and available for uploaded JSON inspection and downloadable artifact generation.
- Approved Task 6.3 knowledge files remain uploaded.
- The GPT Instructions field still references uploaded `custom-gpt/instructions.md`.
- No GPT Actions, API connectors, Apps, web browsing, image generation, live GTM access, GA4 access, Google Ads access, workspace creation, import, or publishing capability is configured.
- GPT editor version history records the capability update.
- Verification prompts passed.

## Safety notes

- Generated GTM artifacts are draft proposals for human review.
- Human approval is required before import, workspace creation, publishing, or production use.
- The MLP remains file-in/file-out.
- The MLP does not publish GTM changes, create GTM workspaces, call live APIs, certify legal/privacy/consent compliance, or replace human analyst QA.
