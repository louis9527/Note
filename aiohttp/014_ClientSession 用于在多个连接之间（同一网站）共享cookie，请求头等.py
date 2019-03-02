async def func1():
    cookies = {'my_cookie': "my_value"}
    async with aiohttp.ClientSession(cookies=cookies) as session:
        async with session.get("https://segmentfault.com/q/1010000007987098") as r:
            print(session.cookie_jar.filter_cookies("https://segmentfault.com"))
        async with session.get("https://segmentfault.com/hottest") as rp:
            print(session.cookie_jar.filter_cookies("https://segmentfault.com"))


"""
Set-Cookie: PHPSESSID=web2~d8grl63pegika2202s8184ct2q
Set-Cookie: my_cookie=my_value
Set-Cookie: PHPSESSID=web2~d8grl63pegika2202s8184ct2q
Set-Cookie: my_cookie=my_value

我们最好使用session.cookie_jar.filter_cookies()获取网站cookie，
不同于requests模块，虽然我们可以使用rp.cookies有可能获取到cookie，但似乎并未获取到所有的cookies。
"""


async def func2():
    """

    """
    cookies = {'my_cookie': "my_value"}
    async with aiohttp.ClientSession(cookies=cookies) as session:
        async with session.get("https://segmentfault.com/q/1010000007987098") as rp:
            print(session.cookie_jar.filter_cookies("https://segmentfault.com"))
            print(rp.cookies)  # Set-Cookie: PHPSESSID=web2~jh3ouqoabvr4e72f87vtherkp6; Domain=segmentfault.com;
            # Path=/　　#首次访问会获取网站设置的cookie
            async with session.get("https://segmentfault.com/hottest") as rp:
                print(session.cookie_jar.filter_cookies("https://segmentfault.com"))
                print(rp.cookies)  # 为空，服务端未设置cookie
                async with session.get("https://segmentfault.com/newest") as rp:
                    print(session.cookie_jar.filter_cookies("https://segmentfault.com"))
                    print(rp.cookies)  # 为空，服务端未设置cookie


"""
总结：

    当我们使用rp.cookie时，只会获取到当前url下设置的cookie,不会维护整站的cookie
    而session.cookie_jar.filter_cookies("https://segmentfault.com")会一直保留这个
    网站的所有设置cookies，含有我们在会话时设置的cookie，并且会根据响应修改更新cookie。这个才是我们需要的
    而我们设置cookie，也是需要在aiohttp.ClientSession(cookies=cookies)中设置

ClientSession 还支持 请求头，keep-alive连接和连接池(connection pooling)
"""
