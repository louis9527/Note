import asyncio
import time

"""
使用async关键字定义的协程对象，使用await可以针对耗时的操作
进行挂起（是生成器中的yield的替代，但是本地协程函数不允许使用），让出当前控制权。
协程遇到await，事件循环将会挂起该协程，执行别的协程，直到其他协程也挂起，或者执行完毕，在进行下一个协程的执行

使用asyncio.sleep模拟阻塞操作。

"""


async def func1(num):
    print(num, 'before---func1----')
    await asyncio.sleep(num)
    return "recv num %s" % num


if __name__ == "__main__":
    begin = time.time()

    coroutine1 = func1(5)
    coroutine2 = func1(3)
    loop = asyncio.get_event_loop()
    task1 = asyncio.ensure_future(coroutine1)
    task2 = asyncio.ensure_future(coroutine2)
    tasks = asyncio.gather(*[task1, task2])  # gather可以实现同时注册多个任务，实现并发操作。wait方法使用一致
    loop.run_until_complete(tasks)
    loop.close()
    end = time.time()
    print(end - begin)
