# Script: 012_cloud_infra_cli.py

import argparse

# Function for setting up infrastructure
def setup_infra(args):
    """
    Set up infrastructure in the specified region.
    """
    print(f"Setting up infrastructure in {args.region}")

# Function for monitoring
def monitor_infra(args):
    """
    Monitor infrastructure at a specified interval.
    """
    print(f"Monitoring infrastructure with an interval of {args.interval} minutes")

# Function for securing infrastructure
def secure_infra(args):
    """
    Secure the infrastructure.
    """
    print("Securing infrastructure...")

# Main function to parse arguments
def main():
    """
    Main function to define and handle CLI commands for managing cloud infrastructure.
    """
    # Create the top-level parser
    parser = argparse.ArgumentParser(prog='cloudman', description='Cloud infrastructure management CLI tool')

    # Create subparsers to handle different subcommands
    subparsers = parser.add_subparsers(help='Sub-command help')

    # Create the parser for the 'setup' command
    parser_setup = subparsers.add_parser('setup', help='Set up infrastructure')
    parser_setup.add_argument('region', type=str, help='Region to set up infrastructure')
    parser_setup.set_defaults(func=setup_infra)

    # Create the parser for the 'monitor' command
    parser_monitor = subparsers.add_parser('monitor', help='Monitor infrastructure')
    parser_monitor.add_argument('interval', type=int, help='Interval in minutes for monitoring')
    parser_monitor.set_defaults(func=monitor_infra)

    # Create the parser for the 'secure' command
    parser_secure = subparsers.add_parser('secure', help='Secure infrastructure')
    parser_secure.set_defaults(func=secure_infra)

    # Parse the arguments and call the appropriate function
    args = parser.parse_args()
    if hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
