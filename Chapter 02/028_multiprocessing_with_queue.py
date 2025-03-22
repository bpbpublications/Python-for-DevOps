# Script: 028_multiprocessing_with_queue.py
# Purpose: Demonstrates how to use `multiprocessing.Queue` for inter-process communication.

from multiprocessing import Process, Queue

# Define the worker function
def worker(q):
    """
    A worker function that puts data into the queue.

    Args:
        q (Queue): The multiprocessing queue to share data.
    """
    q.put("Data from worker")

# Main program
if __name__ == "__main__":
    # Create a multiprocessing queue
    queue = Queue()

    # Create a process that runs the worker function
    process = Process(target=worker, args=(queue,))

    # Start the process
    process.start()

    # Wait for the process to complete
    process.join()

    # Retrieve and print the data from the queue
    print("Received from worker:", queue.get())  # Output: Data from worker
