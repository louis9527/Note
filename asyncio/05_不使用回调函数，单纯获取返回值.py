import asyncio
import time


async def func1(num):
    print(num, 'before---func1----')
    return "recv num %s" % num


if __name__ == "__main__":
    begin = time.time()

    coroutine1 = func1(1)
    loop = asyncio.get_event_loop()
    task1 = asyncio.ensure_future(coroutine1)
    loop.run_until_complete(task1)
    print(task1)
    # 当task状态为finished时候，我们可以直接使用result方法（在future模块）获取返回值
    print(task1.result())
    loop.close()
    end = time.time()
    print(end - begin)
