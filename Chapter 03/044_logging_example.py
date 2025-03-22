# Script: 044_logging_example.py

# Importing the logging module for logging messages
import logging

# Setting up basic configuration for logging with level INFO and a custom format
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Logging an info message
logging.info("This is an info message")

# Handling an exception and logging the exception details
try:
    1 / 0  # Division by zero to raise an exception
except ZeroDivisionError:
    # Logging the exception with a traceback
    logging.exception("Exception occurred")
