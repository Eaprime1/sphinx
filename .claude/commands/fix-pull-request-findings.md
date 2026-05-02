---
name: fix-pull-request-findings
description: Workflow command scaffold for fix-pull-request-findings in sphinx.
allowed_tools: ["Bash", "Read", "Write", "Grep", "Glob"]
---

# /fix-pull-request-findings

Use this workflow when working on **fix-pull-request-findings** in `sphinx`.

## Goal

Applies targeted fixes to specific files in response to pull request review comments or automated findings.

## Common Files

- `.claude/homunculus/instincts/inherited/*-instincts.yaml`
- `.codex/AGENTS.md`
- `.claude/skills/*/SKILL.md`
- `.codex/config.toml`
- `.agents/skills/*/agents/openai.yaml`

## Suggested Sequence

1. Understand the current state and failure mode before editing.
2. Make the smallest coherent change that satisfies the workflow goal.
3. Run the most relevant verification for touched files.
4. Summarize what changed and what still needs review.

## Typical Commit Signals

- Identify file(s) needing fixes from PR feedback
- Edit the relevant file(s) to address the finding
- Commit with a message referencing the fix

## Notes

- Treat this as a scaffold, not a hard-coded script.
- Update the command if the workflow evolves materially.