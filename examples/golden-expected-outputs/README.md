# Golden Expected Outputs

These files define expected GTM Container Audit & Patch Package shapes for the synthetic fixtures in `examples/synthetic-gtm-containers/`.

They are deterministic golden expectations for future regression tests. They are not generated from real client data, they do not represent live GTM exports, and they do not make `optimized_container.json` publish-ready.

Each `*.expected-package.json` file is intended to validate against `schemas/gtm_patch_package.schema.json` and includes:

- A link to the source fixture through `source_container_summary.input_file_name` and `run_metadata.input_files`.
- Expected finding summaries.
- Expected change log posture, including `no_change` entries where the expected outcome is documentation or manual review rather than a proposed GTM edit.
- Validation, risk, QA, and safety sections required by the package contract.

## Index

| Fixture ID | Fixture | Golden expected output |
| --- | --- | --- |
| `synthetic-naming-001` | `../synthetic-gtm-containers/synthetic-naming-issues.json` | `synthetic-naming-001.expected-package.json` |
| `synthetic-reference-001` | `../synthetic-gtm-containers/synthetic-broken-references.json` | `synthetic-reference-001.expected-package.json` |
| `synthetic-duplicate-001` | `../synthetic-gtm-containers/synthetic-duplicate-purchase-tags.json` | `synthetic-duplicate-001.expected-package.json` |
| `synthetic-unused-001` | `../synthetic-gtm-containers/synthetic-unused-legacy-entities.json` | `synthetic-unused-001.expected-package.json` |
| `synthetic-ecommerce-001` | `../synthetic-gtm-containers/synthetic-ecommerce-missing-fields.json` | `synthetic-ecommerce-001.expected-package.json` |
| `synthetic-consent-001` | `../synthetic-gtm-containers/synthetic-consent-risk-remarketing.json` | `synthetic-consent-001.expected-package.json` |

Future golden tests can compare generated package summaries against these files for finding IDs, severities, categories, affected entities, proposed-change posture, validation status, risk summary, and QA checklist coverage.
