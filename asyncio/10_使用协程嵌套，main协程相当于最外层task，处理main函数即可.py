import asyncio
import time


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

    dones, pendings = await asyncio.wait(tasks)

    for task in dones:
        print("Task ret: ", task.result())


if __name__ == "__main__":
    begin = time.time()

    loop = asyncio.get_event_loop()
    task = asyncio.ensure_future(main())
    try:
        loop.run_until_complete(task)
    except KeyboardInterrupt as e:
        # 我们只是把上面的单个写成了所有任务集合取消，和协程嵌套关系不大。上面也可以这样写。不过协程嵌套可以简化代码
        print(asyncio.gather(*asyncio.Task.all_tasks()).cancel())
        loop.stop()
        loop.run_forever()
    finally:
        loop.close()
    end = time.time()
    print(end - begin)

"""
执行结果：
    5 before---func1----
    3 before---func1----
    4 before---func1----
    <class 'asyncio.tasks._GatheringFuture'>
    True
    3.008172035217285

"""


async def func2(num):
    print(num, 'before---func1----')
    await asyncio.sleep(num)
    return "recv num %s" % num


if __name__ == "__main__":
    begin = time.time()

    coroutine1 = func2(5)
    coroutine2 = func2(3)
    coroutine3 = func2(4)

    tasks = [
        asyncio.ensure_future(coroutine1),
        asyncio.ensure_future(coroutine2),
        asyncio.ensure_future(coroutine3),
    ]

    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(asyncio.wait(tasks))
    except KeyboardInterrupt as e:
        print(asyncio.gather(*tasks).cancel())
        loop.stop()
        loop.run_forever()
    finally:
        loop.close()
    end = time.time()
    print(end - begin)


"""
执行结果：
    5 before---func1----
    3 before---func1----
    4 before---func1----
    True
    3.008171796798706

"""
