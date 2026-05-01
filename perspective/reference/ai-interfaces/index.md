---
human_author: Perspective Project
ai_partner: Claude (Anthropic)
creation_mode: generated
---

# AI Interfaces

This section documents the exact contracts for how AI partners interact with Perspective —
inputs, outputs, and MCP routes.

:::{note}
**Stub.** This section will expand as AI interface contracts are formalized. Currently
covers the authoring interface only.
:::

## Authoring interface (Claude)

**Input context provided to Claude:**
- The {doc}`/intro/gravity-architecture` overview (orientation)
- The {doc}`/glossary` (term vocabulary)
- The target page's front-matter template (author, creation_mode)
- Any existing content in `play/` relevant to the topic

**Expected outputs:**
- MyST Markdown valid for direct inclusion in the doc tree
- `:term:` roles used for all {doc}`/glossary` terms
- YAML front-matter block at the top (`human_author`, `ai_partner`, `creation_mode`)
- `{note}` block labeled **Prompt used** when the section is fully AI-generated

**MCP routes (to be defined):**
- `perspective.pool.read` — read content from a Google Drive pool
- `perspective.well.write` — write a completed document to a Box well
- `perspective.sparkle.create` — initiate sparklization of a completed document

## Gemini interface

*To be documented.*

## Automation interfaces (Zapier / IFTTT)

*To be documented. Will cover: intake pool triggers, Aperture pressure update hooks,
sparklization triggers.*
