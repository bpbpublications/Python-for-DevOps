# Script: 005_instrument_requests_with_opentelemetry.py

import requests
from opentelemetry import trace
from opentelemetry.instrumentation.requests import RequestsInstrumentor

# Instrument requests library to enable tracing
RequestsInstrumentor().instrument()

def make_request(url):
    """
    Makes a GET request to the specified URL with OpenTelemetry tracing.
    """
    # Start a new span for tracing the request
    with trace.get_tracer(__name__).start_as_current_span("make_request"):
        response = requests.get(url)  # Perform the GET request
        return response  # Return the response object
