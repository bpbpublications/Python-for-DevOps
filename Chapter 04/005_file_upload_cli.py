# Script: 005_file_upload_cli.py

import argparse

def main():
    """
    Main function to handle a simple CLI for uploading a file.
    Ensures that '--upload' option is used with '--file' argument.
    """
    # Create the argument parser
    parser = argparse.ArgumentParser(description='Upload a file using CLI.')

    # Define arguments
    parser.add_argument('--upload', action='store_true', help='Enable upload functionality')
    parser.add_argument('--file', help='Specify the file to upload')

    # Parse the arguments
    args = parser.parse_args()

    # Validate arguments
    if args.upload and not args.file:
        parser.error("The '--upload' option requires the '--file' option.")

    # Process upload if valid arguments are provided
    if args.upload:
        print(f"Uploading file: {args.file}")
        # TODO: Add the logic to upload the file

if __name__ == "__main__":
    main()
