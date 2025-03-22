# Script: 008_custom_action_argparse.py

import argparse

class CustomAction(argparse.Action):
    """
    Custom argparse action for processing the '--custom' argument.
    Allows for tailored behavior when the argument is encountered.
    """
    def __call__(self, parser, namespace, values, option_string=None):
        # Custom processing logic
        print(f"Custom action triggered with value: {values}")
        setattr(namespace, self.dest, values)

def main():
    """
    Main function to demonstrate the use of a custom argparse action.
    """
    # Create the argument parser
    parser = argparse.ArgumentParser(description='Example of using a custom argparse action.')

    # Add argument using the custom action
    parser.add_argument('--custom', action=CustomAction, help='Trigger custom action with this argument')

    # Parse the arguments
    args = parser.parse_args()

    # Example use of the parsed argument
    if args.custom:
        print(f"Processed custom argument: {args.custom}")

if __name__ == "__main__":
    main()
