import asyncio
import aiohttp


async def show_status(session, url, delay):
    await asyncio.sleep(delay)
    async with session.get(url) as res:
        print(f"status url {url} and delay {delay} is {res.status}")


async def main():
    async with aiohttp.ClientSession() as session:
        requests = [
            show_status(session, "https://docs.python.org/", 2),
            show_status(session, "https://docs.python.org/", 4),
            show_status(session, "https://docs.python.org/", 6),
            show_status(session, "https://docs.python.org/", 8),
        ]

        for res in asyncio.as_completed(requests):
            await res


asyncio.run(main())
# status url https://docs.python.org/ and delay 2 is 200
# status url https://docs.python.org/ and delay 4 is 200
# status url https://docs.python.org/ and delay 6 is 200
# status url https://docs.python.org/ and delay 8 is 200


#####################


async def say_after(delay, what):
    print(f"befor sleep {what}")
    await asyncio.sleep(delay)
    print(f"after sleep {what}")
    return f"success {what}"


async def main():
    tasks = [
        say_after(4, "task4"),
        say_after(3, "task3"),
        say_after(2, "task2"),
        say_after(1, "task1"),
    ]

    for task in asyncio.as_completed(tasks):
        print("main before await")
        result = await task
        print("main after await")
        print(f"result {result}")


asyncio.run(main())
# main before await

# befor sleep task2
# befor sleep task3
# befor sleep task4
# befor sleep task1
# after sleep task1

# main after await
# result success task1

# main before await
# after sleep task2
# main after await
# result success task2

# main before await
# after sleep task3
# main after await
# result success task3

# main before await
# after sleep task4
# main after await
# result success task4
