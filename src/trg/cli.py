import typer

from trg.version import APP_NAME, VERSION, STATUS
from trg.doctor import doctor
from trg.generator.project import ProjectGenerator

app = typer.Typer(
    help=APP_NAME,
    no_args_is_help=True,
)


@app.command()
def version():
    """Show application version."""
    typer.echo(APP_NAME)
    typer.echo(f"Version : {VERSION}")
    typer.echo(f"Status  : {STATUS}")


@app.command()
def init(project_name: str):
    """Create a new project."""

    generator = ProjectGenerator()
    generator.create(project_name)

    typer.echo(f"Project '{project_name}' created successfully.")


app.command()(doctor)


def run():
    app()