"""
默认的IO操作都有5分钟的响应时间 我们可以通过 timeout 进行重写：
如果 timeout=None 或者 timeout=0 将不进行超时检查，也就是不限时长。
"""


async with session.get('https://github.com', timeout=60) as r:
    pass
