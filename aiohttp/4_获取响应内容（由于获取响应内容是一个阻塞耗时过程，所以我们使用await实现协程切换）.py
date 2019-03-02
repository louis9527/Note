import asyncio
import aiohttp

"""
注意：
    text(),read()方法是把整个响应体读入内存，如果你是获取大量的数据，请考虑使用”字节流“（StreamResponse）
"""


async def func1(url, params):
    """（1）使用text()方法"""
    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as r:
            print(r.url)
            print(r.charset)  # 查看默认编码为utf-8
            print(await r.text())  # 不编码，则是使用默认编码　　使用encoding指定编码


async def func2(url, params):
    """（2）使用read()方法，不进行编码，为字节形式"""
    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as r:
            print(r.url)
            print(await r.read())



