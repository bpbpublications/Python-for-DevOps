# Script: 002_track_request_latency.py

from prometheus_client import start_http_server, Summary
import random
import time

# Create a metric to track request latency
REQUEST_LATENCY = Summary('request_latency_seconds', 'Request latency in seconds')

# Decorator to track request latency
def track_request_latency(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Record the start time
        result = func(*args, **kwargs)  # Execute the wrapped function
        end_time = time.time()  # Record the end time
        REQUEST_LATENCY.observe(end_time - start_time)  # Observe the latency
        return result
    return wrapper

# Example function to simulate a web request
@track_request_latency
def process_request():
    time.sleep(random.uniform(0.1, 0.5))  # Simulate processing time

if __name__ == '__main__':
    # Start HTTP server to expose metrics on port 8000
    start_http_server(8000)
    
    # Simulate web requests in an infinite loop
    while True:
        process_request()
