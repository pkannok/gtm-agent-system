# Architecture

## Current architecture: MLP

The MLP is a file-in/file-out workflow.

```text
User uploads GTM container export JSON
  ↓
Custom GPT applies project instructions and knowledge
  ↓
GTM Container Auditor Skill references reusable workflow materials
  ↓
System produces GTM Container Audit & Patch Package
```
