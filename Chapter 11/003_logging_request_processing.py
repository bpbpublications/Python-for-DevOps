# Script: 003_logging_request_processing.py

import logging
import sys

# Configure root logger
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    stream=sys.stdout
)

# Create logger for a specific module or service
logger = logging.getLogger(__name__)

def process_request(request):
    """
    Processes a request and logs success or failure.
    """
    try:
        # Processing logic
        result = process(request)  # Call the process function
        logger.info(f"Request processed successfully: {request}")  # Log success
        return result
    except Exception as e:
        # Log error and raise exception
        logger.error(f"Error processing request: {request}, Error: {e}")
        raise

def process(request):
    """
    Placeholder for processing logic.
    Replace this function with the actual logic as needed.
    """
    return "Processed"  # Simulated processing result

if __name__ == "__main__":
    # Simulating requests
    requests = ["request1", "request2", "request3"]  # List of sample requests
    for req in requests:
        process_request(req)  # Process each request
