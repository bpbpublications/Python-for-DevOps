# Script: 003_timer_decorator.py

import time

# Decorator to measure and log the execution time of a function
def timer_decorator(func):
    """
    A decorator that measures the execution time of a function.
    """
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} executed in {end_time - start_time:.2f} seconds")
        return result
    return wrapper

@timer_decorator
def long_running_function():
    """
    Simulates a long-running operation with a sleep.
    """
    time.sleep(2)
    return "Completed"

# Example function call
if __name__ == "__main__":
    long_running_function()
