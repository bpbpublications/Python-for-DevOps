# Script: 009_argument_dependency_check.py

import argparse

def main():
    """
    Main function to demonstrate argument dependency validation.
    Ensures that a dependent argument is provided when a condition is met.
    """
    # Create the argument parser
    parser = argparse.ArgumentParser(description='Validate argument dependencies.')

    # Add arguments
    parser.add_argument('--some-condition', action='store_true', help='Enable some condition')
    parser.add_argument('--dependent-argument', help='Required when some-condition is enabled')

    # Parse the arguments
    args = parser.parse_args()

    # Validate argument dependencies
    if args.some_condition and not args.dependent_argument:
        parser.error("The '--dependent-argument' is required when '--some-condition' is used.")

    # Example processing
    if args.some_condition:
        print(f"Some condition is enabled. Dependent argument: {args.dependent_argument}")

if __name__ == "__main__":
    main()
