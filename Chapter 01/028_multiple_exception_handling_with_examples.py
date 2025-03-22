# Use a try-except block to handle multiple potential exceptions
try:
    # Code that might raise exceptions
    value = int(input("Enter an integer: "))  # Might raise a ValueError
    result = 10 / value  # Might raise a ZeroDivisionError
    print("Result:", result)
    some_list = [1, 2, 3]
    print(some_list[value])  # Might raise an IndexError if `value` is out of range
except (ValueError, TypeError):
    # Handle cases where a ValueError or TypeError is raised
    print("There seems to be a value or type issue.")
except ZeroDivisionError:
    # Handle division by zero
    print("You cannot divide by zero!")
except IndexError:
    # Handle index errors when accessing a list
    print("Your input caused an index error. Please try with a valid index.")
except Exception as e:
    # Handle any other unexpected exceptions and print the error message
    print(f"An unexpected error occurred: {e}")
