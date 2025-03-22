# Script: 027_calculate_statistics_with_logging.py

import logging

def calculate_statistics(data):
    """
    Calculates the average of a list of numbers and logs the process.
    :param data: List of numerical data.
    :return: The calculated average, or None if the input is invalid.
    """
    if not data:
        logging.error("No data provided for statistics calculation.")
        return None

    try:
        # Assume data is a list of numbers
        average = sum(data) / len(data)
        logging.info(f"Calculated average: {average}")
        return average
    except TypeError as e:
        logging.error(f"Data contains non-numeric elements: {e}")
        return None

if __name__ == "__main__":
    # Configure logging
    logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")
    
    # Example usage
    sample_data = [1, 2, 3, 4, 5]
    result = calculate_statistics(sample_data)
    if result is not None:
        print(f"The average is: {result}")
    else:
        print("Failed to calculate statistics.")
