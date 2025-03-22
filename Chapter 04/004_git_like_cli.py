# Script: 004_git_like_cli.py

import argparse

def main():
    """
    Main function to implement a Git-like CLI with subcommands.
    Supports 'add' to add files and 'commit' to commit changes.
    """
    # Create the main parser
    parser = argparse.ArgumentParser(description='A sample CLI tool with subcommands')
    subparsers = parser.add_subparsers(dest='command', help='Available commands')

    # Adding sub-command 'add'
    add_parser = subparsers.add_parser('add', help='Add file')
    add_parser.add_argument('filename', help='Name of the file to add')

    # Adding sub-command 'commit'
    commit_parser = subparsers.add_parser('commit', help='Commit changes')
    commit_parser.add_argument('message', help='Commit message')

    # Parse the arguments
    args = parser.parse_args()

    # Handle the subcommands
    if args.command == 'add':
        print(f"Adding file: {args.filename}")
        # TODO: Add logic for handling file addition
    elif args.command == 'commit':
        print(f"Committing with message: {args.message}")
        # TODO: Add logic for handling commit action
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
