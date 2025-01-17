from concurrent.futures import ThreadPoolExecutor, Future
import time

executor = ThreadPoolExecutor(max_workers=3)
def wait_and_return(msg, on_done):
    time.sleep(1.0)
    return on_done(msg)
print(executor.submit(wait_and_return, "Hello, executor"))

def on_done(result):
    print(result)

#------ with asyncio also works
import asyncio
loop = asyncio.get_event_loop()
fut = loop.run_in_executor(executor, wait_and_return, "Hello, asyncio executor", on_done)
loop.run_until_complete(fut)


#-----making requests
import requests

async def fetch_urls(urls):
    responses = []
    for url in urls:
        responses.append(await loop.run_in_executor(executor, requests.get, url))
    return responses

urls = [
    "http://www.google.com",
    "http://www.example.com",
    "http://www.facebook.com"
]
responses = loop.run_until_complete(fetch_urls(urls))
print(responses)

#----to show the content
# for response in responses:
    # print(response.text)
#--example
x = requests.get('https://w3schools.com/python/demopage.htm')
print(x.text)