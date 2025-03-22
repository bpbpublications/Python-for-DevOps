# Script: 009_flask_incident_reporting.py

from flask import Flask, request, jsonify

app = Flask(__name__)

# List to store reported incidents
incidents = []

@app.route('/report-incident', methods=['POST'])
def report_incident():
    """
    Endpoint to report an incident. Expects a JSON payload.
    """
    data = request.json  # Parse the incoming JSON data
    incidents.append(data)  # Add the incident to the list
    return jsonify({"message": "Incident reported successfully"})  # Respond with a success message

@app.route('/incidents', methods=['GET'])
def get_incidents():
    """
    Endpoint to retrieve all reported incidents.
    """
    return jsonify(incidents)  # Return the list of incidents as JSON

if __name__ == '__main__':
    app.run(debug=True)  # Run the Flask application in debug mode
