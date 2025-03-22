# Script: 027_multiprocessing_with_pool.py
# Purpose: Demonstrates how to use the `multiprocessing.Pool` to parallelize a task.

from multiprocessing import Pool

# Define the function to calculate the square of a number
def square(number):
    """
    Calculates the square of a given number.

    Args:
        number (int): The number to be squared.

    Returns:
        int: The square of the input number.
    """
    return number * number

# Use a Pool to parallelize the task
if __name__ == "__main__":
    # Create a Pool with 5 worker processes
    with Pool(5) as p:
        # Map the `square` function to a list of numbers
        results = p.map(square, [1, 2, 3, 4, 5])
    
    # Print the results
    print("Squares of the numbers:", results)  # Output: [1, 4, 9, 16, 25]
