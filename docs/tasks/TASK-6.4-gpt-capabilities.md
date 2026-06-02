# Task 6.4 - Configure GPT capabilities

## Status

Upcoming

## Goal

Enable only the Custom GPT capabilities needed for file-in/file-out MLP use.

## How it fits

The MLP needs file handling and possibly data analysis, not external actions or live platform access.

## In scope

- Enable file handling/data analysis capability if available.
- Disable external API actions for the MLP.
- Disable unrelated capabilities.
- State live writes are out of scope.

## Out of scope

- GPT Actions.
- Apps.
- Web search.
- Image generation.
- Live GTM publishing.

## Definition of done for MLP

- [ ] GPT can accept uploaded JSON.
- [ ] GPT can produce downloadable JSON/Markdown artifacts if supported.
- [ ] No external API action is configured.
- [ ] GPT instructions explicitly state live writes are out of scope.
