import asyncio
import time


@asyncio.coroutine  # 设为异步函数
def func1(num):
    print(num, 'before---func1----')
    yield from asyncio.sleep(5)
    print(num, 'after---func1----')


task = [func1(1), func1(2)]

if __name__ == "__main__":
    begin = time.time()
    loop = asyncio.get_event_loop()  # 进入事件循环
    loop.run_until_complete(asyncio.gather(*task))  # 将协同程序注册到事件循环中
    loop.close()
    end = time.time()
    print(end - begin)
