import asyncio
import time

"""
coroutine执行结束时候会调用回调函数。并通过参数future获取
协程执行的结果。我们创建的task和回调里的future对象，实际上是同一个对象。

"""


async def func1(num):
    print(num, 'before---func1----')
    return "recv num %s" % num


def callback(future):
    print(future.result())


if __name__ == "__main__":
    begin = time.time()

    coroutine1 = func1(1)
    loop = asyncio.get_event_loop()
    task1 = asyncio.ensure_future(coroutine1)
    task1.add_done_callback(callback)
    loop.run_until_complete(task1)
    loop.close()
    end = time.time()
    print(end - begin)
