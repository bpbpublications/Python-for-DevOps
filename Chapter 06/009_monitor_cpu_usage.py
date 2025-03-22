# Script: 009_monitor_cpu_usage.py

import psutil
import time

def check_cpu_usage(threshold):
    """
    Check the system's CPU usage and take action if it exceeds the threshold.
    :param threshold: CPU usage percentage that triggers an action.
    """
    cpu_usage = psutil.cpu_percent(interval=1)
    print(f"Current CPU usage: {cpu_usage:.1f}%")
    
    if cpu_usage > threshold:
        print("CPU usage is above the threshold!")
        adjust_web_application(cpu_usage)

def adjust_web_application(cpu_usage):
    """
    Adjust the web application settings based on CPU usage.
    :param cpu_usage: Current CPU usage percentage.
    """
    print(f"Adjusting web application settings based on CPU usage: {cpu_usage:.1f}%")
    # Implement your logic here
    # Example: Adjusting number of workers, sending alerts, scaling services, etc.
    # For now, this is a placeholder.
    pass

if __name__ == "__main__":
    # Configuration
    cpu_usage_threshold = 75  # CPU usage percentage threshold

    # Monitoring loop
    try:
        while True:
            check_cpu_usage(cpu_usage_threshold)
            time.sleep(5)  # Check every 5 seconds
    except KeyboardInterrupt:
        print("CPU monitoring stopped.")
