# Script: 005_retry_with_backoff.py

import time

def retry_with_backoff(retries=5, delay=1):
    """
    A decorator that retries a function with exponential backoff 
    in case of a ConnectionError.
    
    Args:
        retries (int): Number of retries before giving up.
        delay (int): Initial delay in seconds between retries.
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            current_delay = delay
            for attempt in range(1, retries + 1):
                try:
                    return func(*args, **kwargs)
                except ConnectionError as e:
                    if attempt == retries:
                        raise  # Re-raise exception if all retries fail
                    print(f"Attempt {attempt} failed: {e}. Retrying in {current_delay} seconds...")
                    time.sleep(current_delay)
                    current_delay *= 2  # Exponential backoff
        return wrapper
    return decorator

@retry_with_backoff(retries=3, delay=2)
def make_request():
    """
    Simulates a network request that may raise a ConnectionError.
    Replace with actual implementation of a network request.
    """
    print("Attempting to make a request...")
    raise ConnectionError("Simulated connection error.")

# Example usage
if __name__ == "__main__":
    try:
        make_request()
    except ConnectionError as e:
        print(f"All retries failed. Error: {e}")
