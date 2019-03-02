async with session.get(url) as resp:
    print(resp.status)