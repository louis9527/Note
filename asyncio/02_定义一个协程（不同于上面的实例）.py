import asyncio
import time

"""
func1(2)　　# 由于使用async异步关键字，所以不能直接运行
　　  D:/MyPython/day25/mq/multhread.py:15: RuntimeWarning: coroutine 'func1' was never awaited
　　  func1(2)

print(type(func1),type(coroutine))　　#<class 'function'> <class 'coroutine'>

"""


async def func1(num):  # 使用async关键字定义一个协程，协程也是一种对象，不能直接运行，需要加入事件循环中，才能被调用。
    print(num, 'before---func1----')


if __name__ == "__main__":
    begin = time.time()
    coroutine = func1(2)
    # 我们可以使用send(None)
    # 调用协程（这里不这么使用），这里是将协程放入事件循环中进行处理
    # try:
    #     coroutine.send(None)
    # except StopIteration:
    #     pass
    loop = asyncio.get_event_loop()
    loop.run_until_complete(coroutine)
    loop.close()
    end = time.time()
    print(end - begin)

