import aiohttp


# aiohttp支持使用代理来访问网页：
async with aiohttp.ClientSession() as session:
    async with session.get("http://python.org",
                           proxy="http://some.proxy.com") as resp:
        print(resp.status)


# 当然也支持需要授权的页面：
async with aiohttp.ClientSession() as session:
    proxy_auth = aiohttp.BasicAuth('user', 'pass')  # 用户，密码
    async with session.get("http://python.org",
                           proxy="http://some.proxy.com",
                           proxy_auth=proxy_auth) as resp:
        print(resp.status)


# 或者通过这种方式来验证授权：
session.get("http://python.org", proxy="http://user:pass@some.proxy.com")
