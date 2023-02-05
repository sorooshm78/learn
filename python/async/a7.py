import aiohttp
import asyncio


async def get_status_request(session, url):
    async with session.get(url) as response:
        return response.status


async def main():
    async with aiohttp.ClientSession() as session:
        status = await get_status_request(session, url="http://python.org")
        print(status)


# loop = asyncio.get_event_loop()
# loop.run_until_complete(main())
# this is same above
asyncio.run(main())
# 200


##############################
