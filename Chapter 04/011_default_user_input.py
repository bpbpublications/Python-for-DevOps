# Script: 011_default_user_input.py

def main():
    """
    Main function to demonstrate user input with a default value.
    Asks the user for confirmation with an option to accept the default value.
    """
    # Set the default value
    default_value = "yes"

    # Prompt the user for input, defaulting to `default_value` if no input is provided
    user_input = input(f"Proceed with the operation? [yes/no] (default: {default_value}): ") or default_value

    # Process the input
    if user_input.lower() == "yes":
        print("Operation proceeding...")
        # TODO: Add logic for proceeding with the operation
    elif user_input.lower() == "no":
        print("Operation canceled.")
        # TODO: Add logic for handling cancellation
    else:
        print("Invalid input. Please respond with 'yes' or 'no'.")
        # TODO: Add error handling or retry logic

if __name__ == "__main__":
    main()
