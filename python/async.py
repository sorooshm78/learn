# Parallelism consists of performing multiple operations at the same time.
# Multiprocessing is a means to effect parallelism, and it entails spreading tasks over a computer’s central processing units (CPUs, or cores).
# Multiprocessing is well-suited for CPU-bound tasks: tightly bound for loops and mathematical computations usually fall into this category.

# Concurrency is a slightly broader term than parallelism.
# It suggests that multiple tasks have the ability to run in an overlapping manner.
# (There’s a saying that concurrency does not imply parallelism.)

# Threading is a concurrent execution model whereby multiple threads take turns executing tasks.
# One process can contain multiple threads. Python has a complicated relationship with threading thanks to its GIL

# To recap the above,
# concurrency encompasses both multiprocessing (ideal for CPU-bound tasks)
# and threading (suited for IO-bound tasks).
# Multiprocessing is a form of parallelism, with parallelism being a specific type (subset) of concurrency.
# The Python standard library has offered longstanding support for both of these through its multiprocessing, threading, and concurrent.futures packages.

# Asynchronous routines are able to “pause” while waiting on their ultimate result and let other routines run in the meantime.


# Chess master Judit Polgár hosts a chess exhibition in which she plays multiple amateur players. She has two ways of conducting the exhibition: synchronously and asynchronously.
# Assumptions:

#     24 opponents
#     Judit makes each chess move in 5 seconds
#     Opponents each take 55 seconds to make a move
#     Games average 30 pair-moves (60 moves total)

# Synchronous version: Judit plays one game at a time, never two at the same time, until the game is complete. Each game takes (55 + 5) * 30 == 1800 seconds, or 30 minutes. The entire exhibition takes 24 * 30 == 720 minutes, or 12 hours.
# Asynchronous version: Judit moves from table to table, making one move at each table. She leaves the table and lets the opponent make their next move during the wait time. One move on all 24 games takes Judit 24 * 5 == 120 seconds, or 2 minutes. The entire exhibition is now cut down to 120 * 30 == 3600 seconds, or just 1 hour. (Source)

# -----------------------------------------

import asyncio
import time


async def count():
    print("One")
    await asyncio.sleep(1)
    print("Two")


async def main():
    await asyncio.gather(count(), count(), count())


if __name__ == "__main__":
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(f"{end-start} second")

# One
# One
# One
# Two
# Two
# Two
# 1.0022783279418945 second

# -----------------------------------------

import asyncio
from datetime import datetime


async def count(time_sleep):
    print(f"before {time_sleep} at {datetime.now()}")
    await asyncio.sleep(time_sleep)
    print(f"after {time_sleep} at {datetime.now()}")


async def main():
    await asyncio.gather(count(1), count(2), count(3))


if __name__ == "__main__":
    asyncio.run(main())

# before 1 at 2023-05-06 15:51:43.893020
# before 2 at 2023-05-06 15:51:43.893083
# before 3 at 2023-05-06 15:51:43.893115
# after 1 at 2023-05-06 15:51:44.894321
# after 2 at 2023-05-06 15:51:45.894584
# after 3 at 2023-05-06 15:51:46.894797

# -----------------------------------------

# The keyword await passes function control back to the event loop.
# (It suspends the execution of the surrounding coroutine.)
# If Python encounters an await f() expression in the scope of g(),
# this is how await tells the event loop, “Suspend execution of g()
# until whatever I’m waiting on—the result of f()—is returned. In the meantime, go let something else run.”

async def g():
    # Pause here and come back to g() when f() is ready
    r = await f()
    return r

# Finally, when you use await f(), it’s required that f() be an object that is awaitable.
# Well, that’s not very helpful, is it? For now, just know that an awaitable
# object is either (1) another coroutine or (2) an object defining an .__await__() dunder method that returns an iterator.
# If you’re writing a program, for the large majority of purposes, you should only need to worry about case #1.

# An awaitable object generally implements an __await__() method.
# Coroutine objects returned from async def functions are awaitable.

# -----------------------------------------
