"""Development tasks."""

from __future__ import annotations

import os
import sys
from pathlib import Path
from typing import TYPE_CHECKING, Literal

from duty import duty
from duty.callables import black, blacken_docs, coverage, mkdocs, mypy, pytest, ruff, safety, lazy

if TYPE_CHECKING:
    from duty.context import Context

PY_SRC_PATHS = (Path(_) for _ in ("{{ cookiecutter.project_slug }}", "tests", "duties.py"))
PY_SRC_LIST = tuple(str(_) for _ in PY_SRC_PATHS)
PY_SRC = " ".join(PY_SRC_LIST)
TESTING = os.environ.get("TESTING", "0") in {"1", "true"}
CI = os.environ.get("CI", "0") in {"1", "true", "yes", ""}
WINDOWS = os.name == "nt"


@lazy("interrogate")
def interrogate(
    *src: str,
    verbose: int | None = None,
    quiet: bool | None = None,
    fail_under: float | None = None,
    exclude: str | None = None,
    ignore_init_method: bool | None = None,
    ignore_init_module: bool | None = None,
    ignore_magic: bool | None = None,
    ignore_module: bool | None = None,
    ignore_nested_functions: bool | None = None,
    ignore_nested_classes: bool | None = None,
    ignore_private: bool | None = None,
    ignore_property_decorators: bool | None = None,
    ignore_setters: bool | None = None,
    ignore_semiprivate: bool | None = None,
    ignore_regex: str | None = None,
    whitelist_regex: str | None = None,
    output: str | None = None,
    config: str | None = None,
    color: bool | None = None,
    omit_covered_files: bool | None = None,
    generate_badge: str | None = None,
    badge_format: Literal["png", "svg"] = "svg",
    badge_style: Literal[
        "flat", "flat-square", "flat-square-modified", "for-the-badge", "plastic", "social",
    ] = "flat-square-modified",
) -> None:
    """Run `interogate`.

    Args:
        src: Format the directories and file paths.
        verbose: Level of verbosity.
        quiet: Do not print output.
        fail_under: Fail when coverage % is less than a given amount.
        exclude: Exclude PATHs of files and/or directories.
        ignore_init_method: Ignore __init__ method of classes.
        ignore_init_module: Ignore __init__.py modules.
        ignore_magic: Ignore all magic methods of classes.
        ignore_module: Ignore module-level docstrings.
        ignore_nested_functions: Ignore nested functions and methods.
        ignore_nested_classes: Ignore nested classes.
        ignore_private: Ignore private classes, methods, and functions starting with two underscores.
        ignore_property_decorators: Ignore methods with property setter/getter decorators.
        ignore_setters: Ignore methods with property setter decorators.
        ignore_semiprivate: Ignore semiprivate classes, methods, and functions starting with a single underscore.
        ignore_regex: Regex identifying class, method, and function names to ignore.
        whitelist_regex: Regex identifying class, method, and function names to include.
        output: Write output to a given FILE.
        config: Read configuration from pyproject.toml or setup.cfg.
        color: Toggle color output on/off when printing to stdout.
        omit_covered_files: Omit reporting files that have 100% documentation coverage.
        generate_badge: Generate a shields.io status badge (an SVG image) in at a given file or directory.
        badge_format: File format for the generated badge.
        badge_style: Desired style of shields.io badge.
    """
    from interrogate.cli import main as interrogate

    cli_args: list[str] = list(src)

    if verbose:
        cli_args.append("--verbose")
        cli_args.append(str(verbose))

    if quiet:
        cli_args.append("--quiet")

    if fail_under:
        cli_args.append("--fail-under")
        cli_args.append(str(fail_under))

    if exclude:
        cli_args.append("--exclude")
        cli_args.append(exclude)

    if ignore_init_method:
        cli_args.append("--ignore-init-method")

    if ignore_init_module:
        cli_args.append("--ignore-init-module")

    if ignore_magic:
        cli_args.append("--ignore-magic")

    if ignore_module:
        cli_args.append("--ignore-module")

    if ignore_nested_functions:
        cli_args.append("--ignore-nested-functions")

    if ignore_nested_classes:
        cli_args.append("--ignore-nested-classes")

    if ignore_private:
        cli_args.append("--ignore-private")

    if ignore_property_decorators:
        cli_args.append("--ignore-property-decorators")

    if ignore_setters:
        cli_args.append("--ignore-setters")

    if ignore_semiprivate:
        cli_args.append("--ignore-semiprivate")

    if ignore_regex:
        cli_args.append("--ignore-regex")
        cli_args.append(ignore_regex)

    if whitelist_regex:
        cli_args.append("--whitelist-regex")
        cli_args.append(whitelist_regex)

    if output:
        cli_args.append("--output")
        cli_args.append(output)

    if omit_covered_files:
        cli_args.append("--omit-covered-files")

    if generate_badge:
        cli_args.append("--generate-badge")
        cli_args.append(generate_badge)

    if badge_format:
        cli_args.append("--badge-format")
        cli_args.append(badge_format)

    if config:
        cli_args.append("--config")
        cli_args.append(config)

    if badge_style:
        cli_args.append("--badge-style")
        cli_args.append(badge_style)

    if color is True:
        cli_args.append("--color")
    elif color is False:
        cli_args.append("--no-color")

    interrogate(cli_args)


@duty(pre=["check_quality", "check_types", "check_dependencies"])
def check(ctx: Context) -> None:  # noqa: ARG001
    """Check it all!

    Parameters:
        ctx: The context instance (passed automatically).
    """


@duty
def check_quality(ctx: Context) -> None:
    """Check the code quality.

    Parameters:
        ctx: The context instance (passed automatically).
    """
    ctx.run(
        ruff.check(*PY_SRC_LIST, config="pyproject.toml"),
        title="Checking code quality",
    )


@duty
def check_dependencies(ctx: Context) -> None:
    """Check for vulnerabilities in dependencies.

    Parameters:
        ctx: The context instance (passed automatically).
    """
    # retrieve the list of dependencies
    requirements = ctx.run(
        ["poetry", "export", "-f", "requirements.txt", "--without-hashes"],
        title="Exporting dependencies as requirements",
        allow_overrides=False,
    )

    ctx.run(safety.check(requirements), title="Checking dependencies")


@duty
def check_docs(ctx: Context) -> None:
    """Check if the documentation builds correctly.

    Parameters:
        ctx: The context instance (passed automatically).
    """
    Path("htmlcov").mkdir(parents=True, exist_ok=True)
    Path("htmlcov/index.html").touch(exist_ok=True)
    ctx.run(mkdocs.build(strict=True), title="Building documentation")


@duty
def check_types(ctx: Context) -> None:
    """Check that the code is correctly typed.

    Parameters:
        ctx: The context instance (passed automatically).
    """
    ctx.run(
        mypy.run(*PY_SRC_LIST, config_file="pyproject.toml"),
        title="Type-checking",
    )


@duty
def check_docstring_coverage(ctx: Context) -> None:
    """Interrogate a codebase for docstring coverage.

    Parameters:
        ctx: The context instance (passed automatically).
    """
    ctx.run(
        interrogate(*PY_SRC_LIST, config="pyproject.toml"),
        title="Interrogate a codebase for docstring coverage",
    )


@duty(silent=True)
def clean(ctx: Context) -> None:
    """Delete temporary files.

    Parameters:
        ctx: The context instance (passed automatically).
    """
    ctx.run("rm -rf .coverage*")
    ctx.run("rm -rf coverage.*")
    ctx.run("rm -rf .mypy_cache")
    ctx.run("rm -rf .pytest_cache")
    ctx.run("rm -rf .ruff_cache")
    ctx.run("rm -rf .tox")
    ctx.run("rm -rf tests/.pytest_cache")
    ctx.run("rm -rf build")
    ctx.run("rm -rf dist")
    ctx.run("rm -rf htmlcov")
    ctx.run("rm -rf pip-wheel-metadata")
    ctx.run("rm -rf site")
    ctx.run("find . -type d -name __pycache__ | xargs rm -rf")
    ctx.run("find . -name '*.rej' -delete")


@duty
def docs(ctx: Context) -> None:
    """Build the documentation locally.

    Parameters:
        ctx: The context instance (passed automatically).
    """
    ctx.run(mkdocs.build, title="Building documentation")


@duty
def serve_docs(ctx: Context, host: str = "127.0.0.1", port: int = 8000) -> None:
    """Serve the documentation (localhost:8000).

    Parameters:
        ctx: The context instance (passed automatically).
        host: The host to serve the docs from.
        port: The port to serve the docs on.
    """
    ctx.run(
        mkdocs.serve(dev_addr=f"{host}:{port}", strict=True),
        title="Serving documentation",
        capture=False,
    )


@duty
def format(ctx: Context) -> None:
    """Run formatting tools on the code.

    Parameters:
        ctx: The context instance (passed automatically).
    """
    ctx.run(
        ruff.check(*PY_SRC_LIST, config="pyproject.toml", fix_only=True, exit_zero=True),
        title="Auto-fixing code",
    )
    ctx.run(black.run(*PY_SRC_LIST, config="pyproject.toml"), title="Formatting code")
    ctx.run(
        blacken_docs.run(*PY_SRC_LIST, "docs", exts=["py", "md"], line_length=120),
        title="Formatting docs",
        nofail=True,
    )


@duty(silent=True, aliases=["coverage"])
def cov(ctx: Context) -> None:
    """Report coverage as text and HTML.

    Parameters:
        ctx: The context instance (passed automatically).
    """
    ctx.run(coverage.combine, nofail=True)
    ctx.run(coverage.report(rcfile="pyproject.toml"), capture=False)
    ctx.run(coverage.html(rcfile="pyproject.toml"))


@duty
def test(ctx: Context, match: str = "") -> None:
    """Run the test suite.

    Parameters:
        ctx: The context instance (passed automatically).
        match: A pytest expression to filter selected tests.
    """
    py_version = f"{sys.version_info.major}{sys.version_info.minor}"
    os.environ["COVERAGE_FILE"] = f".coverage.{py_version}"
    ctx.run(
        pytest.run("tests", config_file="pyproject.toml", select=match),
        title="Running tests",
    )
