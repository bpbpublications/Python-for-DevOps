# Script: 017_proactive_system_monitoring.py

import requests
import time

def check_system_status():
    """
    Makes an API call to monitor the system status.
    """
    response = requests.get("http://localhost:8080/system-status")  # API call to get system status
    status = response.json().get("status")  # Extract the status from the response
    return status

def scale_up_instances():
    """
    Scales up instances if the system status is degraded.
    """
    if check_system_status() == "degraded":  # Check if the system status is degraded
        requests.post("http://localhost:8080/scale-up")  # API call to scale up instances
        print("Scaled up instances due to degraded status.")  # Log the action

def run_proactive_checks():
    """
    Runs proactive checks every 5 minutes to monitor and scale up instances as needed.
    """
    while True:
        scale_up_instances()  # Check and scale up instances if needed
        time.sleep(300)  # Wait for 5 minutes before the next check

if __name__ == "__main__":
    run_proactive_checks()  # Start proactive monitoring
