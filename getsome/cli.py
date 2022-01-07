"""Console script for getsome."""
import sys
import click
from getsome.getsome import readFeeds

@click.command()
@click.option('--lc', default=-1, help='Number of links')
def main(lc, args=None):
    """Console script for getsome."""
    click.echo("GetSome !")
    readFeeds(lc)
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
