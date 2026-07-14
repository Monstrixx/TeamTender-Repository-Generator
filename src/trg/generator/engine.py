"""
Generator Engine

Core automation engine for TRG.
"""

from rich.console import Console


class GeneratorEngine:
    """
    Core Generator Engine.
    """

    def __init__(self):
        self.console = Console()

    def info(self, message: str):
        """Display information."""
        self.console.print(f"[cyan]{message}[/cyan]")