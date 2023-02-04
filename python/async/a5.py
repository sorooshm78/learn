import asyncio
from asyncio.exceptions import TimeoutError


async def something():
    print("before sleep ...")
    await asyncio.sleep(3)
    print("after sleep ...")
    print("return number")
    return 5


async def main():
    task = asyncio.create_task(something())
    res = await asyncio.wait_for(asyncio.shield(task), 2)
    print("res", res)


asyncio.run(main())
# before sleep ...
# Traceback (most recent call last):
#   File "/usr/lib/python3.10/asyncio/tasks.py", line 456, in wait_for
#     return fut.result()
# asyncio.exceptions.CancelledError

##########################


async def something():
    print("before sleep ...")
    await asyncio.sleep(3)
    print("after sleep ...")
    print("return number")
    return 5


async def main():
    task = asyncio.create_task(something())
    try:
        res = await asyncio.wait_for(asyncio.shield(task), 2)
    except TimeoutError:
        print("except timeout error")
        res = await task
    print("res", res)


asyncio.run(main())
# before sleep ...
# except timeout error
# after sleep ...
# return number
# res 5
