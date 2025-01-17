import time
import asyncio
import aiohttp
import aiofiles
import os
import json
from concurrent.futures import ThreadPoolExecutor
from urls import urls

def drink_requests(session, urls):
    responses = []
    for url in urls:
        response = session.get(url)
        responses.append(response)
    return responses

async def save_drink(drink_name, drink_content):
    path = f"./drinks/{drink_name}.json"
    os.makedirs(os.path.dirname(path), exist_ok=True)
    async with aiofiles.open(path, 'w') as f:
        drink_json = json.dumps(drink_content, indent=2)
        await f.write(drink_json)


async def get_drinks(urls):
    async with aiohttp.ClientSession() as session:
        tasks = drink_requests(session, urls)
        responses = await asyncio.gather(*tasks)
        for response in responses:
            data = await response.json()
            if data["drinks"] != None:
                drink = data["drinks"][0]
                drink_name = drink['strDrink']
                print(drink_name)
                await save_drink(drink_name, drink)      


def loop(urls):    
    asyncio.run(get_drinks(urls))

def save_time(time_data):
    path = f"./times/threads_{time_data['threads']}.json"
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        time_data = json.dumps(time_data, indent=2)
        f.write(time_data)
        
def call_requests(threads):
    start = time.time()
    chunks = [urls[i::threads] for i in range(threads)]
    
    with ThreadPoolExecutor(max_workers=threads) as executor:
        executor.map(loop, chunks)
     
    end = time.time()
    total_time = round((end-start),2)
    print("Threads amount: {} Time: {} seconds".format(threads, total_time))
    time_data = {"threads": threads, "seconds": total_time}
    save_time(time_data)
    

call_requests(2)
time.sleep(10)
call_requests(4)
time.sleep(10)
call_requests(8)
time.sleep(10)
call_requests(16)
time.sleep(10)
call_requests(32)


