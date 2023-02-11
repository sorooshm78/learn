import asyncio

# task coroutine
async def task(condition, work_list):
    # block for a moment
    await asyncio.sleep(1)
    # add data to the work list
    work_list.append(33)
    # notify a waiting coroutine that the work is done
    print("Task sending notification...")
    async with condition:
        condition.notify()


# main coroutine
async def main():
    # create a condition
    condition = asyncio.Condition()
    # prepare the work list
    work_list = list()
    # wait to be notified that the data is ready
    print("Main waiting for data...")
    async with condition:
        # create and start the a task
        _ = asyncio.create_task(task(condition, work_list))
        # wait to be notified
        await condition.wait()
    # we know the data is ready
    print(f"Got data: {work_list}")


# run the asyncio program
asyncio.run(main())
# Main waiting for data...
# Task sending notification...
# Got data: [33]

###################


async def task(condition, work_list):
    await asyncio.sleep(1)
    work_list.append(33)
    print("Task sending notification...")
    async with condition:
        condition.notify()


async def main():
    condition = asyncio.Condition()
    work_list = list()

    print("Main waiting for data...")
    async with condition:
        _ = asyncio.create_task(task(condition, work_list))
        _ = asyncio.create_task(task(condition, work_list))
        await condition.wait()

    print(f"Got data: {work_list}")


asyncio.run(main())
# Main waiting for data...
# Task sending notification...
# Task sending notification...
# Got data: [33, 33]


###################


async def task(condition, work_list):
    print("start task")
    async with condition:
        print("before add number...")
        work_list.append(33)
        print("wait for notify")
        await condition.wait()


async def main():
    condition = asyncio.Condition()
    work_list = list()
    print("create tasks")
    _ = asyncio.create_task(task(condition, work_list))
    _ = asyncio.create_task(task(condition, work_list))

    async with condition:
        print("Main before sleep")
        await asyncio.sleep(5)
        print("notify")
        condition.notify_all()

    print(f"Got data: {work_list}")


asyncio.run(main())
# create tasks
# Main before sleep
# start task
# start task
# notify
# Got data: []
# before add number...
# wait for notify


###################

from random import random


async def task(condition, number):
    # report a message
    print(f"Task {number} waiting...")
    # acquire the condition
    async with condition:
        # wait to be notified
        await condition.wait()
    # generate a random number between 0 and 1
    value = random()
    # block for a moment
    await asyncio.sleep(value)
    # report a result
    print(f"Task {number} got {value}")


# main coroutine
async def main():
    # create a condition
    condition = asyncio.Condition()
    # create and start many tasks
    tasks = [asyncio.create_task(task(condition, i)) for i in range(5)]
    # allow the tasks to run
    await asyncio.sleep(1)
    # acquire the condition
    async with condition:
        # notify all waiting tasks
        condition.notify_all()
    # wait for all tasks to complete
    _ = await asyncio.wait(tasks)


# run the asyncio program
asyncio.run(main())
# Task 0 waiting...
# Task 1 waiting...
# Task 2 waiting...
# Task 3 waiting...
# Task 4 waiting...
# Task 1 got 0.2711177993331084
# Task 2 got 0.5984537132514656
# Task 3 got 0.7247601769561107
# Task 4 got 0.8822708022080372
# Task 0 got 0.9902754430132965

#############################

from random import random


# task coroutine
async def task(condition, work_list):
    # acquire the condition
    async with condition:
        # generate a random value between 0 and 1
        value = random()
        # block for a moment
        await asyncio.sleep(value)
        # add work to the list
        work_list.append(value)
        print(f"Task added {value}")
        # notify the waiting coroutine
        condition.notify()


# main coroutine
async def main():
    # create a condition
    condition = asyncio.Condition()
    # define work list
    work_list = list()
    # create and start many tasks
    _ = [asyncio.create_task(task(condition, work_list)) for _ in range(5)]
    # acquire the condition
    async with condition:
        # wait to be notified
        await condition.wait_for(lambda: len(work_list) == 5)
        # report final message
        print(f"Done, got: {work_list}")


# run the asyncio program
asyncio.run(main())
# Task added 0.19546561872529444
# Task added 0.9441654755668607
# Task added 0.9197856330867586
# Task added 0.2262295121554686
# Task added 0.5082505194406802
# Done, got: [0.19546561872529444, 0.9441654755668607, 0.9197856330867586, 0.2262295121554686, 0.5082505194406802]
