import asyncio
import aiohttp
import time

async def show_status(session, url):
    async with session.get(url) as res:
        print(f"status url {url} is {res.status}")


async def main():
    async with aiohttp.ClientSession() as session:
        requests = [
            asyncio.create_task(show_status(session, "https://docs.python.org/")),
            asyncio.create_task(show_status(session, "https://docs.python.org/")),
            asyncio.create_task(show_status(session, "https://docs.python.org/")),
            asyncio.create_task(show_status(session, "https://docs.python.org/")),
        ]

        done, pending = await asyncio.wait(requests)
        print(f'done : {done}')
        print(f'pending : {pending}')


asyncio.run(main())



#####################


async def say_after(delay, what):
    print(f"befor sleep {what}")
    await asyncio.sleep(delay)
    print(f"after sleep {what}")


async def main():
    tasks = [
        asyncio.create_task(say_after(4, "task4")),
        asyncio.create_task(say_after(3, "task3")),
        asyncio.create_task(say_after(2, "task2")),
        asyncio.create_task(say_after(1, "task1")),
    ]

    # return_when=asyncio.ALL_COMPLETED
    done, pending = await asyncio.wait(tasks)
    
    print(f'done : {done}')
    print(f'pending : {pending}')



asyncio.run(main())
# befor sleep task4
# befor sleep task3
# befor sleep task2
# befor sleep task1
# after sleep task1
# after sleep task2
# after sleep task3
# after sleep task4
# done : {<Task finished name='Task-2' coro=<say_after() done, defined at /home/sm/src/learn/python/async/a9.py:31> result=None>, <Task finished name='Task-4' coro=<say_after() done, defined at /home/sm/src/learn/python/async/a9.py:31> result=None>, <Task finished name='Task-5' coro=<say_after() done, defined at /home/sm/src/learn/python/async/a9.py:31> result=None>, <Task finished name='Task-3' coro=<say_after() done, defined at /home/sm/src/learn/python/async/a9.py:31> result=None>}
# pending : set()

#######################

async def say_after(delay, what):
    print(f"befor sleep {what}")
    await asyncio.sleep(delay)
    print(f"after sleep {what}")


async def main():
    tasks = [
        asyncio.create_task(say_after(4, "task4")),
        asyncio.create_task(say_after(3, "task3")),
        asyncio.create_task(say_after(2, "task2")),
        asyncio.create_task(say_after(1, "task1")),
    ]

    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    
    print(f'done : {done}')
    print(f'pending : {pending}')



asyncio.run(main())
# befor sleep task4
# befor sleep task3
# befor sleep task2
# befor sleep task1
# after sleep task1
# done : {<Task finished name='Task-5' coro=<say_after() done, defined at /home/sm/src/learn/python/async/a9.py:67> result=None>}
# pending : {<Task pending name='Task-2' coro=<say_after() running at /home/sm/src/learn/python/async/a9.py:69> wait_for=<Future pending cb=[Task.task_wakeup()]>>, <Task pending name='Task-4' coro=<say_after() running at /home/sm/src/learn/python/async/a9.py:69> wait_for=<Future pending cb=[Task.task_wakeup()]>>, <Task pending name='Task-3' coro=<say_after() running at /home/sm/src/learn/python/async/a9.py:69> wait_for=<Future pending cb=[Task.task_wakeup()]>>}


#######################

async def say_after(delay, what):
    print(f"befor sleep {what}", time.strftime("%X"))
    await asyncio.sleep(delay)
    print(f"after sleep {what}", time.strftime("%X"))


async def main():
    tasks = [
        asyncio.create_task(say_after(4, "task4")),
        asyncio.create_task(say_after(3, "task3")),
        asyncio.create_task(say_after(2, "task2")),
        asyncio.create_task(say_after(1, "task1")),
    ]

    print("before wait main", time.strftime("%X"))
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    print("after wait main", time.strftime("%X"))
    
    print("before loop in pending", time.strftime("%X"))
    for p in pending:
        await p
    print("after loop in pending", time.strftime("%X"))

asyncio.run(main())
# before wait main 16:32:54
# befor sleep task4 16:32:54
# befor sleep task3 16:32:54
# befor sleep task2 16:32:54
# befor sleep task1 16:32:54
# after sleep task1 16:32:55
# after wait main 16:32:55
# before loop in pending 16:32:55
# after sleep task2 16:32:56
# after sleep task3 16:32:57
# after sleep task4 16:32:58
# after loop in pending 16:32:58

#######################

async def say_after(delay, what):
    print(f"befor sleep {what}", time.strftime("%X"))
    if delay == 2:
        raise Exception("something")
    await asyncio.sleep(delay)
    print(f"after sleep {what}", time.strftime("%X"))
    return what


async def main():
    tasks = [
        asyncio.create_task(say_after(3, "task3")),
        asyncio.create_task(say_after(2, "task2")),
        asyncio.create_task(say_after(1, "task1")),
    ]

    print("before wait main", time.strftime("%X"))
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_EXCEPTION)
    print("after wait main", time.strftime("%X"))
    
    print("before loop in pending", time.strftime("%X"))
    for p in pending:
        await p
    print("after loop in pending", time.strftime("%X"))

    print("pending", [p.result() for p in pending])
    print("done", done)

asyncio.run(main())
# before wait main 16:45:34
# befor sleep task3 16:45:34
# befor sleep task2 16:45:34
# befor sleep task1 16:45:34
# after wait main 16:45:34
# before loop in pending 16:45:34
# after sleep task1 16:45:35
# after sleep task3 16:45:37
# after loop in pending 16:45:37
# pending ['task3', 'task1']
# done {<Task finished name='Task-3' coro=<say_after() done, defined at /home/sm/src/learn/python/async/a9.py:139> exception=Exception('something')>}

#######################

async def say_after(delay, what):
    print(f"befor sleep {what}", time.strftime("%X"))
    await asyncio.sleep(delay)
    print(f"after sleep {what}", time.strftime("%X"))
    return what


async def main():
    tasks = [
        asyncio.create_task(say_after(5, "task5")),
        asyncio.create_task(say_after(4, "task4")),
        asyncio.create_task(say_after(2, "task2")),
        asyncio.create_task(say_after(1, "task1")),
    ]

    print("before wait main", time.strftime("%X"))
    done, pending = await asyncio.wait(tasks, timeout=3)
    print("after wait main", time.strftime("%X"))
    
    print("done", done)
    print("pending", pending)

    print("before loop in pending", time.strftime("%X"))
    for p in pending:
        await p
    print("after loop in pending", time.strftime("%X"))

    print("pending", [p.result() for p in pending])
    print("done", done)

asyncio.run(main())
# before wait main 16:57:03
# befor sleep task5 16:57:03
# befor sleep task4 16:57:03
# befor sleep task2 16:57:03
# befor sleep task1 16:57:03
# after sleep task1 16:57:04
# after sleep task2 16:57:05
# after wait main 16:57:06
# done {<Task finished name='Task-5' coro=<say_after() done, defined at /home/sm/src/learn/python/async/a9.py:182> result='task1'>, <Task finished name='Task-4' coro=<say_after() done, defined at /home/sm/src/learn/python/async/a9.py:182> result='task2'>}
# pending {<Task pending name='Task-3' coro=<say_after() running at /home/sm/src/learn/python/async/a9.py:184> wait_for=<Future pending cb=[Task.task_wakeup()]>>, <Task pending name='Task-2' coro=<say_after() running at /home/sm/src/learn/python/async/a9.py:184> wait_for=<Future pending cb=[Task.task_wakeup()]>>}
# before loop in pending 16:57:06
# after sleep task4 16:57:07
# after sleep task5 16:57:08
# after loop in pending 16:57:08
# pending ['task4', 'task5']
# done {<Task finished name='Task-5' coro=<say_after() done, defined at /home/sm/src/learn/python/async/a9.py:182> result='task1'>, <Task finished name='Task-4' coro=<say_after() done, defined at /home/sm/src/learn/python/async/a9.py:182> result='task2'>}
