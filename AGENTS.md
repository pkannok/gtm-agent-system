# AGENTS.md

## Project

This repository defines and implements a portable GTM Container Audit & Patch Package system for a future Custom GPT + Skill workflow.

## Current scope

The current milestone is Task 0.1: define the canonical MLP deliverable.

Do not create validators, schemas, scripts, fixtures, GitHub Actions, API connectors, or full Skill files unless explicitly asked.

## Working rules

- Prefer small, reviewable changes.
- Keep all project decisions in repo files, not only in ChatGPT or Custom GPT configuration.
- Use plain Markdown for planning documents.
- Treat the Custom GPT as a user interface, not the system of record.
- Treat the Skill as a reusable package that will later reference the same deliverable contract.
- Preserve the exact deliverable name: GTM Container Audit & Patch Package.
- Do not describe optimized_container.json as the only MLP output.
- Do not imply that any generated GTM JSON is safe to publish without human review.

## Current definition of done for Task 0.1

Task 0.1 is complete when:

1. The team agrees the first MLP deliverable is GTM Container Audit & Patch Package.
2. Required output files are named.
3. The future Custom GPT instructions and Skill references use the same deliverable name.
4. "Optimized GTM JSON only" is explicitly out of scope for the MLP output.
