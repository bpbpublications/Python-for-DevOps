# Script: 018_system_health_monitoring.py

import requests
import time

def monitor_system():
    """
    Monitors the system health by periodically checking the health endpoint.
    If an error is detected, it performs reactive actions.
    """
    while True:
        response = requests.get("http://localhost:8080/health")  # API call to check system health
        status = response.json().get("status")  # Extract the health status
        if status == "error":
            handle_error()  # Perform reactive actions if an error is detected
        time.sleep(60)  # Wait for 1 minute before checking again

def handle_error():
    """
    Handles errors by restarting the service and sending an alert notification.
    """
    restart_service()  # Restart the problematic service
    send_alert()  # Send an alert notification

def restart_service():
    """
    Sends an API request to restart the service.
    """
    requests.post("http://localhost:8080/restart")
    print("Service restarted.")

def send_alert():
    """
    Sends an alert notification via an API call.
    """
    requests.post("http://localhost:8080/send-alert")
    print("Alert notification sent.")

if __name__ == "__main__":
    monitor_system()  # Start monitoring the system
