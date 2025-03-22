# Script: 030_multiprocessing_with_lock.py
# Purpose: Demonstrates how to use `multiprocessing.Lock` to ensure exclusive access to a shared resource.

from multiprocessing import Process, Lock, current_process

# Define the task function that requires exclusive access
def task_with_lock(lock):
    """
    A task function that uses a lock to ensure exclusive access.

    Args:
        lock (Lock): A multiprocessing lock to synchronize access.
    """
    with lock:
        # Perform a task that requires exclusive access
        print(f"Lock acquired by {current_process().name}")
        # Simulate a critical section
        pass

if __name__ == "__main__":
    # Create a multiprocessing lock
    lock = Lock()

    # Create multiple processes that share the lock
    p1 = Process(target=task_with_lock, args=(lock,))
    p2 = Process(target=task_with_lock, args=(lock,))

    # Start the processes
    p1.start()
    p2.start()

    # Wait for both processes to complete
    p1.join()
    p2.join()
