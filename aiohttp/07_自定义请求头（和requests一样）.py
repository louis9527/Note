import asyncio
import aiohttp


async def func1(url, params, filename):
    async with aiohttp.ClientSession() as session:
        headers = {'Content-Type': 'text/html; charset=utf-8'}
        async with session.get(url, params=params, headers=headers) as r:
            with open(filename, "wb") as fp:
                while True:
                    chunk = await r.content.read(10)
                    if not chunk:
                        break
                    fp.write(chunk)
