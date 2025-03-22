# File: receive_input.py
# This script reads input from stdin and prints it.
import sys

def main():
    # Read input from stdin
    for line in sys.stdin:
      # Process the line
      print(f'Received: {line.strip()}')


if __name__ == "__main__":
    main()