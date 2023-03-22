"""Console script for imogen."""

import click


@click.command()
def main():
    """Main entrypoint."""
    click.echo("imogen")
    click.echo("=" * len("imogen"))
    click.echo("Skeleton project created by Cookiecutter PyPackage")


if __name__ == "__main__":
    main()  # pragma: no cover
