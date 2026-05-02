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
```
