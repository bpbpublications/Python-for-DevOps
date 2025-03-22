# Script: 026_divide_with_logging.py

import logging

def divide_numbers(a, b):
    """
    Divides two numbers and handles exceptions gracefully.
    Logs errors if division by zero or other exceptions occur.
    :param a: Numerator
    :param b: Denominator
    :return: Result of division, or None if an error occurs.
    """
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        logging.error("Attempted to divide by zero.")
    except Exception as e:
        logging.exception(f"An exception occurred: {e}")
    return None

if __name__ == "__main__":
    # Configure logging
    logging.basicConfig(level=logging.ERROR, format="%(asctime)s - %(levelname)s - %(message)s")
    
    # Example usage
    print(divide_numbers(10, 0))  # This will log an error
    print(divide_numbers(10, 2))  # This will return the result
