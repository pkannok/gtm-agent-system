# Task 10.5 - Introduce Agents SDK orchestration

## Status

Future

## Goal

Split the monolithic workflow into specialist agents coordinated by an orchestrator.

## How it fits

This future task defines the long-term architecture for handoffs, guardrails, human review, traces, and evaluation loops.

## In scope

- Define explicit contracts for specialist agents.
- Ensure specialist agents exchange schema-valid artifacts.
- Make the orchestrator responsible for the final answer.
- Log tool calls and outputs.
- Require human approval for risky actions.

## Out of scope

- Replacing the MLP file-in/file-out workflow.
- Allowing specialists to publish GTM changes.
- Allowing agents to bypass schema contracts.
- Moving project decisions out of the repository.

## Recommended future agents

- Intake Agent
- GTM Container Auditor
- GTM Patch Builder
- GTM Validator
- Recipe Builder
- HAR Analyzer
- GA4 Data Querier
- Google Ads Data Querier
- Reconciliation Agent
- Final Analyst Agent

## Definition of done for future phase

- [ ] Each agent has an explicit contract.
- [ ] The orchestrator owns the final answer.
- [ ] Specialist agents communicate using schema-valid artifacts.
- [ ] Risky actions trigger human approval.
- [ ] Tool calls and outputs are logged.
