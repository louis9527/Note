import asyncio
import threading
import time


def func1(num):
    print(num, 'before---func1----')
    time.sleep(num)
    return "recv num %s" % num


def start_loop(loop):
    asyncio.set_event_loop(loop)
    loop.run_forever()


if __name__ == "__main__":
    begin = time.time()

    new_loop = asyncio.new_event_loop()  # 在当前线程下创建时间循环，（未启用）
    t = threading.Thread(target=start_loop, args=(new_loop,))  # 开启新的线程去启动事件循环
    t.start()

    new_loop.call_soon_threadsafe(func1, 3)
    new_loop.call_soon_threadsafe(func1, 2)
    new_loop.call_soon_threadsafe(func1, 6)

    end = time.time()
    print(end - begin)  # 当前线程未阻塞，耗时0.02800154685974121

"""
执行结果：
    3 before---func1----
    0.02800154685974121
    2 before---func1----
    6 before---func1----
    
"""
