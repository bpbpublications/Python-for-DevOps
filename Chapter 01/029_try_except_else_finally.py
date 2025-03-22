# Use a try-except-else-finally block to handle exceptions and cleanup
try:
    # Attempt to execute risky code
    value = int(input("Enter an integer: "))  # Might raise a ValueError
    result = 10 / value  # Might raise a ZeroDivisionError
    print(f"Result: {result}")
except ValueError:
    # Handle cases where input is not a valid integer
    print("Oops! That's not a valid integer.")
except ZeroDivisionError:
    # Handle cases where division by zero is attempted
    print("Division by zero is not allowed!")
else:
    # Execute this block if no exceptions were raised
    print("Everything went smoothly!")
finally:
    # Execute this block no matter what happens
    print("Execution completed. Cleaning up if necessary.")
