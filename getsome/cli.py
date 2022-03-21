import sys
import click
from getsome.core.main import run


@click.command()
@click.option('--add', default="", help='Add a new link')
@click.option('--rm', default="", help='Remove an existing link')
@click.option('--sync/--no-sync', default=False, help='sync the feed file')
@click.option('--fetch/--no-fetch', default=False, help='fetch new links')
def main(add, rm, sync, fetch):
    run(add, rm, sync, fetch)
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
