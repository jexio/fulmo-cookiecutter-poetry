.PHONY: install
install: ## Install the poetry environment
	@echo "🚀 Creating virtual environment using pyenv and poetry"
	@poetry install
	@poetry shell

.PHONY: pre-commit-install
pre-commit-install: ## Install pre-commit hooks
	@echo "🚀 Install pre-commit hooks"
	@poetry run pre-commit install --hook-type commit-msg --hook-type pre-push

.PHONY: check
check: ## Run code quality tools.
	@echo "🚀 Checking Poetry lock file consistency with 'pyproject.toml': Running poetry lock --check"
	@poetry lock --check
	@echo "🚀 Linting code: Running pre-commit"
	@poetry run pre-commit run -a
	@poetry run duty check
	@poetry run duty check_docstring_coverage
	@poetry run duty check_docs

.PHONY: test
test: ## Test the code with pytest
	@echo "🚀 Testing code: Running pytest"
{%- if cookiecutter.codecov == "y"%}
	@poetry run duty test
{%- else %}
	@poetry run pytest --doctest-modules
{%- endif%}

.PHONY: build
build: clean-build ## Build wheel file using poetry
	@echo "🚀 Creating wheel file"
	@poetry build

.PHONY: clean
clean-build: ## clean build, test and linting artifacts
	@poetry run duty clean

{%- if cookiecutter.publish_to == "pypi"%}

.PHONY: publish
publish: ## publish a release to pypi.
	@echo "🚀 Publishing: Dry run."
	@poetry config pypi-token.pypi $(PYPI_TOKEN)
	@poetry publish --dry-run
	@echo "🚀 Publishing."
	@poetry publish

.PHONY: build-and-publish
build-and-publish: build publish ## Build and publish.
{%- endif%}

{%- if cookiecutter.mkdocs == "y" %}

.PHONY: docs-build
docs-build: ## Build the documentation locally
	@poetry run duty docs

.PHONY: docs-test
docs-test: ## Test if documentation can be built without warnings or errors
	@poetry run duty check_docs

.PHONY: docs
docs: ## Build and serve the documentation
	@poetry run duty serve_docs

{%- endif %}

.PHONY: help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

.DEFAULT_GOAL := help
