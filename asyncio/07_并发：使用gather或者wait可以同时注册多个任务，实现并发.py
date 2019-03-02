
# gather：Return a future aggregating results from the given coroutines or futures.　　返回结果
task1 = asyncio.ensure_future(coroutine1)
task2 = asyncio.ensure_future(coroutine2)
tasks = asyncio.gather(*[task1, task2])
loop.run_until_complete(tasks)


# wait：Returns two sets of Future: (done, pending).
# #返回dones是已经完成的任务，pending是未完成的任务，都是集合类型
task1 = asyncio.ensure_future(coroutine1)
task2 = asyncio.ensure_future(coroutine2)
tasks = asyncio.wait([task1, task2])
loop.run_until_complete(tasks)


# Usage:
done, pending = yield from asyncio.wait(fs)


# wait是接收一个列表，而后gather是接收一堆任务数据。
# 两者的返回值也是不同的