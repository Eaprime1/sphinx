---
human_author: Perspective Project
ai_partner: Claude (Anthropic)
creation_mode: manual
---

# GravityWell

| Field | Value |
|---|---|
| Entity type | `GravityWell` |
| Storage location | Box |
| Ka signature | Unique identifier encoding well type + creation timestamp |
| Relates to | {doc}`pool`, {doc}`aperture`, {doc}`sparkle` |

## Description

A GravityWell is a stable knowledge attractor. It is the destination content flows toward
after passing through the {term}`Aperture`. Wells are stored in Box.

## Fields

`id`
: String. Unique identifier. Format: `GW-{type_code}-{timestamp}`.

`ka_signature`
: String. The runic Ka encoding for this well. Encodes type, creation context, and lineage.

`type`
: Enum. One of: `Gravitar`, `Magnetar`, `Pulsar`, `Void`.

`state`
: Enum. One of: `Active`, `Dormant`, `Collapsed`.

`pools`
: List of {doc}`pool` IDs. The pools that feed this well.

`aperture`
: Reference to the {doc}`aperture` governing this well's inbound threshold.

`sparkles`
: List of {doc}`sparkle` IDs. Completed journeys compressed from this well.

`created_at`
: ISO 8601 datetime.

`collapsed_at`
: ISO 8601 datetime or null. Set when state transitions to `Collapsed`.

## State transitions

```
Active ──► Dormant ──► Active      (reactivation)
Active ──► Dormant ──► Collapsed   (terminal)
Active ──► Collapsed               (immediate collapse)
```

Collapsed is a terminal state. A collapsed well cannot return to Active or Dormant.

## Well type behavior

| Type | Inbound | Outbound | Lifecycle |
|---|---|---|---|
| Gravitar | High pull | Minimal | Long-lived |
| Magnetar | High pull | High emission | Project-scoped |
| Pulsar | Cyclic | None between pulses | Rhythmic |
| Void | Absorbing | None | Terminal archive |

## See also

- {doc}`/explanation/gravity-well-cosmology`
- {term}`Gravity Well` in {doc}`/glossary`
