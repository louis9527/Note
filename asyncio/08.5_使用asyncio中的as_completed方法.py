import asyncio
import time

"""
as_completed():
    Return an iterator whose values are coroutines.　　#返回一个可迭代的协程函数值
    
    When waiting for the yielded coroutines you'll get the results (or
    exceptions!) of the original Futures (or coroutines), in the order
    in which and as soon as they complete.

"""


async def func1(num):
    print(num, 'before---func1----')
    await asyncio.sleep(num)
    return "recv num %s" % num


async def main():
    coroutine1 = func1(5)
    coroutine2 = func1(3)
    coroutine3 = func1(4)

    tasks = [
        asyncio.ensure_future(coroutine1),
        asyncio.ensure_future(coroutine2),
        asyncio.ensure_future(coroutine3),
    ]

    for task in asyncio.as_completed(tasks):
        result = await task
        print("Task ret: ", result)


if __name__ == "__main__":
    begin = time.time()

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

    loop.close()
    end = time.time()
    print(end - begin)
