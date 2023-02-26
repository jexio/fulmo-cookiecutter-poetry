"""Post generation hooks."""
from __future__ import annotations

import shutil
from pathlib import Path

PROJECT_DIR = Path.cwd()
PROJECT_TESTS = PROJECT_DIR / Path("tests")
PROJECT_SRC = PROJECT_DIR / Path("{{ cookiecutter.project_slug }}")


def remove_file(filepath: str | Path) -> None:
    """Remove a file from the file system.

    Args:
    ----
        filepath: Path to file.
    """
    Path.unlink(PROJECT_DIR / filepath)


def add_symlink(path: Path, target: str | Path, target_is_directory: bool = False) -> None:
    """Add symbolic link to target.

    Args:
    ----
        path: Path to file.
        target: Target path.
        target_is_directory: It must be True if `target` is directory.
    """
    if path.is_symlink():
        path.unlink()
    path.symlink_to(target, target_is_directory)


def remove_dir(directory_path: str | Path) -> None:
    """Remove a directory from the file system.

    Args:
    ----
        directory_path:
    """
    directory_path = str(PROJECT_DIR / directory_path)
    shutil.rmtree(directory_path)


if __name__ == "__main__":
    if "No command-line interface" in "{{cookiecutter.command_line_interface}}":
        remove_file(PROJECT_TESTS / "test_cli.py")
        remove_file(PROJECT_SRC / "cli.py")

    if "{{cookiecutter.include_github_actions}}" != "y":
        remove_dir(".github")
    else:
        if "{{cookiecutter.mkdocs}}" != "y" and "{{cookiecutter.publish_to}}" == "none":
            remove_file(".github/workflows/on-release-main.yml")

    if "{{cookiecutter.mkdocs}}" != "y":
        remove_dir("docs")
        remove_file("mkdocs.yml")

    if "{{cookiecutter.codecov}}" != "y":
        remove_file("codecov.yaml")
        if "{{cookiecutter.include_github_actions}}" == "y":
            remove_file(".github/workflows/validate-codecov-config.yml")
