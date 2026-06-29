# synthetic-duplicate-001 Run Folder

Place only actual GPT run outputs and manual review evidence in this folder.

Expected fixture:

- `examples/synthetic-gtm-containers/synthetic-duplicate-purchase-tags.json`

Golden expected output for reviewer comparison:

- `examples/golden-expected-outputs/synthetic-duplicate-001.expected-package.json`

Expected issue category:

- Duplicate GA4 purchase tracking on the same trigger; expected rules `GTM-DUP-001` and `GTM-ECOM-001`.

Expected run folder contents after manual execution:

```text
runs/synthetic-duplicate-001/
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
