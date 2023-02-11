import asyncio
import time


async def waiter(event):
    print("waiting for it ...", time.strftime("%X"))
    await event.wait()
    print("... got it!", time.strftime("%X"))


async def main():
    event = asyncio.Event()
    waiter_task = asyncio.create_task(waiter(event))

    print("main before sleep", time.strftime("%X"))
    await asyncio.sleep(1)
    print("main after sleep", time.strftime("%X"))
    event.set()

    await waiter_task


asyncio.run(main())
# main before sleep 15:06:00
# waiting for it ... 15:06:00
# main after sleep 15:06:01
# ... got it! 15:06:01


######################


async def read_file(event):
    print("read file ....", time.strftime("%X"))
    await asyncio.sleep(5)
    event.set()
    print("read file done", time.strftime("%X"))


async def write_network(event):
    print("waiting for reading file", time.strftime("%X"))
    await event.wait()
    print("... got it!", time.strftime("%X"))


async def main():
    event = asyncio.Event()
    await asyncio.gather(read_file(event), write_network(event))


asyncio.run(main())
# read file .... 15:16:11
# waiting for reading file 15:16:11
# read file done 15:16:16
# ... got it! 15:16:16


#######################


async def read_file(event):
    print("read file ....", time.strftime("%X"))
    await asyncio.sleep(5)
    event.set()
    print("read file done", time.strftime("%X"))


async def write_network(event):
    print("in nettwork waiting for reading file", time.strftime("%X"))
    await event.wait()
    print("network got it!", time.strftime("%X"))


async def write_socket(event):
    print("in socket waiting for reading file", time.strftime("%X"))
    await event.wait()
    print("socket got it!", time.strftime("%X"))


async def main():
    event = asyncio.Event()
    await asyncio.gather(
        read_file(event),
        write_network(event),
        write_socket(event),
    )


asyncio.run(main())
# read file .... 15:34:52
# in nettwork waiting for reading file 15:34:52
# in socket waiting for reading file 15:34:52
# read file done 15:34:57
# network got it! 15:34:57
# socket got it! 15:34:57


#######################

import functools


def set_event(event):
    event.set()


async def work(event):
    print("waiting for ...", time.strftime("%X"))
    await event.wait()
    print("... got it", time.strftime("%X"))


async def main():
    event = asyncio.Event()
    asyncio.get_event_loop().call_later(5, functools.partial(set_event, event))
    await asyncio.gather(work(event))


asyncio.run(main())
# waiting for ... 15:21:43
# ... got it 15:21:48
