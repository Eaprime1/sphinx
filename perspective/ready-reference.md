---
human_author: Perspective Project
ai_partner: Claude (Anthropic)
creation_mode: generated
---

# Ready Reference

Quick-card for the most common operations. Each entry links to the full reference.

## Build commands

```bash
# from inside perspective/

make html          # build HTML site → _build/html/index.html
make epub          # build ePub     → _build/epub/Perspective.epub
make latexpdf      # build PDF      → _build/latex/perspective.pdf
make serve         # build HTML and serve at http://localhost:8000
make play-html     # build play/ pool as standalone mini-site
make clean         # wipe _build/
```

Install dependencies once:

```bash
pip install -r requirements.txt
```

## Key entity types

| Entity | Storage | Character |
|---|---|---|
| {term}`Gravity Well` | Box | Stable attractor |
| {term}`Pool` | Google Drive | Liminal holding space |
| {term}`Aperture` | — (governance layer) | Threshold / gate |
| {term}`Sparkle` | Box (well registry) | Compressed journey artifact |

## Well types at a glance

| Type | Pull | Emission | Lifecycle |
|---|---|---|---|
| {term}`Gravitar` | Highest | Minimal | Permanent |
| {term}`Magnetar` | High | High | Project-scoped |
| {term}`Pulsar` | Cyclic | None between pulses | Rhythmic |
| {term}`Void` | Absorbing | None | Terminal |

## Well states

`Active` → `Dormant` → `Collapsed` (terminal)

## Aperture pressure scoring

| Event | Pressure |
|---|---|
| Cross-reference from another doc | +0.1 |
| Human author engagement | +0.15 |
| Explicit "ready" tag | +0.25 |
| AI partner marks complete | +0.1 |
| 30+ days without engagement | −0.05/week |

Default crossing threshold: **0.7**

## Runyatr code format

```
GW:REF:APERTURE:v1.2
│   │   │        └── Version
│   │   └─────────── Concept
│   └─────────────── Quadrant (REF / TUT / HOW / EXP)
└─────────────────── Well type
```

## MyST quick reference

```markdown
{term}`Gravity Well`          ← glossary link
{doc}`/explanation/index`     ← page link (absolute)
{doc}`reference/entities/aperture`   ← page link (relative)
{ref}`section label`          ← section link

:::{note}
Content
:::

:::{admonition} Title
Content
:::
```

## Diátaxis quadrant assignments

| Content type | Quadrant | Directory |
|---|---|---|
| Step-by-step learning journey | Tutorial | `tutorials/` |
| Task recipe with clear goal | How-to | `how-to/` |
| Conceptual / philosophical | Explanation | `explanation/` |
| Precise field definitions | Reference | `reference/` |
| Draft / experimental | Pool | `play/` |

---

♓

