# Task 6.2 - Write Custom GPT instructions

## Status

Complete

## Goal

Write the core behavior instructions for the GTM Container Analyst Custom GPT.

## How it fits

The Custom GPT controls interaction style and task execution, while the Skill/reference package controls the domain-specific workflow.

## In scope

- Store instructions in `custom-gpt/instructions.md`.
- Require GTM export verification.
- Require the full GTM Container Audit & Patch Package.
- Require conservative, reversible, reviewable changes.
- State that outputs are not safe to publish without human review.

## Out of scope

- Duplicating the full audit rule catalog.
- Live API actions.
- Full Skill implementation.
- External web browsing requirements.

## Definition of done for MLP

- [x] Instructions are in `custom-gpt/instructions.md`.
- [x] Instructions are copied into the GPT configuration.
- [x] Instructions do not duplicate the full audit rule catalog.
- [x] GPT consistently returns required package sections during tests.
