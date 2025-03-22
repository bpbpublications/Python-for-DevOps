# Script: 010_log_message.py

import sys

def log_message(message):
    """
    Append a message to the log file.

    Args:
        message (str): The message to log.
    """
    try:
        with open("log.txt", "a") as file:
            file.write(message + "\n")
        print(f"Message logged: {message}")
    except Exception as e:
        print(f"Error writing to log file: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python log_message.py <message>")
        sys.exit(1)

    # Log the provided message
    log_message(sys.argv[1])
