# Synthetic GTM Container Fixtures

These fixtures are controlled, synthetic GTM container export JSON files for MLP workflow testing.

They do not contain real client data, live GTM account data, production container IDs, or real customer values. They are hand-authored, deterministic examples with known issues that future fixture-based tests can use as repeatable inputs.

These files document expected findings only. They are not golden output packages and do not define expected `audit_report.json`, `change_log.json`, `validation_report.json`, or `qa_checklist.md` artifacts.

## Fixture index

| Fixture ID | File | Primary expected issue types | Expected validator result |
| --- | --- | --- | --- |
| `synthetic-naming-001` | `synthetic-naming-issues.json` | Vague tag, trigger, variable, and folder names. Expected rule: `GTM-NAME-001`. | Pass with no structural errors. |
| `synthetic-reference-001` | `synthetic-broken-references.json` | Missing trigger, folder, and variable references. Expected rule: `GTM-REF-001`. | Fail reference validation. |
| `synthetic-duplicate-001` | `synthetic-duplicate-purchase-tags.json` | Duplicate GA4 purchase tracking on the same trigger. Expected rules: `GTM-DUP-001`, `GTM-ECOM-001`. | Pass with no structural errors. |
| `synthetic-unused-001` | `synthetic-unused-legacy-entities.json` | Orphaned legacy trigger, variable, and folder candidates. Expected rule: `GTM-UNUSED-001`. | Pass with no structural errors. |
| `synthetic-ecommerce-001` | `synthetic-ecommerce-missing-fields.json` | Purchase event lacks clear transaction ID and currency mappings. Expected rule: `GTM-ECOM-001`. | Pass with no structural errors. |
| `synthetic-consent-001` | `synthetic-consent-risk-remarketing.json` | All-pages remarketing and Custom HTML risk without clear consent evidence. Expected rule: `GTM-CONSENT-001`. | Pass with no structural errors. |

## Expected findings

### `synthetic-naming-001`

- Finding: Tag `101` is named `tag 1`, which does not identify platform, tag type, or purpose.
- Finding: Trigger `201` is named `all`, which does not describe the trigger condition.
- Finding: Variable `301` is named `id`, which does not identify variable type or data layer key.
- Finding: Folder `401` is named `misc`, which does not describe grouping purpose.
- Safety note: Any proposed rename is name-only and still requires human analyst review before import or production use.

### `synthetic-reference-001`

- Finding: Tag `102` references missing firing trigger ID `299`.
- Finding: Tag `102` references missing folder ID `499`.
- Finding: Tag `102` references missing variable `{{Missing Revenue}}`.
- Safety note: Broken references should be reported for analyst review, not repaired automatically.

### `synthetic-duplicate-001`

- Finding: Tags `103` and `104` both appear to send GA4 purchase events from trigger `203`.
- Finding: Both tags use the same measurement ID variable and purchase event name.
- Safety note: Duplicate purchase tracking can affect revenue reporting and must not be deleted or disabled automatically.

### `synthetic-unused-001`

- Finding: Trigger `204` is not referenced by any tag and is named as a legacy candidate.
- Finding: Variable `304` is not referenced by any tag, trigger, or variable in this fixture.
- Finding: Folder `404` groups no entities.
- Safety note: Unused-looking entities may be referenced outside the export and should be reviewed before any cleanup recommendation.

### `synthetic-ecommerce-001`

- Finding: Tag `105` sends a GA4 purchase event without a clear transaction ID mapping.
- Finding: Tag `105` sends a value mapping but does not include a clear currency mapping.
- Finding: Purchase tracking requires GTM Preview and test-order QA before trusting reporting behavior.
- Safety note: The MLP must not alter ecommerce data layer keys or payload mappings without human review.

### `synthetic-consent-001`

- Finding: Tag `106` appears to be Google Ads remarketing firing on all pages.
- Finding: Tag `107` is a Custom HTML tag that loads an external script from `https://vendor.example.test/pixel.js`.
- Finding: The export does not show clear consent gating evidence for these consent-sensitive tags.
- Safety note: This fixture flags consent and privacy risk only; it does not certify compliance or live consent behavior.
