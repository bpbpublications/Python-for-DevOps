# Define a custom exception for negative age values
class NegativeAgeError(Exception):
    """Custom exception for negative age values."""
    def __init__(self, message="Age cannot be negative!"):
        super().__init__(message)

# Prompt the user to enter their age
try:
    age = int(input("Enter your age: "))  # Convert input to an integer
    if age < 0:
        # Raise the custom NegativeAgeError if age is negative
        raise NegativeAgeError(f"Invalid age: {age}. Age cannot be negative!")
    print(f"Your age is: {age}")
except ValueError:
    # Handle cases where the input is not a valid integer
    print("Invalid input! Please enter a valid number.")
except NegativeAgeError as e:
    # Handle cases where a negative age is entered
    print(f"Error: {e}")
