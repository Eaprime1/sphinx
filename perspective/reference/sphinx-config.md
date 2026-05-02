---
human_author: Perspective Project
ai_partner: Claude (Anthropic)
creation_mode: manual
---

# Sphinx Configuration Reference

The `perspective/conf.py` file controls how this doc set builds. Key settings:

## Extensions

`myst_parser`
: Enables MyST Markdown as a source format. Required. All `.md` files are parsed as MyST.

`sphinx.ext.autosectionlabel`
: Auto-generates reference labels for every section heading. Allows `:ref:` links by title.
  Combined with `autosectionlabel_prefix_document = True` to namespace labels by file.

`sphinx_copybutton`
: Adds a copy button to all code blocks in HTML output.

## MyST options

`myst_enable_extensions`
: The following MyST extensions are enabled:
  - `colon_fence` — allows `:::` as an alternative to ` ``` ` for directives (cleaner in some editors)
  - `deflist` — enables definition list syntax (term / : definition)
  - `fieldlist` — enables RST-style field lists for structured metadata blocks

## Output formats

### HTML

Theme: `furo`. Run with:

```bash
make html
```

Output: `_build/html/index.html`

### ePub

```bash
make epub
```

Output: `_build/epub/Perspective.epub`

### PDF (LaTeX)

Requires a LaTeX installation (e.g., `texlive-full` on Linux, MacTeX on macOS).

```bash
make latexpdf
```

Output: `_build/latex/perspective.pdf`

## Exclude patterns

`play/**` is excluded from the main build by default. Use `make play-html` to build the
play area as a standalone mini-site.

## Adding a new extension

1. Install the package: `pip install sphinx-<name>`
2. Add to `extensions` list in `conf.py`
3. Add to `requirements.txt`
4. Document it in this page
