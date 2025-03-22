# Script: 006_process_multiple_files.py

import argparse

def main():
    """
    Main function to process a list of files passed as command-line arguments.
    Handles multiple files provided as positional arguments.
    """
    # Create the argument parser
    parser = argparse.ArgumentParser(description='Process a list of files.')

    # Define positional argument for multiple filenames
    parser.add_argument('filenames', nargs='*', help='List of files to process')

    # Parse the arguments
    args = parser.parse_args()

    # Process the files
    if args.filenames:
        for filename in args.filenames:
            print(f"Processing file: {filename}")
            # TODO: Add logic to handle file processing
    else:
        print("No files provided. Please specify at least one file.")

if __name__ == "__main__":
    main()
