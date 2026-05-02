# ECC for Codex CLI

This document provides a repo-local ECC baseline for Codex CLI work in this repository.
This file provides the repo-local ECC baseline for Codex CLI work in this repository.

## Repo Skill

- Repo-generated Codex skill: `.agents/skills/sphinx/SKILL.md`
- Claude-facing companion skill: `.claude/skills/sphinx/SKILL.md`
- Keep user-specific credentials and private MCPs in `~/.codex/config.toml`, not in this repo.

## MCP Baseline

Treat `.codex/config.toml` as the default ECC-safe baseline for work in this repository.
The generated baseline enables GitHub, Context7, Exa, Memory, Playwright, and Sequential Thinking.

## Multi-Agent Support

- Explorer: read-only evidence gathering
- Reviewer: correctness, security, and regression review
- Docs researcher: API and release-note verification

## Workflow Files

- No dedicated workflow command files were generated for this repo.
- `.claude/commands/feature-development.md`
- `.claude/commands/add-ecc-bundle.md`
- `.claude/commands/fix-pull-request-findings.md`

Use these workflow files as reusable task scaffolds when the detected repository workflows recur.