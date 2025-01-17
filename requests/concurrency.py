import threading
import requests
import time
from ping import ping, urls

start = time.time()

threads = []

def get_async_urls(threads_amount):
    urls_portion = 1
    if 0 < threads_amount <= len(urls):
        urls_portion = len(urls) // threads_amount
    else:
        raise Exception("Threads amount is out of range")
    
    for i in range(0, len(urls), +urls_portion):
        print(urls[i:i+urls_portion])
    #     thread = threading.Thread(target=ping, args=(urls[i:urls_portion],))
    #     threads.append(thread)
    #     thread.start()

    # for thread in threads:
    #     thread.join()


get_async_urls(4)
print(f"Threading: {time.time() - start} seconds")

