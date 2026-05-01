---
human_author: Perspective Project
ai_partner: Claude (Anthropic)
creation_mode: generated
---

# AI-First Authoring

Perspective is built AI-first: AI models are collaborators from the beginning, not cleanup
tools at the end. This page explains what that means in practice.

## What "AI-first" means here

AI-first does not mean AI-only. It means:

1. **The authoring format is AI-friendly.** MyST Markdown is chosen because AI models
   handle Markdown natively. The directive vocabulary (`:term:`, `{note}`, `{toctree}`) is
   small enough to teach in a prompt.

2. **AI contributions are visible.** Every page carries front-matter recording `ai_partner`
   and `creation_mode`. Nothing is hidden.

3. **Prompts are documented.** Where a section was generated from a specific prompt, that
   prompt appears in a `{note}` block labeled **Prompt used**. This makes the AI a documented
   tool rather than a ghost writer.

4. **AI voice is preserved.** `{admonition}` blocks labeled **Perspective's notes** carry
   AI commentary on structure or reasoning — the collaboration itself becomes part of the
   record.

## Working with AI partners

When authoring with an AI:

- Provide the {doc}`gravity-architecture` overview as context before asking for content.
- Ask the AI to use `:term:` roles when referencing {doc}`/glossary` terms so cross-references
  are wired from the start.
- Place AI-generated drafts in {file}`play/` first. Graduate them through the Aperture into
  stable quadrants once they've accumulated enough shape.

See {doc}`/ai-playbook` for the full convention set.
