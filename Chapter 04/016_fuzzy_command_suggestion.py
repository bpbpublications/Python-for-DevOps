# Script: 016_fuzzy_command_suggestion.py

from fuzzywuzzy import process

def main():
    """
    Main function to demonstrate fuzzy matching for user input.
    Suggests the closest valid command if the user's input is misspelled.
    """
    # List of valid commands
    valid_commands = ["install", "uninstall", "update"]

    # Simulated user input (misspelled command)
    user_input = "instal"  # Example misspelled input

    # Find the closest match using fuzzy matching
    suggestion = process.extractOne(user_input, valid_commands)

    # Suggest the closest command if the match exceeds the threshold
    if suggestion and suggestion[1] > 85:  # 85% similarity threshold
        print(f"Did you mean: {suggestion[0]}?")
    else:
        print("No close match found for your input.")

if __name__ == "__main__":
    main()
