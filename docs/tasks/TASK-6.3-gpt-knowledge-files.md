# Task 6.3 - Add knowledge files to the GPT

## Status

Complete

## Goal

Upload MLP reference documents and standards as Custom GPT knowledge.

## How it fits

Knowledge files provide reference material while behavior and workflow rules stay in instructions and Skill files.

For this GPT, `custom-gpt/instructions.md` exceeds the GPT Instructions field limit. Task 6.3 may upload that repo-versioned instructions file as knowledge when the GPT Instructions field explicitly references it.

## In scope

- Identify MLP-relevant knowledge files.
- Ensure knowledge files are versioned in the repo.
- Upload only concise, text-forward reference files.
- Ensure the GPT can state which standards were applied.

## Out of scope

- Hidden non-repo knowledge.
- Large raw documentation dumps.
- API connectors.
- Web browsing.

## Definition of done for MLP

- [x] GPT knowledge includes only MLP-relevant files.
- [x] Knowledge files are versioned in repo.
- [x] GPT can answer which standards were applied.
- [x] GPT does not rely on hidden, non-repo instructions.
