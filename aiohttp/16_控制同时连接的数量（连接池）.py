"""
限制同时打开限制同时打开连接到同一端点的数量（(host, port, is_ssl) 三的倍数），可以通过设置 limit_per_host 参数：

limit_per_host： 同一端点的最大连接数量。同一端点即(host, port, is_ssl)完全相同

conn = aiohttp.TCPConnector(limit_per_host=30)#默认是0
在协程下测试效果不明显

"""

async def func1():
    """"TCPConnector维持链接池，限制并行连接的总量，当池满了，有请求退出再加入新请求"""
    cookies = {'my_cookie': "my_value"}
    conn = aiohttp.TCPConnector(limit=2)  # 默认100，0表示无限
    async with aiohttp.ClientSession(cookies=cookies, connector=conn) as session:
        for i in range(7, 35):
            url = "https://www.ckook.com/list-%s-1.html" % i
            async with session.get(url) as rp:
                print('---------------------------------')
                print(rp.status)
