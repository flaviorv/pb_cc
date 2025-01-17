import asyncio

async def hello():
    await asyncio.sleep(3)
    print("Hello, async!")

coro = hello()
print(coro)
loop = asyncio.get_event_loop()
loop.run_until_complete(coro)

async def network_request(number):
    await asyncio.sleep(3.0)
    return {"success": True, "result": number**2}


async def fetch_square(number):
    response = await network_request(number)
    if response["success"]:
        print("Result is: {}".format(response["result"]))

asyncio.ensure_future(fetch_square(2))
asyncio.ensure_future(fetch_square(3))
loop.run_until_complete(fetch_square(2))
loop.run_until_complete(fetch_square(3))
