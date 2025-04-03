import time
import asyncio
import aiohttp
import aiofiles
import os
import json
from urls import urls

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.json()

async def save_drink(drink_name, drink_content):
    path = f"./drinks/{drink_name}.json"
    os.makedirs(os.path.dirname(path), exist_ok=True)
    async with aiofiles.open(path, 'w') as f:
        drink_json = json.dumps(drink_content, indent=2)
        await f.write(drink_json)

async def get_drinks(urls, max_concurrent):
    semaphore = asyncio.Semaphore(max_concurrent)
    async with aiohttp.ClientSession() as session:
        async def limited_fetch(url):
            async with semaphore:
                return await fetch(session, url)
        tasks = [limited_fetch(url) for url in urls]
        responses = await asyncio.gather(*tasks)
        for data in responses:
            if data and "drinks" in data and data["drinks"]:
                drink = data["drinks"][0]
                drink_name = drink['strDrink']
                print(drink_name)
                await save_drink(drink_name, drink)

def save_time(time_data):
    path = f"./times/threads_{time_data['threads']}.json"
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        time_data = json.dumps(time_data, indent=2)
        f.write(time_data)

def run_experiment(threads):
    start = time.time()
    asyncio.run(get_drinks(urls, threads))
    end = time.time()
    total_time = round((end - start), 2)
    print(f"Threads: {threads} | Time: {total_time} segundos")
    save_time({"threads": threads, "seconds": total_time})

def call_requests():
    for threads in [8, 4, 1]:
        run_experiment(threads)
        time.sleep(10)
