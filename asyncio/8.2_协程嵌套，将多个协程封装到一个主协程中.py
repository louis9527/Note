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

    # dones, pendings = await asyncio.wait(tasks)
    # for task in dones:  # 对已完成的任务集合进行操作
    #     print("Task ret: ", task.result())

    # 也可以直接使用gather直接获取值
    results = await asyncio.gather(*tasks)
    for result in results:
        print("Task ret: ", result)


if __name__ == "__main__":
    begin = time.time()

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
    end = time.time()
    print(end - begin)


