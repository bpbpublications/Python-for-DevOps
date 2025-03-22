# Script: 021_click_greeting.py

import click

@click.command()
@click.argument('name')
@click.option('--greeting', default='Hello', help='Change the greeting.')
def greet(name, greeting):
    """
    CLI tool to greet a user with a customizable message.
    
    Arguments:
        name (str): The name of the person to greet.
    Options:
        --greeting: Customize the greeting message (default is 'Hello').
    """
    click.echo(f"{greeting}, {name}!")

if __name__ == "__main__":
    greet()
