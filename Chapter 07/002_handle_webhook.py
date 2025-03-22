# Script: 002_handle_webhook.py

from flask import Flask, request

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def handle_webhook():
    """
    Handle incoming webhooks.
    """
    # Parse the JSON data from the request
    event_data = request.json

    # Log the received webhook data
    print("Webhook received:", event_data)

    # Perform actions based on the event type
    if event_data.get('event') == 'network_down':
        print("Handling Network down event.")
        # Add additional logic to handle 'network_down' events here

    # Return a success response
    return "Webhook processed", 200

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True, host='0.0.0.0', port=5000)
