import asyncio
from asyncio.exceptions import TimeoutError


async def something():
    print("before sleep ...")
    await asyncio.sleep(3)
    print("after sleep ...")


async def main():
    try:
        async with asyncio.timeout(2):
            await something()
    except TimeoutError:
        print("except timeout error")


# asyncio.run(main())
# before sleep ...
# except timeout error

####################


async def something():
    print("before sleep ...")
    await asyncio.sleep(3)
    print("after sleep ...")


async def main():
    try:
        async with asyncio.timeout(2) as cm:
            print(cm.when())
            await something()
    except TimeoutError:
        print("except timeout error")


# asyncio.run(main())
# 3911.956273083
# before sleep ...
# except timeout error

#########################


async def something():
    print("before sleep ...")
    await asyncio.sleep(3)
    print("after sleep ...")


async def main():
    try:
        async with asyncio.timeout(delay=None) as cm:
            print(cm.when())
            await something()
    except TimeoutError:
        print("except timeout error")


# asyncio.run(main())
# None
# before sleep ...
# after sleep ...

#######################


async def something():
    print("before sleep ...")
    await asyncio.sleep(3)
    print("after sleep ...")


async def main():
    try:
        async with asyncio.timeout(delay=None) as cm:
            new_time = asyncio.get_running_loop().time() + 5  # 5 second
            cm.reschedule(new_time)
            await something()
    except TimeoutError:
        print("except timeout error")


asyncio.run(main())
# before sleep ...
# after sleep ...
