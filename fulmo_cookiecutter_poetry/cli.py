"""Cli ro run cookiecutter."""
import os
from pathlib import Path


def main() -> None:
    """Run cookiecutter."""
    cwd = Path(__file__).parent
    package_dir = Path(cwd / "..").resolve()
    os.system(f"cookiecutter {package_dir}")
