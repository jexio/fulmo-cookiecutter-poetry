"""Test section."""
from __future__ import annotations

import os
import shlex
import subprocess
from contextlib import contextmanager
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Generator

    from pytest_cookies.plugin import Cookies


@contextmanager
def run_within_dir(path: str | Path) -> Generator[None, None, None]:
    """Execute code from inside the given directory.

    Args:
        path: A path to the directory where the command is being run.

    Yields:
        None.
    """
    oldpwd = Path.cwd()
    try:
        os.chdir(path)
        yield
    finally:
        os.chdir(oldpwd)


def file_contains_text(file: str, text: str) -> bool:
    """Whether the `file` contains `text` or not."""
    with Path(file).open() as f:
        return f.read().find(text) != -1


def test_bake_project(cookies: Cookies) -> None:
    """Test bake the project with the default values."""
    result = cookies.bake(extra_context={"project_name": "my-project"})

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_path.name == "my-project"
    assert result.project_path.is_dir()


def test_using_pytest(cookies: Cookies, tmp_path: Path) -> None:
    """Test pytest section."""
    with run_within_dir(tmp_path):
        result = cookies.bake()

        # Assert that project was created.
        assert result.exit_code == 0
        assert result.exception is None
        assert result.project_path.name == "example-project"
        assert result.project_path.is_dir()

        # Install the poetry environment and run the tests.
        with run_within_dir(str(result.project_path)):
            assert subprocess.check_call(shlex.split("poetry install --no-interaction")) == 0
            assert subprocess.check_call(shlex.split("poetry run make test")) == 0


def test_cicd_contains_pypi_secrets(cookies: Cookies, tmp_path: Path) -> None:
    """Test ci/cd section."""
    with run_within_dir(tmp_path):
        result = cookies.bake(extra_context={"publish_to": "pypi"})
        assert result.exit_code == 0
        assert file_contains_text(f"{result.project_path}/.github/workflows/on-release-main.yml", "PYPI_TOKEN")
        assert file_contains_text(f"{result.project_path}/Makefile", "build-and-publish")


def test_dont_publish(cookies: Cookies, tmp_path: Path) -> None:
    """Test publish section."""
    with run_within_dir(tmp_path):
        result = cookies.bake(extra_context={"publish_to": "none"})
        assert result.exit_code == 0
        assert not file_contains_text(
            f"{result.project_path}/.github/workflows/on-release-main.yml",
            "make build-and-publish",
        )


def test_mkdocs(cookies: Cookies, tmp_path: Path) -> None:
    """Test mkdocs section."""
    with run_within_dir(tmp_path):
        result = cookies.bake(extra_context={"mkdocs": "y"})
        assert result.exit_code == 0
        assert file_contains_text(f"{result.project_path}/.github/workflows/on-release-main.yml", "mkdocs gh-deploy")
        assert file_contains_text(f"{result.project_path}/Makefile", "docs:")
        assert Path(f"{result.project_path}/docs").is_dir()


def test_not_mkdocs(cookies: Cookies, tmp_path: Path) -> None:
    """Test not mkdocs section."""
    with run_within_dir(tmp_path):
        result = cookies.bake(extra_context={"mkdocs": "n"})
        assert result.exit_code == 0
        assert not file_contains_text(
            f"{result.project_path}/.github/workflows/on-release-main.yml",
            "mkdocs gh-deploy",
        )
        assert not file_contains_text(f"{result.project_path}/Makefile", "docs:")
        assert not Path(f"{result.project_path}/docs").is_dir()


def test_tox(cookies: Cookies, tmp_path: Path) -> None:
    """Test tox section."""
    with run_within_dir(tmp_path):
        result = cookies.bake()
        assert result.exit_code == 0
        assert file_contains_text(f"{result.project_path}/.github/workflows/main.yml", "pip install tox tox-gh-actions")
        assert Path(f"{result.project_path}/tox.ini").is_file()
        assert file_contains_text(f"{result.project_path}/tox.ini", "[tox]")


def test_codecov(cookies: Cookies, tmp_path: Path) -> None:
    """Test codecov section."""
    with run_within_dir(tmp_path):
        result = cookies.bake()
        assert result.exit_code == 0
        assert Path(f"{result.project_path}/codecov.yaml").is_file()
        assert Path(f"{result.project_path}/.github/workflows/validate-codecov-config.yml").is_file()


def test_not_codecov(cookies: Cookies, tmp_path: Path) -> None:
    """Test not codecov section."""
    with run_within_dir(tmp_path):
        result = cookies.bake(extra_context={"codecov": "n"})
        assert result.exit_code == 0
        assert not Path(f"{result.project_path}/codecov.yaml").is_file()
        assert not Path(f"{result.project_path}/.github/workflows/validate-codecov-config.yml").is_file()


def test_remove_release_workflow(cookies: Cookies, tmp_path: Path) -> None:
    """Test release workflow section."""
    with run_within_dir(tmp_path):
        result = cookies.bake(extra_context={"publish_to": "none", "mkdocs": "y"})
        assert result.exit_code == 0
        assert Path(f"{result.project_path}/.github/workflows/on-release-main.yml").is_file()

        result = cookies.bake(extra_context={"publish_to": "none", "mkdocs": "n"})
        assert result.exit_code == 0
        assert not Path(f"{result.project_path}/.github/workflows/on-release-main.yml").is_file()
