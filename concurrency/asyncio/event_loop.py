import asyncio

loop = asyncio.get_event_loop()

def callback():
    print("Hello World")
    loop.stop()

loop.call_later(1.0, callback)
loop.run_forever()
