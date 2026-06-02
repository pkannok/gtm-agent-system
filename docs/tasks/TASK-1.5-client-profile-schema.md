# Task 1.5 - Create `client_profile.schema.json`

## Status

Complete

## Goal

Define how client-specific standards and overrides are represented.

## How it fits

The schema prevents one-off prompt customization per client and supports repeatable agency-wide use.

## In scope

- Create `schemas/client_profile.schema.json`.
- Create `examples/schema-validation/client_profile.sample.json`.
- Define client identity, standards, overrides, consent requirements, and manual-review rules.
- Validate the sample against the schema.

## Out of scope

- Creating client YAML templates.
- Applying client profiles in a live workflow.
- Agency standards implementation.
- Live API access.

## Definition of done for MLP

- [x] Client profile schema exists.
- [x] Sample client profile validates successfully.
- [x] Schema can represent client standards and overrides.
- [x] Schema can represent manual-review and consent requirements.
