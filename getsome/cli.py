from email.policy import default
from math import fabs
import sys
import click
from getsome.core.main import run


@click.command()
@click.option('--add', default="", help='Add a new link')
@click.option('--rm', default="", help='Remove an existing link')
@click.option('--addlist', default="", help='Add multiple rss links from remote url')
@click.option('--addlistlocal', default="", help='Add multiple rss links from local file')
@click.option('--list/--no-list', default=False, help='list all RSS links')
@click.option('--fetch/--no-fetch', default=False, help='fetch new links')
def main(add, rm, addlist, addlistlocal, list, fetch):
    run(add, rm, addlist, addlistlocal, list, fetch)
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
