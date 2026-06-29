# synthetic-consent-001 Run Folder

Place only actual GPT run outputs and manual review evidence in this folder.

Expected fixture:

- `examples/synthetic-gtm-containers/synthetic-consent-risk-remarketing.json`

Golden expected output for reviewer comparison:

- `examples/golden-expected-outputs/synthetic-consent-001.expected-package.json`

Expected issue category:

- All-pages remarketing and Custom HTML risk without clear consent evidence; expected rule `GTM-CONSENT-001`.

Expected run folder contents after manual execution:

```text
runs/synthetic-consent-001/
  gpt-response.md
  optimized_container.json
  audit_report.md
  audit_report.json
  change_log.json
  validation_report.json
  qa_checklist.md
  run_metadata.json
  manual-review.md
```

Do not add generated artifacts until a human has run the fixture through the internal `GTM Container Analyst` Custom GPT.
