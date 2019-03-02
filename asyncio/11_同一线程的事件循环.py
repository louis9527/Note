import asyncio
import time

"""
在当前线程中创建一个事件循环（不启用，单纯获取标识），开启一个新的线程，在新的线程中
启动事件循环。在当前线程依据事件循环标识，可以向事件中添加协程对象。当前线程不会由于事件循环而阻塞了。

上面在一个线程中执行的事件循环，只有我们主动关闭事件close，事件循环才会结束，会阻塞。

"""


async def func1(num):
    print(num, 'before---func1----')
    await asyncio.sleep(num)
    return "recv num %s" % num


if __name__ == "__main__":
    begin = time.time()

    coroutine1 = func1(5)
    coroutine2 = func1(3)
    coroutine3 = func1(4)

    tasks = [
        asyncio.ensure_future(coroutine1),
        asyncio.ensure_future(coroutine2),
        asyncio.ensure_future(coroutine3),
    ]

    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
    loop.run_forever()
    end = time.time()
    print(end - begin)
