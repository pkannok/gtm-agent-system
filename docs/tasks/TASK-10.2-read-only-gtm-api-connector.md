# Task 10.2 - Add read-only GTM API connector

## Status

Future

## Goal

Allow future system versions to fetch GTM configuration data directly through a read-only connector.

## How it fits

This future task can replace file upload for authorized users while preserving the same GTM Container Audit & Patch Package output.

## In scope

- Fetch GTM account, container, and workspace data with read-only permissions.
- Normalize fetched data into the same input shape as file uploads.
- Keep read-only, workspace-write, and publish permissions explicitly separated.
- Preserve the existing audit package output contract.

## Out of scope

- GTM workspace writes.
- GTM version publishing.
- Permission changes.
- Treating fetched data as approved implementation work.

## Definition of done for future phase

- [ ] Connector can fetch container and workspace data read-only.
- [ ] No write scopes are used.
- [ ] Output is normalized into the same format as file uploads.
- [ ] Audit package output does not change.
