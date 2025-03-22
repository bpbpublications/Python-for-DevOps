# Script: 029_multiprocessing_with_pipe.py
# Purpose: Demonstrates how to use `multiprocessing.Pipe` for inter-process communication.

from multiprocessing import Process, Pipe

# Define the worker function
def worker(conn):
    """
    A worker function that sends data through a pipe connection.

    Args:
        conn (Connection): The child end of the pipe to send data through.
    """
    conn.send("Data from worker")  # Send data to the parent process
    conn.close()  # Close the connection after sending

# Main program
if __name__ == "__main__":
    # Create a pipe
    parent_conn, child_conn = Pipe()

    # Create a process that runs the worker function with the child connection
    process = Process(target=worker, args=(child_conn,))

    # Start the process
    process.start()

    # Receive and print data from the worker using the parent connection
    print("Received from worker:", parent_conn.recv())  # Output: Data from worker

    # Wait for the process to complete
    process.join()
