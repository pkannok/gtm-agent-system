# Task 9.1 - Build documentation synthesis tool

## Status

Future

## Goal

Create a tool that converts developer docs into clean reference markdown.

## How it fits

Later agents need high-quality reference docs without dumping large raw web pages into the GPT.

## In scope

- Build `tools/docs_to_reference.py`.
- Process saved HTML or markdown.
- Output normalized markdown, metadata, captured date, product/version, rules, and open questions.
- Require human review before adding synthesized docs to Skill references.

## Out of scope

- Blocking the MLP.
- Automatic trust of generated reference docs.
- Live web crawling beyond active task scope.

## Definition of done for first post-MLP version

- [ ] Tool can process saved HTML or markdown.
- [ ] Output is readable.
- [ ] Output includes source and capture date.
- [ ] Human review is required before adding synthesized docs to Skill references.
