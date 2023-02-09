import asyncio


async def nested():
    return 42


def normal():
    return 45


########################


async def main():
    nested()  # RuntimeWarning: coroutine 'nested' was never awaited
    print(await nested())  # will print "42".


asyncio.run(main())

#########################


async def main():
    print(normal())  # will print 45
    print(await normal())  # TypeError: object int can't be used in 'await' expression


asyncio.run(main())
