# Script: 019_async_click_tasks.py

import asyncio
import click

async def async_task():
    """
    Example of an asynchronous IO-bound operation.
    Simulates a delay and returns a completion message.
    """
    await asyncio.sleep(2)
    return "Task completed"

@click.command()
@click.option('--count', default=1, help='Number of tasks to run')
async def run_tasks(count):
    """
    CLI command to run a specified number of asynchronous tasks.
    """
    tasks = [asyncio.create_task(async_task()) for _ in range(count)]
    for task in tasks:
        result = await task
        click.echo(result)

if __name__ == '__main__':
    asyncio.run(run_tasks())
