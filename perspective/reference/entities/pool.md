---
human_author: Perspective Project
ai_partner: Claude (Anthropic)
creation_mode: manual
---

# Pool

| Field | Value |
|---|---|
| Entity type | `Pool` |
| Storage location | Google Drive |
| Character | Liminal — content here has not passed through the Aperture |

## Description

A Pool is the holding space for content before it becomes canonical. Pools live on Google
Drive. They are fluid, accepting, and structurally loose — the point of a Pool is to
lower the barrier to entry, not to enforce correctness.

Nothing in a Pool is permanent. Everything in a Pool is a candidate.

## Fields

`id`
: String. Unique identifier. Format: `PL-{name}-{timestamp}`.

`name`
: Human-readable label for this pool.

`drive_folder_id`
: Google Drive folder ID where this pool's content lives.

`target_well`
: Reference to the {doc}`gravity-well` this pool feeds. May be null for free-floating pools.

`aperture`
: Reference to the {doc}`aperture` governing outbound flow. May be null until a target well
  is assigned.

`content_items`
: List of content item references. Each item carries its own pressure score.

`created_at`
: ISO 8601 datetime.

## Content item pressure

Each item in a pool carries a `pressure` float (0.0–1.0). When pressure exceeds the
governing {doc}`aperture`'s `pressure_threshold`, the item is eligible to cross.

Items in a Pool are never automatically deleted. They may be:
- Graduated to the target well (crossed the Aperture)
- Archived to the {term}`Void`
- Marked as {term}`Monarch` (null journey — no sparklizable content)

## Pool types (informal)

Pools do not have a strict type system, but common patterns emerge:

| Pattern | Character |
|---|---|
| **Working pool** | Active authoring. High churn. Direct feed to a Magnetar well. |
| **Holding pool** | Waiting for the right well to be created. No aperture yet. |
| **Play pool** | Experimental. May never graduate. Equivalent to `play/` in this doc set. |
| **Intake pool** | Automated ingest from external sources (email, Zapier). |

## See also

- {doc}`/explanation/aperture-and-event-horizons`
- {term}`Pool` in {doc}`/glossary`
