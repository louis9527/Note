import asyncio
import aiohttp

"""
除了上面的get方法外，会话还支持post，put,delete....等
    session.put('http://httpbin.org/put', data=b'data')
    session.delete('http://httpbin.org/delete')
    session.head('http://httpbin.org/get')
    session.options('http://httpbin.org/get')
    session.patch('http://httpbin.org/patch', data=b'data')
"""


async def fetch_async(url):
    """
    不要为每次的连接都创建一次session,一般情况下只需要创建一个session，然后使用这个session执行所有的请求。
    每个session对象，内部包含了一个连接池，并且将会保持连接和连接复用（默认开启）可以加快整体的性能。
    """
    print(url)
    async with aiohttp.ClientSession() as session:  # 协程嵌套，只需要处理最外层协程即可fetch_async
        async with session.get(url) as resp:
            print(resp.status)
            print(await resp.text())  # 因为这里使用到了await关键字，实现异步，所有他上面的函数体需要声明为异步async


tasks = [fetch_async('http://www.baidu.com/'), fetch_async('http://www.cnblogs.com/ssyfj/')]

event_loop = asyncio.get_event_loop()
results = event_loop.run_until_complete(asyncio.gather(*tasks))
event_loop.close()
