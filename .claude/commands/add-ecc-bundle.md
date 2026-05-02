---
name: add-ecc-bundle
description: Workflow command scaffold for add-ecc-bundle in sphinx.
allowed_tools: ["Bash", "Read", "Write", "Grep", "Glob"]
---

# /add-ecc-bundle

Use this workflow when working on **add-ecc-bundle** in `sphinx`.

## Goal

Adds a new ECC bundle for a skill or agent, including configuration, identity, skills, instincts, and agent definitions.

## Common Files

- `.claude/ecc-tools.json`
- `.claude/skills/*/SKILL.md`
- `.agents/skills/*/SKILL.md`
- `.agents/skills/*/agents/openai.yaml`
- `.claude/identity.json`
- `.codex/config.toml`

## Suggested Sequence

1. Understand the current state and failure mode before editing.
2. Make the smallest coherent change that satisfies the workflow goal.
3. Run the most relevant verification for touched files.
4. Summarize what changed and what still needs review.

## Typical Commit Signals

- Add or update .claude/ecc-tools.json
- Add or update .claude/skills/<skill>/SKILL.md
- Add or update .agents/skills/<skill>/SKILL.md
- Add or update .agents/skills/<skill>/agents/openai.yaml
- Add or update .claude/identity.json

## Notes

- Treat this as a scaffold, not a hard-coded script.
- Update the command if the workflow evolves materially.