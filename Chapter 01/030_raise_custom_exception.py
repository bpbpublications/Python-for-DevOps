# Prompt the user to enter their age
try:
    age = int(input("Enter your age: "))  # Might raise a ValueError if input is not an integer
    if age < 0:
        # Raise a ValueError if the entered age is negative
        raise ValueError("Age cannot be negative!")
    print(f"Your age is: {age}")
except ValueError as e:
    # Handle the ValueError and display an appropriate message
    print(f"Invalid input: {e}")
