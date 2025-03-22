# Script: 031_psutil_process_monitoring.py
# Purpose: Demonstrates how to use the `psutil` module to list and monitor processes.

import psutil

# Listing all processes
print("Listing all processes:")
for process in psutil.process_iter(['pid', 'name']):
    try:
        print(process.info)  # Print process ID and name
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        # Handle processes that might terminate or deny access during iteration
        pass

# Monitoring a specific process
pid = 1234  # Replace with the process ID you want to monitor
if psutil.pid_exists(pid):
    proc = psutil.Process(pid)
    print(f"\nMonitoring process with PID {pid}:")
    print(f"CPU Usage: {proc.cpu_percent(interval=1)}%")  # Get CPU usage over a 1-second interval
    print(f"Memory Usage: {proc.memory_info().rss / (1024 ** 2):.2f} MB")  # Convert memory to MB
else:
    print(f"\nProcess with PID {pid} does not exist.")
