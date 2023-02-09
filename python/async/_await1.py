import asyncio
import time


async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)


# SyntaxError: 'await' outside function
# await asyncio.run(say_after(1, "hello"))
# await asyncio.run(say_after(2, "world"))


async def main():
    print(f"started at {time.strftime('%X')}")
    await say_after(1, "hello")
    await say_after(2, "world")
    print(f"finished at {time.strftime('%X')}")


asyncio.run(main())  # 3 Second


async def main():
    task1 = asyncio.create_task(say_after(1, "hello"))
    task2 = asyncio.create_task(say_after(2, "world"))

    print(f"started at {time.strftime('%X')}")
    await task1
    await task2
    print(f"finished at {time.strftime('%X')}")


asyncio.run(main())  # 2 Second


# test -> what order finished
async def main():
    task1 = asyncio.create_task(say_after(2, "1 order"))
    task2 = asyncio.create_task(say_after(3, "2 order"))
    task3 = asyncio.create_task(say_after(3, "3 order"))
    task4 = asyncio.create_task(say_after(2, "4 order"))

    print(f"started at {time.strftime('%X')}")
    await task1
    await task2
    await task3
    await task4
    print(f"finished at {time.strftime('%X')}")


asyncio.run(main())

# started at 15:05:20
# 1 order
# 4 order
# 2 order
# 3 order
# finished at 15:05:23


# test -> what order finished when not io bound in once function
# 5 second when run sync
async def not_io_bound():
    a = 0
    for i in range(100000000):
        a += i
    print("finish not io bound")


async def main():
    task1 = asyncio.create_task(say_after(2, "io bound"))
    task2 = asyncio.create_task(not_io_bound())

    print(f"started at {time.strftime('%X')}")
    await task1
    await task2
    print(f"finished at {time.strftime('%X')}")


asyncio.run(main())
# started at 15:13:20
# finish not io bound
# io bound
# finished at 15:13:25


async def main():
    task1 = asyncio.create_task(say_after(2, "io bound"))
    task2 = asyncio.create_task(not_io_bound())
    task3 = asyncio.create_task(not_io_bound())

    print(f"started at {time.strftime('%X')}")
    await task1
    await task2
    await task3
    print(f"finished at {time.strftime('%X')}")


asyncio.run(main())
# started at 18:54:40
# finish not io bound
# finish not io bound
# io bound
# finished at 18:54:51
