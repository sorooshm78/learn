import asyncio
import time


async def say_after(delay, what):
    print(f"inside func {delay} {what}", time.strftime("%X"))
    await asyncio.sleep(delay)
    print(what)


#########################


# behaviar await
async def main():
    task1 = asyncio.create_task(say_after(2, "task1"))
    task2 = asyncio.create_task(say_after(1, "task2"))

    print("after create task")

    print("before await task1 in main")
    await task1
    print("after await task1 in main")

    print("before await task2 in main")
    await task2
    print("after await task2 in main")


# asyncio.run(main())
# after create task
# before await task1 in main
# inside func 1 task1
# inside func 2 task2
# task1
# after await task1 in main
# before await task2 in main
# task2
# after await task2 in main


########################


async def say_after(delay, what):
    print(f"inside func {delay} {what}", time.strftime("%X"))
    await asyncio.sleep(delay)
    print(what)


# behaviar await
async def main():
    task1 = asyncio.create_task(say_after(4, "task1"))
    task2 = asyncio.create_task(say_after(2, "task2"))

    print("after create task", time.strftime("%X"))

    print("before await task1 in main", time.strftime("%X"))
    await task1
    print("after await task1 in main", time.strftime("%X"))

    print("before await task2 in main", time.strftime("%X"))
    await task2
    print("after await task2 in main", time.strftime("%X"))


asyncio.run(main())

# result : task1 2sec, task2 4 sec  ******* import ******
# after create task 20:18:17
# before await task1 in main 20:18:17
# inside func 2 task1 20:18:17
# inside func 4 task2 20:18:17
# task1
# after await task1 in main 20:18:19
# before await task2 in main 20:18:19
# task2
# after await task2 in main 20:18:21


# result : task1 4sec, task2 2 sec  ******* import ******
# after create task 20:25:55
# before await task1 in main 20:25:55
# inside func 4 task1 20:25:55
# inside func 2 task2 20:25:55
# task2
# task1
# after await task1 in main 20:25:59
# before await task2 in main 20:25:59
# after await task2 in main 20:25:59

####################


async def say_after(delay, what):
    print(f"inside func {delay} {what}", time.strftime("%X"))
    await asyncio.sleep(delay)
    print(what)


async def main():
    async with asyncio.TaskGroup() as tg:
        print("before task1 in main", time.strftime("%X"))
        task1 = tg.create_task(say_after(1, "task1"))
        print("after task1 in main", time.strftime("%X"))
        print("before task2 in main", time.strftime("%X"))
        task2 = tg.create_task(say_after(2, "task2"))
        print("after task2 in main", time.strftime("%X"))

    print("Both tasks have completed now.")


asyncio.run(main())


######################
