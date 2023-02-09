import asyncio
import time


num = 0

async def add():
    global num

    _num = num 
    _num += 1
    await asyncio.sleep(1)
    num = _num


async def main():
    tasks = [asyncio.create_task(add()) for _ in range(10)]
    await asyncio.gather(*tasks)
    print(f"number {num}")

asyncio.run(main())
# number = 1


##############################

num = 0

async def add(lock):
    global num

    async with lock:
        _num = num 
        _num += 1
        await asyncio.sleep(0.5)
        num = _num


async def main():
    lock = asyncio.Lock()
    tasks = [asyncio.create_task(add(lock)) for _ in range(10)]
    await asyncio.gather(*tasks)
    print(f"number {num}")

asyncio.run(main())
# number 10

###############################
num = 0

async def add(lock):
    global num

    async with lock:
        _num = num 
        _num += 1
        await asyncio.sleep(1)
        num = _num


async def main():
    lock = asyncio.Lock()
    tasks = [asyncio.create_task(add(lock)) for _ in range(10)]
    print("start", time.strftime("%X"))
    await asyncio.gather(*tasks)
    print("end", time.strftime("%X"))
    print(f"number {num}")

asyncio.run(main())
# start 20:27:06
# end 20:27:16
# number 10

