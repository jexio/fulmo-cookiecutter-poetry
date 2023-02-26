# Makefile

The generated repository will have a `Makefile` available. A list of all
available commands that are available can be obtained by running
`make help` in the terminal. Initially, if all features are selected, the following commands are
available:

```
install              Install the poetry environment and install the pre-commit hooks.
pre-commit-install   Install pre-commit hooks.
check                Lint and check code and docstrings by running black, ruff, mypy, safety, interrogate.
test                 Test the code with pytest
build                Build wheel file using poetry
clean                clean build, test and linting artifacts
publish              publish a release to pypi.
build-and-publish    Build and publish.
docs-build           Build the documentation locally.
docs-test            Test if documentation can be built without warnings or errors.
docs                 Build and serve the documentation.
```
