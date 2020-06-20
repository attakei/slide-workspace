"""Initialize workspace for Dev-container."""
import click


@click.command()
def cmd():
    click.echo("Initializing workspace...")


def main():
    cmd()
