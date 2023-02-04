import asyncio
from asyncio.exceptions import CancelledError, TimeoutError


async def something():
    print("before sleep ...")
    await asyncio.sleep(3)
    print("after sleep ...")
    print("return number")
    return 5


async def main():
    try:
        async with asyncio.timeout(10):
            await something()
    except TimeoutError:
        print("The long operation timed out, but we've handled it.")

    print("This statement will run regardless.")


asyncio.run(main())
