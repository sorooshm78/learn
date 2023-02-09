import asyncio
import time


async def factorial(name, number):
    f = 1
    for i in range(2, number + 1):
        print(f"Task {name}: Compute factorial({number}), currently i={i}...")
        await asyncio.sleep(1)
        f *= i
    print(f"Task {name}: factorial({number}) = {f}")
    return f


async def main():
    # Schedule three calls *concurrently*:
    L = await asyncio.gather(
        factorial("C", 4),
        factorial("B", 3),
        factorial("A", 2),
    )
    print(L)


# asyncio.run(main())
# Task C: Compute factorial(4), currently i=2...
# Task B: Compute factorial(3), currently i=2...
# Task A: Compute factorial(2), currently i=2...
# Task C: Compute factorial(4), currently i=3...
# Task B: Compute factorial(3), currently i=3...
# Task A: factorial(2) = 2
# Task C: Compute factorial(4), currently i=4...
# Task B: factorial(3) = 6
# Task C: factorial(4) = 24
# [24, 6, 2]


##########################


async def say_after(delay, what):
    print(f"inside func {delay} {what}", time.strftime("%X"))
    await asyncio.sleep(delay)
    print(what)


async def main():
    print("before gatherit", time.strftime("%X"))
    L = await asyncio.gather(
        say_after(1, "task1"),
        say_after(2, "task2"),
        say_after(3, "task3"),
    )
    print("after gatherit", time.strftime("%X"))
    print(L)


asyncio.run(main())
# before gatherit 21:33:28
# inside func 1 task1 21:33:28
# inside func 2 task2 21:33:28
# inside func 3 task3 21:33:28
# task1
# task2
# task3
# after gatherit 21:33:31
# [None, None, None]
