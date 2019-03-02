import asyncio
import aiohttp


url = "www.baidu.com"
async with session.get(url) as resp:
    print(resp.cookies)
