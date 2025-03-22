# Script: 026_multiprocessing_example.py
# Purpose: Demonstrates how to use the `multiprocessing` module to create and manage a separate process.

from multiprocessing import Process

# Define the function to be executed in a separate process
def task_function(name):
    """
    A simple task function that prints a greeting message.

    Args:
        name (str): The name to include in the greeting.
    """
    print(f"Hello, {name}")

# Create a process to run the task_function with the argument 'World'
process = Process(target=task_function, args=('World',))

# Start the process
process.start()

# Wait for the process to complete
process.join()
