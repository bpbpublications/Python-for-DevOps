# Script: 015_monitor_high_cpu_usage.py

import psutil
import time

def check_cpu_usage(threshold=75):
    """
    Monitors the system's CPU usage and prints a warning if it exceeds the threshold.
    :param threshold: CPU usage percentage that triggers an alert.
    """
    try:
        cpu_usage = psutil.cpu_percent(interval=1)
        if cpu_usage > threshold:
            print(f"Warning: CPU usage is high at {cpu_usage}%")
    except Exception as e:
        print(f"Error monitoring CPU usage: {e}")

if __name__ == "__main__":
    # Configuration
    cpu_threshold = 75  # CPU usage percentage threshold

    try:
        while True:
            check_cpu_usage(cpu_threshold)
            time.sleep(5)  # Check every 5 seconds
    except KeyboardInterrupt:
        print("CPU monitoring stopped by user.")
