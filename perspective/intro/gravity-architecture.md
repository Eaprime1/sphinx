---
human_author: Perspective Project
ai_partner: Claude (Anthropic)
creation_mode: manual
---

# Gravity Architecture Overview

This page is the entry point to the Perspective architecture. It maps the key entities and
their relationships. For deep theory, see {doc}`/explanation/index`.

## The entities

The four primary entity types are:

**{term}`Gravity Well`**
: A stable attractor. Knowledge flows toward it, organizes around it, and deepens over time.
  Wells have types (Gravitar, Magnetar, Pulsar, Void) and states (Active, Dormant, Collapsed).

**{term}`Pool`**
: A liminal space. Drafts, fragments, and experimental content float here. Pools live on
  Google Drive. Content in a pool has not yet passed through the Aperture.

**{term}`Aperture`**
: The threshold between Pool and Well. Crossing the Aperture is a deliberate act — content
  becomes canonical. The Aperture has pressure thresholds and ethical constraints.

**{term}`Sparkle`**
: A compressed artifact. When a document completes its journey, it becomes a Sparkle —
  the crystallized essence, encoded with runic compression that preserves its history.

## How they connect

```
Pool (Google Drive)
    │
    │  content accumulates pressure
    ▼
Aperture ── threshold crossed ──► Gravity Well (Box)
                                        │
                                        │  journey complete
                                        ▼
                                     Sparkle
```

The {term}`Runyatr` is the runic encoding system that preserves journey history inside
Sparkles. It is the memory of how knowledge moved.

## Next steps

- **Learn by doing**: {doc}`/tutorials/index`
- **Understand deeply**: {doc}`/explanation/gravity-well-cosmology`
- **Look up a term**: {doc}`/glossary`
- **See the full entity spec**: {doc}`/reference/entities/gravity-well`
