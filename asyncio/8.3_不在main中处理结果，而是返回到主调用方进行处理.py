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

    return await asyncio.gather(*tasks)


if __name__ == "__main__":
    begin = time.time()

    loop = asyncio.get_event_loop()
    results = loop.run_until_complete(main())
    for result in results:
        print("Task ret: ", result)
    loop.close()
    end = time.time()
    print(end - begin)
