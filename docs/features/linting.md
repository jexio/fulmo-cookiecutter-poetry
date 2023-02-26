# Linting and code quality

Code can be linted and quality-checked with the command

``` bash
make check
```

Note that this requires the pre-commit hooks to be installed.

This command will run the following tools:

## black

[black](https://pypi.org/project/black/) is used to format the code, and it is configured through `pyproject.toml`:

```toml
[tool.black]
line-length = 120
include = '\.pyi?$'
target-version = ["py310"]
fast = true
```

To exclude directories or files, add an `exclude` argument to `pre-commit-config.yaml`. Note that adding an `exclude` argument to `pyproject.toml`
will not work, see also [here](https://stackoverflow.com/a/61046953/8037249).

## ruff

[ruff](https://github.com/charliermarsh/ruff) is used to check the code style, and it is configured through `pyproject.toml`:

```
[tool.ruff]
target-version = "py310"
line-length = 120
select = [
    "ALL"
]
ignore = [
    "A001",  # Variable is shadowing a Python builtin
    "ANN101",  # Missing type annotation for self
    "ANN401",  # Dynamically typed expressions (typing.Any) are disallowed
    "C901",  # Too complex
    "D105",  # Missing docstring in magic method
    "D417",  # Missing argument description in the docstring
    "E501",  # Line too long
    "PLR0911",  # Too many return statements
    "PLR0912",  # Too many branches
    "PLR0913",  # Too many arguments to function call
    "PLR0915",  # Too many statements
    "TRY003",  # Avoid specifying long messages outside the exception class
]

[tool.ruff.per-file-ignores]
"scripts/*.py" = [
    "INP001",  # File is part of an implicit namespace package
]
"tests/*.py" = [
    "ANN",  # Missing/wrong type annotations
    "ARG005",  # Unused lambda argument
    "PLR2004",  # Magic value used in comparison
    "S101",  # Use of assert detected
]
"hooks/*.py" = [
    "PLR0133", # Two constants compared in a comparison, consider replacing
    "FBT001", # Boolean positional arg in function definition
    "FBT002", # Boolean default value in function definition
]
"*/*__init__.py" = [
    "D104", # Missing docstring in public package
]

[tool.ruff.flake8-type-checking]
strict = true

[tool.ruff.flake8-quotes]
docstring-quotes = "double"

[tool.ruff.flake8-tidy-imports]
ban-relative-imports = "all"

[tool.ruff.isort]
known-first-party = ["fulmo_cookiecutter_poetry"]

[tool.ruff.pydocstyle]
convention = "google"
```

# mypy

[mypy](https://mypy.readthedocs.io/en/stable/) is used for static type checking, and it's configuration and can be edited in `pyproject.toml`.

```toml
[tool.mypy]
warn_return_any = "True"
warn_unused_ignores = "True"
show_error_codes = "True"
exclude = [
    '{{cookiecutter.project_name}}'
]
```
