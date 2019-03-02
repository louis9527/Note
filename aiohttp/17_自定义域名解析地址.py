"""
我们可以指定域名服务器的IP对我们提供的get或post的url进行解析：

"""

from aiohttp.resolver import AsyncResolver

resolver = AsyncResolver(nameservers=["8.8.8.8", "8.8.4.4"])
conn = aiohttp.TCPConnector(resolver=resolver)