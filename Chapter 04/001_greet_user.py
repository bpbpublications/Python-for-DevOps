# Script: 001_greet_user.py

import sys

def main():
    """
    Main function to greet the user.
    If a name is passed as a command-line argument, it greets the user by name.
    Otherwise, it defaults to "Hello, World!".
    """
    # Check if there are any command-line arguments
    if len(sys.argv) > 1:
        name = sys.argv[1]  # Get the first argument as the name
        print(f"Hello, {name}!")
    else:
        print("Hello, World!")  # Default greeting if no arguments are provided

if __name__ == "__main__":
    main()
