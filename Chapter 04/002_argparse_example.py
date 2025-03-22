# Script: 002_argparse_example.py

import argparse

def main():
    """
    Main function to demonstrate argument parsing with argparse.
    Processes a filename, verbosity, and logging level.
    """
    # Initialize the argument parser
    parser = argparse.ArgumentParser(description='Process a file with customizable verbosity and logging level.')
    
    # Add arguments
    parser.add_argument('filename', help='The name of the file to process')
    parser.add_argument('-v', '--verbose', action='store_true', help='Increase output verbosity')
    parser.add_argument('-l', '--loglevel', default='WARNING', 
                        choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'], 
                        help='Set the logging level')

    # Parse the arguments
    args = parser.parse_args()

    # Handle verbose mode
    if args.verbose:
        print("Verbose mode activated")

    # Handle logging level
    if args.loglevel:
        print(f"Logging level set to {args.loglevel}")

    # Process the provided filename
    print(f"Processing file: {args.filename}")

    # Placeholder for further application logic
    # TODO: Add the logic to process the file

if __name__ == "__main__":
    main()
