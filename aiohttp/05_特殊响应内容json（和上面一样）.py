import asyncio
import aiohttp


async def func1(url, params):
    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as r:
            print(r.url)
            print(r.charset)
            print(await r.json())  # 可以设置编码，设置处理函数
