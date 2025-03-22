# Script: 023_custom_url_validator.py

import click

class URLType(click.ParamType):
    """
    Custom Click parameter type for validating URLs.
    Ensures the URL starts with 'http://' or 'https://'.
    """
    name = "url"

    def convert(self, value, param, ctx):
        # Custom validation for URL
        if not value.startswith("http://") and not value.startswith("https://"):
            self.fail(f"{value} is not a valid URL. URLs must start with 'http://' or 'https://'.", param, ctx)
        return value

@click.command()
@click.option("--url", prompt="Input URL", help="The URL to check.", type=URLType())
def cli(url):
    """
    CLI tool to validate and echo a provided URL.
    
    Options:
        --url: Input the URL to validate.
    """
    click.echo(f"URL is {url}")

if __name__ == "__main__":
    cli()
