# Script: 015_argparse_autocomplete.py

import argcomplete, argparse

def main():
    """
    Main function to demonstrate argparse with autocomplete functionality.
    Allows the user to select an option from predefined choices.
    """
    # Create the argument parser
    parser = argparse.ArgumentParser(description="CLI tool with autocomplete support.")

    # Add argument with predefined choices
    parser.add_argument("option", choices=["setup", "deploy", "teardown"], help="Select an operation to perform")

    # Enable autocomplete
    argcomplete.autocomplete(parser)

    # Parse the arguments
    args = parser.parse_args()

    # Display the selected option
    print(f"Selected option: {args.option}")

if __name__ == "__main__":
    main()
