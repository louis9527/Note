import asyncio
import aiohttp


async def func1(url, params):
    """只需要将参数字典，传入params参数中即可"""
    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as r:
            print(r.url)
            print(await r.read())


tasks = [func1('https://www.ckook.com/forum.php', {"gid": 6}), ]

event_loop = asyncio.get_event_loop()
results = event_loop.run_until_complete(asyncio.gather(*tasks))
event_loop.close()
