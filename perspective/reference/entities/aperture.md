---
human_author: Perspective Project
ai_partner: Claude (Anthropic)
creation_mode: manual
---

# Aperture

| Field | Value |
|---|---|
| Entity type | `Aperture` |
| Governs | Transition from {doc}`pool` to {doc}`gravity-well` |
| Ka signature | Encoded with source pool ID + target well ID |

## Description

An Aperture governs the threshold between a {term}`Pool` and a {term}`Gravity Well`.
It defines the conditions under which content may cross from liminal to canonical.

## Fields

`id`
: String. Unique identifier. Format: `AP-{pool_id}-{well_id}`.

`source_pool`
: Reference to the {doc}`pool` on the inbound side.

`target_well`
: Reference to the {doc}`gravity-well` on the outbound side.

`pressure_threshold`
: Float (0.0–1.0). The minimum accumulated pressure required for content to cross.
  Default: `0.7`.

`state`
: Enum. One of: `Open`, `Closed`, `Sealed`.

`ethics_flags`
: List of strings. Tags that block crossing regardless of pressure. Examples:
  `private`, `draft-only`, `embargoed`.

`automation_trigger`
: Optional. Reference to an automation rule (Zapier/IFTTT) that can open the Aperture
  when threshold conditions are met.

`opened_at`
: ISO 8601 datetime or null. Last time the Aperture transitioned to `Open`.

`sealed_at`
: ISO 8601 datetime or null. Set when state becomes `Sealed` (permanent close).

## State transitions

```
Closed ──► Open    (threshold met, ethics clear)
Open   ──► Closed  (content passed or conditions no longer met)
Closed ──► Sealed  (deliberate permanent close)
Open   ──► Sealed  (rare — emergency close)
```

`Sealed` is terminal. A sealed Aperture cannot reopen.

## Pressure calculation

Pressure is accumulated per content item in the source pool:

- Each cross-reference from another document: `+0.1`
- Each review/engagement by a human author: `+0.15`
- Explicit "ready" tag applied: `+0.25`
- AI partner marks as complete: `+0.1`
- Time in pool beyond 30 days without engagement: `-0.05` per week

## See also

- {doc}`/explanation/aperture-and-event-horizons`
- {term}`Aperture` in {doc}`/glossary`
