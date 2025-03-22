# Script: 014_interactive_prompt.py

from InquirerPy import prompt

def main():
    """
    Main function to demonstrate interactive CLI prompts using InquirerPy.
    Allows the user to select an option from a list.
    """
    # Define the questions for the prompt
    questions = [
        {
            "type": "list",
            "name": "choice",
            "message": "Select an option:",
            "choices": ["Option 1", "Option 2"]
        }
    ]

    # Prompt the user and capture the answer
    answer = prompt(questions)

    # Display the selected option
    print(f"You selected {answer['choice']}.")

if __name__ == "__main__":
    main()
