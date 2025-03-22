# Script: 018_asyncio_fetch_data.py

import asyncio

async def fetch_data():
    """
    Simulates fetching data from an external source.
    Uses asyncio to mimic an IO-bound operation.
    """
    print("Start fetching")
    await asyncio.sleep(2)  # Simulates a delay for an IO operation
    print("Done fetching")
    return {'data': 123}

async def main():
    """
    Main asynchronous function to manage tasks.
    Creates and awaits the fetch_data task.
    """
    task = asyncio.create_task(fetch_data())  # Create an asynchronous task
    # You can add more tasks or coroutines here if needed
    result = await task  # Await the result of the task
    print(result)

if __name__ == '__main__':
    asyncio.run(main())  # Run the main coroutine
