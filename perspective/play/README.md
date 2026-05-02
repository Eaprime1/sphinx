# play/ — The Pool

This directory is the **pool** for this documentation project. It is the lightweight,
low-friction area for drafts, experiments, and content that isn't ready to cross the
Aperture into a stable quadrant.

## What belongs here

- Draft pages that need more development before they earn a place in `tutorials/`,
  `how-to/`, `explanation/`, or `reference/`
- Exploratory notes — ideas being tested, not yet committed
- AI-generated first passes that need human review
- Content whose Diátaxis quadrant is not yet clear

## What doesn't belong here

- Finished, reviewed content (graduate it)
- Secrets, credentials, private information
- Content that will never graduate (delete it instead — the {term}`Monarch` handles
  the memory of null journeys at the system level, not the file level)

## Rules (minimal)

1. **No front-matter required.** Files here don't need `human_author` or `ai_partner`
   headers. Add them when you graduate.
2. **No toctree required.** Files here are excluded from the main build. They won't
   break anything if they're incomplete.
3. **Name files clearly.** Use a name that describes the content, even if rough.
   `draft-aperture-ethics.md` is better than `notes.md`.

## Graduating content

When a file is ready, run through the graduation checklist in {doc}`/ai-playbook` and
move it to the appropriate quadrant. Then add it to that quadrant's `toctree`.

## Building play/ standalone

```bash
make play-html
```

Builds the play area as a standalone mini-site at `_build/play-site/html/`. Useful for
reviewing drafts in rendered form without touching the main build.
