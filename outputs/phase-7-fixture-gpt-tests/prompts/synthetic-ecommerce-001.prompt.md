# Prompt for synthetic-ecommerce-001

Use the uploaded fixture JSON file as the only GTM container export input.

Fixture ID: `synthetic-ecommerce-001`

Expected issue category: purchase event lacks clear transaction ID and currency mappings; expected rule `GTM-ECOM-001`.

Produce the full canonical **GTM Container Audit & Patch Package** with all seven required artifacts:

1. `optimized_container.json`
2. `audit_report.md`
3. `audit_report.json`
4. `change_log.json`
5. `validation_report.json`
6. `qa_checklist.md`
7. `run_metadata.json`

Use the repo standards and knowledge files already loaded into the Custom GPT. Preserve evidence and traceability from findings to affected GTM entities. Identify manual-review flags and unsafe changes.

Treat all outputs as draft proposals requiring human analyst review before import, workspace creation, publishing, or production use. Do not claim to connect to, inspect, change, import, publish, or verify any live GTM, GA4, Google Ads, API, workspace, website, or production platform.
