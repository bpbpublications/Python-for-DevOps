# Script: 013_file_upload_progress.py

import time
from tqdm import tqdm

def main():
    """
    Main function to simulate a file upload process with a progress bar.
    Uses tqdm to display the progress bar in the terminal.
    """
    for i in tqdm(range(100), desc="Uploading file", unit="%", ncols=80):
        time.sleep(0.05)  # Simulating a task with a delay

if __name__ == "__main__":
    main()
