"""
PYTHON CONCURRENCY & ASYNCHRONOUS PROGRAMMING NOTES
This file covers:
1. Asyncio Basics
2. Sync vs Async API calls
3. Multi-threading (I/O Bound)
4. Multi-processing (CPU Bound)
"""

import asyncio
import requests
import aiohttp
import threading
import time
from multiprocessing import Process

# =================================================================
# 1. ASYNCIO BASICS (Single-threaded Concurrency)
# =================================================================



async def task(name, delay):
    print(f"{name}: started")
    await asyncio.sleep(delay)   # yields control to event loop
    print(f"{name}: resumed after {delay}s")
    await asyncio.sleep(1)
    print(f"{name}: finished")

async def main():
    print("Main: start")

    t1 = asyncio.create_task(task("Task-1", 2))
    t2 = asyncio.create_task(task("Task-2", 1))

    print("Main: tasks created")

    await t1
    await t2

    print(f"Tasks at end of main: {asyncio.all_tasks()}")
    print("Main: end")

# Run the asyncio example
asyncio.run(main())

# =================================================================
# 2. SYNC VS ASYNC API CALLS
# =================================================================
def apisycncall():
    print("--- Starting Sync Call ---")
    try:
        data = requests.get("https://api.github.com/users/octocat")
        print("Sync data:", data.json().get("name"))
    except Exception as e:
        print(f"Sync error: {e}")
    finally:
        print("Sync final\n")

async def apiasynccall():
    print("--- Starting Async Call ---")
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get("https://api.github.com/users/octocat") as res:
                # Await the json coroutine
                data = await res.json()
                print("Async data:", data.get("name"))
                return data
    except Exception as e:
        print(f"Async error: {e}")
    finally:
        print("Async final")


apisycncall()
asyncio.run(apiasynccall())

# =================================================================
# 3. MULTI-THREADING (I/O Bound Tasks)
# =================================================================
# Threads are used for I/O bound tasks to run operations in parallel.

def task(name):
    print(f"Start {name}")
    print("Running in:", threading.current_thread().name)
    time.sleep(2)
    print(f"End {name}")

t1 = threading.Thread(target=task, args=("Thread-1",))
t2 = threading.Thread(target=task, args=("Thread-2",))

t1.name = "first thread"
t2.name = "second thread"

t1.start()
t2.start()

t1.join()
t2.join()
# =================================================================
# 4. MULTI-PROCESSING (CPU Bound Tasks)
# =================================================================
# Processes are used for CPU bound tasks to bypass the GIL (Global Interpreter Lock).

def task(name):
    print(f"{name} started")

    total = 0
    for i in range(10**8):   # increase workload
        total += i * i

    print(f"{name} finished")

if __name__ == "__main__":

    p1 = Process(target=task, args=("Process-1",))
    p2 = Process(target=task, args=("Process-2",))

    p1.start()
    p2.start()

    p1.join()
    p2.join()





