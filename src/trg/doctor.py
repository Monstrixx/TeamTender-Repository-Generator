"""
TRG Doctor

Checks the development environment.
"""

import platform
import sys

from rich.console import Console

from trg.generator.engine import GeneratorEngine

console = Console()


def doctor():
    """Run environment diagnostics."""

    engine = GeneratorEngine()

    console.print("[bold cyan]TRG Doctor[/bold cyan]")
    console.print()

    engine.info("Generator Engine loaded successfully.")

    console.print(f"[green]✓[/green] Python Version : {platform.python_version()}")
    console.print(f"[green]✓[/green] Python Executable : {sys.executable}")