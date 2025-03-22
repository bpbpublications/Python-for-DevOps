# Script: 020_parse_and_analyze_logs.py

import re

# Sample log file path
log_file_path = "/var/log/syslog"  # Replace with your log file path

def parse_log(file_path):
    """
    Parses the specified log file line by line.
    :param file_path: Path to the log file.
    """
    try:
        with open(file_path, 'r') as file:
            for line in file:
                parse_log_entry(line)
    except FileNotFoundError:
        print(f"Log file not found: {file_path}")
    except PermissionError:
        print(f"Permission denied. Run this script with elevated privileges to access: {file_path}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def parse_log_entry(entry):
    """
    Analyzes a single log entry using a regex pattern.
    :param entry: A single line from the log file.
    """
    log_pattern = r'(\w{3} \d{2} \d{2}:\d{2}:\d{2}) (\w+) (.*)'
    match = re.search(log_pattern, entry)
    if match:
        date, source, message = match.groups()
        analyze_log_data(date, source, message)

def analyze_log_data(date, source, message):
    """
    Analyzes extracted log data and prints errors.
    :param date: Timestamp of the log entry.
    :param source: Source of the log entry.
    :param message: Message content of the log entry.
    """
    if "error" in message.lower():
        print(f"Error found: {message} from {source} at {date}")

if __name__ == "__main__":
    parse_log(log_file_path)
