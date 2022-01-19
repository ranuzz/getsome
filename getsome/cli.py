import sys
import click
from getsome.core.main import run


@click.command()
@click.option('--add', default="", help='Add a new link')
@click.option('--rm', default="", help='Remove an existing link')
def main(add, rm):
    run(add, rm)
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
