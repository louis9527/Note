import asyncio
import threading
import time


async def func1(num):
    print(num, 'before---func1----')
    await asyncio.sleep(num)
    return "recv num %s" % num


def start_loop(loop):
    asyncio.set_event_loop(loop)
    loop.run_forever()


if __name__ == "__main__":
    begin = time.time()

    coroutine1 = func1(5)
    coroutine2 = func1(3)
    coroutine3 = func1(4)

    new_loop = asyncio.new_event_loop()  # 在当前线程下创建事件循环，（未启用）
    t = threading.Thread(target=start_loop, args=(new_loop,))  # 开启新的线程去启动事件循环
    t.start()

    # 主线程通过run_coroutine_threadsafe新注册协程对象。
    # 这样就能在子线程中进行事件循环的并发操作，同时主线程又不会被block。
    asyncio.run_coroutine_threadsafe(coroutine1, new_loop)  # 传参必须是协程对象
    asyncio.run_coroutine_threadsafe(coroutine2, new_loop)
    asyncio.run_coroutine_threadsafe(coroutine3, new_loop)

    end = time.time()
    print(end - begin)  # 当前线程未阻塞，耗时0.010000467300415039

"""
执行结果参考：
    5 before---func1----
    3 before---func1----
    4 before---func1----
    0.010000467300415039

"""
