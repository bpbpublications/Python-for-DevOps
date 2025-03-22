# Script: 021_analyze_log_data_with_pandas.py

import pandas as pd
import re

# Sample log data (replace with actual log file path or contents)
log_data = """
INFO 2021-01-01 Server started
ERROR 2021-01-02 Connection failed
INFO 2021-01-03 User logged in
"""

def parse_logs(log_contents):
    """
    Parses log entries into a structured format.
    :param log_contents: Multiline string containing log entries.
    :return: List of dictionaries with log details.
    """
    log_entries = []
    log_pattern = r'(\w+) (\d{4}-\d{2}-\d{2}) (.*)'
    for line in log_contents.strip().split('\n'):
        match = re.search(log_pattern, line)
        if match:
            level, date, message = match.groups()
            log_entries.append({'level': level, 'date': date, 'message': message})
    return log_entries

if __name__ == "__main__":
    # Parse log data
    log_entries = parse_logs(log_data)
    
    # Convert log entries to a DataFrame for analysis
    df = pd.DataFrame(log_entries)
    
    # Analyzing log data
    print("Log Level Counts:")
    print(df['level'].value_counts())
    
    print("\nLog Entries on 2021-01-02:")
    print(df[df['date'] == '2021-01-02'])
