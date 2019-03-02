import asyncio
import aiohttp

"""
注意1：
    我们获取的session.get()是Response对象，他继承于StreamResponse
    
注意2：
    async with session.get(url,params=params) as r:　　#异步上下文管理器
    with open(filename,"wb") as fp:　　#普通上下文管理器
    
    两者的区别：
        在于异步上下文管理器中定义了__aenter__和__aexit__方法
        异步上下文管理器指的是在enter和exit方法处能够暂停执行的上下文管理器
         为了实现这样的功能，需要加入两个新的方法：__aenter__ 和__aexit__。这两个方法都要返回一个 awaitable类型的值。
    
    推文：
        (https://blog.csdn.net/tinyzhao/article/details/52684473)
        异步上下文管理器async with和异步迭代器async for
"""


async def func1(url, params):
    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as r:
            print(await r.content.read(10))  # 读取前10字节


async def func2(url, params, filename):
    """
    下面字节流形式读取数据，保存文件
    """
    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as r:
            with open(filename, "wb") as fp:
                while True:
                    chunk = await r.content.read(10)
                    if not chunk:
                        break
                    fp.write(chunk)


tasks = [func2('https://www.ckook.com/forum.php', {"gid": 6}, "1.html"), ]
