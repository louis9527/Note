import asyncio, time
from inspect import getcoroutinestate

"""
 深入了解:关于Task,create_task(),ensure_future都可以用来创建任务，那么应该使用哪个？
    条件使用ensure_future,他是最外层函数，其中调用了create_task()方法，功能全面，而Task官方不推荐直接使用
    asyncio.ensure_future(coroutine) 和 loop.create_task(coroutine)都可以创建一个task，run_until_complete的参数
    是一个futrue对象。当传入一个协程，其内部会自动封装成task，task是Future的子类。isinstance(task, asyncio.Future)将会输出True。
"""


async def func1(num):
    print(num, 'before---func1----')


if __name__ == "__main__":
    begin = time.time()

    coroutine = func1(2)

    loop = asyncio.get_event_loop()

    task = loop.create_task(coroutine)  # 创建了任务
    print(task)  # pending
    # 协程的4种状态
    # 协程在运行中的四种状态
    # GEN_CREATE: 等待开始执行
    # GEN_RUNNING: 解释器正在执行，这个状态一般看不到
    # GEN_SUSPENDED: 在yield表达式处暂停
    # GEN_CLOSED: 执行结束
    print(getcoroutinestate(coroutine))
    loop.run_until_complete(task)
    loop.close()
    print(task)  # finished
    print(getcoroutinestate(coroutine))

    # loop.run_until_complete(task)
    # loop.close()
    # print(task)  # finished
    # end = time.time()
    # print(end - begin)
