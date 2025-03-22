# Script: 016_monitor_disk_usage.py

import psutil
import subprocess
import logging

def check_disk_usage(disk, threshold):
    """
    Checks the disk usage of the specified disk and performs cleanup if it exceeds the threshold.
    :param disk: Path to the disk (e.g., '/').
    :param threshold: Usage percentage that triggers cleanup.
    """
    try:
        du = psutil.disk_usage(disk)
        usage_percent = du.percent
        if usage_percent > threshold:
            logging.warning(f"Disk usage is high on {disk}: {usage_percent}%")
            perform_cleanup()
        else:
            logging.info(f"Disk usage is normal on {disk}: {usage_percent}%")
    except FileNotFoundError:
        logging.error(f"Disk path not found: {disk}")
    except Exception as e:
        logging.error(f"Error checking disk usage: {e}")

def perform_cleanup():
    """
    Performs cleanup actions to free disk space.
    Placeholder for actual cleanup actions.
    """
    try:
        logging.info("Performing disk cleanup...")
        # Example cleanup action (replace with actual cleanup commands)
        subprocess.run("echo 'Performing cleanup actions...'", shell=True, check=True)
    except subprocess.CalledProcessError as e:
        logging.error(f"Cleanup command failed: {e}")
    except Exception as e:
        logging.error(f"Error during cleanup: {e}")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    # Configuration
    disk_to_monitor = '/'  # Root disk
    usage_threshold = 80  # Percentage threshold for triggering cleanup

    check_disk_usage(disk_to_monitor, usage_threshold)
