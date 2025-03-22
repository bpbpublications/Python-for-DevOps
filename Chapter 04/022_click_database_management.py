# Script: 022_click_database_management.py

import click

@click.group()
def cli():
    """
    A CLI tool for database management.
    Provides commands to initialize or drop the database.
    """
    pass

@cli.command()
def initdb():
    """
    Command to initialize the database.
    """
    click.echo('Initialized the database')

@cli.command()
def dropdb():
    """
    Command to drop the database.
    """
    click.echo('Dropped the database')

if __name__ == "__main__":
    cli()
