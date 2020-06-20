"""Initialize workspace for Dev-container."""
import click
from cookiecutter.main import cookiecutter

from slides_workspace import templates_dir


@click.command()
def cmd():
    click.echo("Initializing workspace...")
    cookiecutter(str(templates_dir / "revealjs"))


def main():
    cmd()
