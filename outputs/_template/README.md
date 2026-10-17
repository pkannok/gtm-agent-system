# GTM Container Audit & Patch Package Output Template

Each MLP run should produce a folder with this structure:

```text
outputs/
  {client_id-or-no-client}/
    {run_id}/
      optimized_container.json
      audit_report.md
      audit_report.json
      change_log.json
      validation_report.json
      qa_checklist.md
      run_metadata.json
```

Use the repository schemas as the artifact templates. Do not create one combined JSON object and split it later; each listed JSON file is a separate artifact.

## Required artifact contract

- `optimized_container.json`: a complete GTM export-shaped JSON object. Preserve `exportFormatVersion`, `containerVersion`, and array-valued `containerVersion.tag`, `containerVersion.trigger`, and `containerVersion.variable` fields. This is a draft proposal, not publish-ready output.
- `audit_report.json`: use `artifact_type`, `schema_version`, `run_id`, `client_id`, `source_container_summary`, `audit_summary`, `findings`, `manual_review_items`, and `assumptions`. Every finding needs a description and `human_review_required`.
- `change_log.json`: use `artifact_type`, `schema_version`, `run_id`, `client_id`, `source_container_file`, `optimized_container_file`, `changes`, `summary`, `human_approval_required`, and `publishes_gtm_changes`. Set the last two safety fields to `true` and `false` respectively.
- `validation_report.json`: use `artifact_type`, `schema_version`, `run_id`, `package_schema_version`, `validation_status`, `checks`, `errors`, `warnings`, and `publish_safety`. Warnings are strings. Set `optimized_container_publish_ready` and `mlp_publishes_gtm_changes` to `false`, and `human_approval_required` to `true`.
- `run_metadata.json`: include `run_id`, `created_at`, `input_files` as a non-empty string array, `client_id`, `standards_applied`, `mlp_version`, and `tool_version`.

Keep run IDs, finding IDs, change IDs, related finding/change links, and summary counts consistent across all artifacts. Run the package validator before delivery:

```powershell
python scripts\validate_output_package.py --package-dir <package-directory>
```

For every direct child package directory under the Phase 7 runs directory, plus the known-good/known-bad controls, use:

```powershell
.\scripts\validate_phase_7_outputs.ps1
```

Validation is structural and does not prove tracking correctness, privacy or consent compliance, publish safety, or production readiness. Human approval is required before import, workspace creation, publishing, or production use.
