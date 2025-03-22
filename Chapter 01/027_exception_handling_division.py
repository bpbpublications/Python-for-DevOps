# Use a try-except block to handle potential exceptions
try:
    # Prompt the user for input and attempt to divide 10 by the entered number
    result = 10 / int(input("Enter a number: "))
    # Print the result if successful
    print(f"10 divided by your number is {result}")
except ValueError:
    # Handle the case where the input is not a valid integer
    print("Oops! That doesn't look like a number.")
except ZeroDivisionError:
    # Handle the case where the user attempts to divide by zero
    print("Well, dividing by zero isn't really possible.")
