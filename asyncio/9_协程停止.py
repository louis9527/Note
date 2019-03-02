import asyncio
import time
"""
future对象有几个状态：
        Pending
        Running
        Done
        Cacelled
    创建future的时候，task为pending，
    事件循环调用执行的时候当然就是running，
    调用完毕自然就是done，
    如果需要停止事件循环，就需要先把task取消。
    可以使用asyncio.Task获取事件循环的task

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
    try:
        loop.run_until_complete(asyncio.wait(tasks))
    except KeyboardInterrupt as e:
        print(asyncio.Task.all_tasks())
        for task in asyncio.Task.all_tasks():  # 获取所有任务
            print(task.cancel())  # 单个任务取消
        loop.stop()  # 需要先stop循环
        loop.run_forever()  # 需要在开启事件循环
    finally:
        loop.close()  # 统一关闭
    end = time.time()
    print(end - begin)


"""
执行终端异常捕获时打印的结果：
    5 before---func1----
    3 before---func1----
    4 before---func1----
    {<Task pending coro=<func1() running at multhread.py:5> wait_for=<Future pending cb=[Task._wakeup()]> cb=[_wait.<loc
    als>._on_completion() at C:\Users\Administrator\AppData\Local\Programs\Python\Python35\lib\asyncio\tasks.py:428]>, <
    Task pending coro=<wait() running at C:\Users\Administrator\AppData\Local\Programs\Python\Python35\lib\asyncio\tasks
    .py:361> wait_for=<Future pending cb=[Task._wakeup()]>>, <Task pending coro=<func1() running at multhread.py:5> wait
    _for=<Future pending cb=[Task._wakeup()]> cb=[_wait.<locals>._on_completion() at C:\Users\Administrator\AppData\Loca
    l\Programs\Python\Python35\lib\asyncio\tasks.py:428]>, <Task pending coro=<func1() running at multhread.py:5> wait_f
    or=<Future pending cb=[Task._wakeup()]> cb=[_wait.<locals>._on_completion() at C:\Users\Administrator\AppData\Local\
    Programs\Python\Python35\lib\asyncio\tasks.py:428]>}　　#未处理，刚刚挂起为pending状态
    True　　#返回True，表示cancel取消成功
    True
    True
    True
    3.014172315597534
    
结果分析：
    True表示cannel成功，loop stop之后还需要再次开启事件循环，最后在close，不然还会抛出异常：

cancel前后task的状态分析：
    分析：
        Task was destroyed but it is pending! 因为cancel后task的状态依旧是pending
    
    测试代码：
        for task in asyncio.Task.all_tasks():
            print(task)
            print(task.cancel())
            print(task)
            
    终端打印结果：
        <Task pending coro=<func1() running at multhread.py:5> wait_for=<Future pending cb=[Task._wakeup()]> cb=[_wait.<loca
        ls>._on_completion() at C:\Users\Administrator\AppData\Local\Programs\Python\Python35\lib\asyncio\tasks.py:428]>
        True
        <Task pending coro=<func1() running at multhread.py:5> wait_for=<Future cancelled> cb=[_wait.<locals>._on_completion
        () at C:\Users\Administrator\AppData\Local\Programs\Python\Python35\lib\asyncio\tasks.py:428]>
"""




































