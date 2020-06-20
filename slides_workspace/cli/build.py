"""Build presentation from source."""
import shutil
from pathlib import Path

import click
from sphinx.cmd.build import main as sphinx_main


@click.command()
@click.option("--clean", is_flag=True, help="Cleanup DEST dir")
@click.argument("src", type=click.Path(exists=True))
@click.argument("dest", type=click.Path())
def cmd(src, dest, clean):
    click.echo("Initializing workspace...")
    src_ = Path.cwd() / src
    dest_ = Path.cwd() / dest
    click.echo(f"Srouce: {src_}")
    click.echo(f"Output: {dest_}")
    if dest_.exists() and clean:
        shutil.rmtree(dest_)
    dest_.mkdir(parents=True, exist_ok=True)
    args = ["-b", "revealjs"]
    args += [str(src_), str(dest_)]
    sphinx_main(args)


def main():
    cmd()
