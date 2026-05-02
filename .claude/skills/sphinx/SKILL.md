```markdown
# sphinx Development Patterns

> Auto-generated skill from repository analysis

## Overview
This skill teaches the core development patterns and conventions used in the `sphinx` Python codebase. You'll learn about file naming, import/export styles, commit patterns, and how to write and run tests. This guide also provides step-by-step instructions for common workflows and suggested commands to streamline your development process.

## Coding Conventions

### File Naming
- **CamelCase** is used for file names.
  - Example: `MyModule.py`, `DataProcessor.py`

### Import Style
- **Relative imports** are preferred within the codebase.
  - Example:
    ```python
    from .utils import HelperClass
    from ..models import DataModel
    ```

### Export Style
- **Named exports** are used to control what is available when importing from a module.
  - Example:
    ```python
    __all__ = ['MyClass', 'my_function']
    ```

### Commit Patterns
- **Freeform commit messages** (no strict prefixing)
- **Average length:** ~60 characters

  Example:
  ```
  Fix bug in data processing for edge cases
  ```

## Workflows

### Adding a New Module
**Trigger:** When you need to add new functionality to the codebase  
**Command:** `/add-module`

1. Create a new file using CamelCase naming (e.g., `NewFeature.py`).
2. Implement your classes and functions.
3. Use relative imports to reference other modules.
4. Add your exports to the `__all__` list.
5. Write corresponding test files (see Testing Patterns).
6. Commit your changes with a clear, descriptive message.

### Importing from Other Modules
**Trigger:** When you need to use code from another module in the repository  
**Command:** `/import-module`

1. Use relative imports to reference the required module.
    ```python
    from .otherModule import SomeClass
    ```
2. Ensure the target module lists the exported names in `__all__`.

### Writing and Running Tests
**Trigger:** When you add or modify code and need to ensure correctness  
**Command:** `/run-tests`

1. Create a test file in `tests/` following the `test_*.py` naming pattern (e.g., `tests/test_my_module.py`).
2. Implement your test cases using `pytest`.
3. Run the test suite with `pytest`.
4. Run your tests and ensure they pass before committing.

## Testing Patterns

- **Test files** follow the pattern: `tests/test_*.py` (e.g., `tests/test_data_processor.py`)
- **Testing framework:** `pytest`
- **Test structure:** Place tests in the dedicated `tests/` directory.

  Example test file:
  ```python
  from sphinx.my_module import MyClass

  def test_feature():
      obj = MyClass()
      assert obj.some_method()
  ```

## Commands
| Command        | Purpose                                           |
|----------------|--------------------------------------------------|
| /add-module    | Add a new module following codebase conventions  |
| /import-module | Import code from another module using relative imports |
| /run-tests     | Run all tests in the codebase                    |

This skill teaches you the core development patterns, coding conventions, and collaborative workflows used in the `sphinx` Python codebase. While the repository is primarily Python and does not use a formal web framework, it features structured documentation, configuration management, and an emphasis on extensibility (notably via Sphinx autodoc extensions). You will learn how to contribute new skills or agents, address pull request feedback, manage documentation merges, and maintain build and extension scripts.

---

## Coding Conventions

**File Naming**
- Uses snake_case for Python files and directories.
    - Example: `application.py`, `ext/autodoc/_generate.py`

**Import Style**
- Absolute imports are commonly preferred within modules.
    - Example:
      ```python
      from sphinx.util import logging
      ```

**Export Style**
- Named exports are used; avoid wildcard (`*`) exports.
    - Example:
      ```python
      def build_docs():
          ...
      __all__ = ['build_docs']
      ```

**Commit Messages**
- Mixed types, but commonly use the `feat` prefix.
- Keep messages concise (~51 characters on average).
    - Example: `feat: add support for new autodoc option`

---

## Workflows

### Add ECC Bundle
**Trigger:** When introducing a new skill or agent bundle to the system  
**Command:** `/add-ecc-bundle`

1. Add or update `.claude/ecc-tools.json` with the new bundle.
2. Add or update `.claude/skills/<skill>/SKILL.md` to document the skill.
3. Add or update `.agents/skills/<skill>/SKILL.md` for agent-specific documentation.
4. Add or update `.agents/skills/<skill>/agents/openai.yaml` for agent configuration.
5. Add or update `.claude/identity.json` with identity information.
6. Add or update `.codex/config.toml` for configuration.
7. Add or update `.codex/AGENTS.md` to register the agent.
8. Add or update `.codex/agents/*.toml` for agent definitions.
9. Add or update `.claude/homunculus/instincts/inherited/<skill>-instincts.yaml` for inherited instincts.

**Example directory structure:**
```
.claude/
  ecc-tools.json
  skills/
    mySkill/
      SKILL.md
  identity.json
  homunculus/
    instincts/
      inherited/
        mySkill-instincts.yaml
.agents/
  skills/
    mySkill/
      SKILL.md
      agents/
        openai.yaml
.codex/
  config.toml
  AGENTS.md
  agents/
    mySkill.toml
```

---

### Fix Pull Request Findings
**Trigger:** When addressing code review or automated PR feedback  
**Command:** `/fix-pr-finding`

1. Identify files needing fixes from PR feedback.
2. Edit the relevant files to address the comments or findings.
3. Commit changes with a message referencing the fix.
    - Example: `fix: address typo in SKILL.md for mySkill`

**Common files:**
- `.claude/homunculus/instincts/inherited/*-instincts.yaml`
- `.codex/AGENTS.md`
- `.claude/skills/*/SKILL.md`
- `.codex/config.toml`
- `.agents/skills/*/agents/openai.yaml`

---

### Merge Multi-File Documentation Changes
**Trigger:** When merging a feature or documentation branch into main  
**Command:** `/merge-docs`

1. Update multiple documentation and configuration files (e.g., `.md`, `.toml`, `.py`, `Makefile`, `requirements.txt`).
2. Merge the branch into `main` or a feature branch.
3. Resolve any merge conflicts, especially in documentation and config files.

**Example files:**
- `perspective/Makefile`
- `perspective/glossary.md`
- `perspective/requirements.txt`
- `perspective/reference/entities/aperture.md`
- `.ruff.toml`

---

### Autodoc Generator Fix
**Trigger:** When fixing bugs or updating the Sphinx autodoc extension generator  
**Command:** `/fix-autodoc-generator`

1. Edit `sphinx/ext/autodoc/_generate.py` to fix issues or add features.
2. Commit changes, optionally with co-authorship if collaborating.
    - Example commit: `fix: update autodoc generator for new options`

**Code Example:**
```python
# sphinx/ext/autodoc/_generate.py
def generate_docs():
    # Updated logic here
    pass
```

---

### Makefile Suppress Warnings Fix
**Trigger:** When resolving build warnings or configuration issues in the Makefile  
**Command:** `/fix-makefile-warnings`

1. Edit `perspective/Makefile` to fix `suppress_warnings` syntax or Python variable duplication.
2. Commit changes with a descriptive message.
    - Example: `fix: correct suppress_warnings in Makefile`

**Snippet:**
```makefile
SPHINXOPTS    = -W --keep-going -n
suppress_warnings = reference
```

---

## Testing Patterns

- **Framework:** `pytest`.
- **Location:** Tests live in the dedicated `tests/` directory.
- **Style:** Test files follow the `tests/test_*.py` pattern and use descriptive `test_*` function names.

**Example:**
```python
# tests/test_config.py
def test_parse_config_valid():
    ...
```

---

## Commands

| Command                | Purpose                                                         |
|------------------------|-----------------------------------------------------------------|
| /add-ecc-bundle        | Add a new ECC bundle for a skill or agent                       |
| /fix-pr-finding        | Address code review or automated PR feedback                    |
| /merge-docs            | Merge branches with large documentation/configuration updates   |
| /fix-autodoc-generator | Fix or update the Sphinx autodoc extension generator script     |
| /fix-makefile-warnings | Fix Makefile targets related to Sphinx build warnings/config    |
```
