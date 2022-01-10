"""Console script for getsome."""
import sys
import click
from getsome.core.main import run


@click.command()
@click.option('--lc', default=-1, help='Number of links')
@click.option('--verbose', default=False, help='Verbose mode')
def main(lc, verbose, args=None):
    """Console script for getsome."""
    # click.echo("GetSome !")
    run(lc, verbose)
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
