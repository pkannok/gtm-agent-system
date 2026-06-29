# synthetic-naming-001 Run Folder

Place only actual GPT run outputs and manual review evidence in this folder.

Expected fixture:

- `examples/synthetic-gtm-containers/synthetic-naming-issues.json`

Golden expected output for reviewer comparison:

- `examples/golden-expected-outputs/synthetic-naming-001.expected-package.json`

Expected issue category:

- Vague tag, trigger, variable, and folder names; expected rule `GTM-NAME-001`.

Expected run folder contents after manual execution:

```text
runs/synthetic-naming-001/
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
