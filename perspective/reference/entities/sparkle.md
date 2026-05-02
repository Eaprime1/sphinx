---
human_author: Perspective Project
ai_partner: Claude (Anthropic)
creation_mode: manual
---

# Sparkle

| Field | Value |
|---|---|
| Entity type | `Sparkle` |
| Storage location | Well Sparkle registry (Box) |
| Character | Terminal — the compressed essence of a completed journey |

## Description

A Sparkle is what a document becomes after its journey is complete. It is not a living
document — it does not get edited. It is a permanent, compressed, AI-readable record of
a knowledge journey, encoded via {term}`Runyatr`.

## Fields

`id`
: String. Unique identifier. Format: `SPK-{well_id}-{sequence}`.

`source_well`
: Reference to the {doc}`gravity-well` this Sparkle emerged from.

`runyatr_code`
: String. The runic compression code encoding the journey. Format:
  `{well_type}:{quadrant}:{concept}:v{version}`.

`origin_path`
: The original document path before sparklization.

`human_authors`
: List of human author identifiers who contributed to the journey.

`ai_partners`
: List of AI model identifiers (e.g., `claude-sonnet-4-6`) who contributed.

`creation_mode`
: Enum. One of: `manual`, `generated`, `sparklized`.

`sparklized_at`
: ISO 8601 datetime. When sparklization occurred.

`pressure_at_crossing`
: Float. The pressure score the content carried when it crossed the Aperture.

`is_monarch`
: Boolean. `true` if this Sparkle is a {term}`Monarch` (null journey / empty vector).
  Default: `false`.

## Reading a Runyatr code

The Runyatr code is structured as:

```
GW:REF:APERTURE:v1.2
│   │   │        │
│   │   │        └── Version of this Sparkle in its well
│   │   └─────────── Concept/topic encoded
│   └─────────────── Diátaxis quadrant (REF, TUT, HOW, EXP)
└─────────────────── Well type (GW = GravityWell, PL = Pool)
```

## The Monarch Sparkle

A {term}`Monarch` is a Sparkle where `is_monarch = true`. It represents a journey that
was initiated but produced no content worth compressing. The Monarch preserves the *fact*
of the attempt without fabricating substance.

Monarchs are important: they prevent the system from re-attempting journeys that have
already been found empty.

## See also

- {doc}`/explanation/sparkles-and-runic-compression`
- {term}`Sparkle` in {doc}`/glossary`
- {term}`Runyatr` in {doc}`/glossary`
- {term}`Monarch` in {doc}`/glossary`
