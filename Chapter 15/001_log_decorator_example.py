# Script: 001_log_decorator_example.py

import logging

# Setting up a basic logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Decorator to log function execution details
def log_decorator(func):
    """
    A decorator that logs the execution details of a function.
    """
    def wrapper(*args, **kwargs):
        logger.info(f"Executing {func.__name__} with arguments {args} and keyword arguments {kwargs}")
        result = func(*args, **kwargs)
        logger.info(f"{func.__name__} returned {result}")
        return result
    return wrapper

@log_decorator
def add(a, b):
    """
    Adds two numbers and returns the result.
    """
    return a + b

# Example function call
add(5, 3)
