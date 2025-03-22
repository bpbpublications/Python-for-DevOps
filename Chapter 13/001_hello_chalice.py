# Script: 001_hello_chalice.py

from chalice import Chalice

# Initialize the Chalice app
app = Chalice(app_name='hello-chalice')

# Define the root endpoint for the Chalice app
@app.route('/')
def index():
    """
    Root endpoint returning a welcome message.
    """
    return {'hello': 'world'}
