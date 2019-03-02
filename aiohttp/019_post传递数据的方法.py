import asyncio
import aiohttp


#（1）模拟表单
payload = {'key1': 'value1', 'key2': 'value2'}
async with session.post('http://httpbin.org/post',
                        data=payload) as resp:
    print(await resp.text())

"""
注意：data = dict的方式post的数据将被转码，和form提交数据是一样的作用，如果你不想被转码，可以直接以字符串的形式
data = str提交，这样就不会被转码。
"""


# （2）post json
payload = {'some': 'data'}

async with session.post(url, data=json.dumps(payload)) as resp:
    pass

"""其实json.dumps(payload)返回的也是一个字符串，只不过这个字符串可以被识别为json格式"""


# （3）post 小文件
url = 'http://httpbin.org/post'
files = {'file': open('report.xls', 'rb')}

await session.post(url, data=files)


url = 'http://httpbin.org/post'
data = FormData()
data.add_field('file',
               open('report.xls', 'rb'),
               filename='report.xls',
               content_type='application/vnd.ms-excel')

await session.post(url, data=data)

"""如果将文件对象设置为数据参数，aiohttp将自动以字节流的形式发送给服务器。"""


# （4）post 大文件
@aiohttp.streamer
def file_sender(writer, file_name=None):
    """aiohttp支持多种类型的文件以流媒体的形式上传，所以我们可以在文件未读入内存的情况下发送大文件。"""
    with open(file_name, 'rb') as f:
        chunk = f.read(2 ** 16)
        while chunk:
            yield from writer.write(chunk)
            chunk = f.read(2 ** 16)

# Then you can use `file_sender` as a data provider:
async with session.post('http://httpbin.org/post', data=file_sender(file_name='huge_file')) as resp:
    print(await resp.text())


# （5）从一个url获取文件后，直接post给另一个url
r = await session.get('http://python.org')
await session.post('http://httpbin.org/post', data=r.content)



#（6）post预压缩数据
"""在通过aiohttp发送前就已经压缩的数据, 调用压缩函数的函数名（通常是 deflate 或 zlib）作为content - encoding的值："""
async def my_coroutine(session, headers, my_data):
    data = zlib.compress(my_data)
    headers = {'Content-Encoding': 'deflate'}
    async with session.post('http://httpbin.org/post', data=data, headers=headers)
        pass









