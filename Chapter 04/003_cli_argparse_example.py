# Script: 003_cli_argparse_example.py

import argparse

def main():
    """
    Main function to demonstrate a sample CLI application using argparse.
    Processes a filename, verbosity, and logging level with defined options.
    """
    # Create the parser
    parser = argparse.ArgumentParser(description='Sample CLI Application using Argparse')

    # Define positional argument
    parser.add_argument('filename', help='The name of the file to process')

    # Define optional argument for verbosity
    parser.add_argument('-v', '--verbose', action='store_true', help='Increase output verbosity')

    # Define optional argument with choices for log level
    parser.add_argument('-l', '--loglevel', default='WARNING', 
                        choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'], 
                        help='Set the logging level')

    # Parse arguments
    args = parser.parse_args()

    # Use the arguments in the application logic
    if args.verbose:
        print("Verbose mode activated")
    print(f"Processing file: {args.filename}")
    print(f"Logging level set to {args.loglevel}")

    # Placeholder for further application logic
    # TODO: Add logic to process the file or adjust logging level dynamically

if __name__ == "__main__":
    main()
