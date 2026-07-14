"""
TeamTender Repository Generator (TRG)

Main Entry Point
"""

from rich.console import Console

console = Console()


def main():
    console.print("[bold green]====================================[/bold green]")
    console.print("[bold cyan] TeamTender Repository Generator[/bold cyan]")
    console.print("[bold green]====================================[/bold green]")
    console.print("")
    console.print("Version : 0.1.0 Alpha")
    console.print("Status  : Development")
    console.print("")
    console.print("[green]TRG berhasil dijalankan.[/green]")


if __name__ == "__main__":
    main()