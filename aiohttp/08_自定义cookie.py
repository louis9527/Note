import asyncio
import aiohttp


class ClientSession:
    """
    注意：
        对于自定义cookie，我们需要设置在ClientSession(cookies=自定义cookie字典),而不是session.get()中
    """
    def __init__(self, *, connector=None, loop=None, cookies=None,
                 headers=None, skip_auto_headers=None,
                 auth=None, json_serialize=json.dumps,
                 request_class=ClientRequest, response_class=ClientResponse,
                 ws_response_class=ClientWebSocketResponse,
                 version=http.HttpVersion11,
                 cookie_jar=None, connector_owner=True, raise_for_status=False,
                 read_timeout=sentinel, conn_timeout=None,
                 timeout=sentinel,
                 auto_decompress=True, trust_env=False,
                 trace_configs=None):
        pass


# 使用：
cookies = {'cookies_are': 'working'}
async with ClientSession(cookies=cookies) as session:
    pass













