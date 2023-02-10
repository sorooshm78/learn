import asyncio
import time


async def say_what(what):
    print(f"before sleep {what}", time.strftime("%X"))
    await asyncio.sleep(1)
    print(f"say {what}", time.strftime("%X"))


async def main():

    tasks = [say_what(f"task{i+1}") for i in range(10)]

    await asyncio.gather(*tasks)


asyncio.run(main())
# before sleep task1 14:43:04
# before sleep task2 14:43:04
# before sleep task3 14:43:04
# before sleep task4 14:43:04
# before sleep task5 14:43:04
# before sleep task6 14:43:04
# before sleep task7 14:43:04
# before sleep task8 14:43:04
# before sleep task9 14:43:04
# before sleep task10 14:43:04
# say task1 14:43:05
# say task2 14:43:05
# say task3 14:43:05
# say task:43:05
# say task8 14:43:05
# say task9 14:43:05
# say task10 14:43:05


###############################


async def say_what(smp, what):
    async with smp:
        print(f"before sleep {what}", time.strftime("%X"))
        await asyncio.sleep(1)
        print(f"say {what}", time.strftime("%X"))


async def main():
    smp = asyncio.Semaphore(2)
    tasks = [say_what(smp, f"task{i+1}") for i in range(10)]

    await asyncio.gather(*tasks)


asyncio.run(main())
# before sleep task1 14:45:32
# before sleep task2 14:45:32
# say task1 14:45:33
# say task2 14:45:33
# before sleep task3 14:45:33
# before sleep task4 14:45:33
# say task3 14:45:34
# say task4 14:45:34
# before sleep task5 14:45:34
# before sleep task6 14:45:34
# say task5 14:45:35
# say task6 14:45:35
# before sleep task7 14:45:35
# before sleep task8 14:45:35
# say task7 14:45:36
# say task8 14:45:36
# before sleep task9 14:45:36
# before sleep task10 14:45:36
# say task9 14:45:37
# say task10 14:45:37


###############################
