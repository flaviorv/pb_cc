import multiprocessing.process
import numpy as np
from time import time
import multiprocessing

def sum_sub(sub, queue):
    amount = 0
    for element in sub:
        amount += element
    queue.put(amount)

def parallel_sum(threads, list):
    queue = multiprocessing.Queue()
    processes = []
    amount = 0
    size = len(list)
    chunk = size//threads
    for i in range(threads):
        start = i*chunk
        end = start+chunk
        if i == threads -1:
            end = size
        sub = list[start:end]
        process = multiprocessing.Process(target=sum_sub, args=(sub, queue))
        processes.append(process)
        process.start()
    for process in processes:
        process.join()
    for _ in range(len(processes)):
        amount += queue.get()
    print("Parallel result:", amount)

def sequential_sum(list):
    amount = 0
    for element in list:
        amount += element
    print("Sequential result:", amount)

if __name__ == "__main__":
    print("Creating a list...")
    list = np.random.randint(1, 100, size=100_000_000, dtype=np.uint32)
    print(f"List with {list.shape[0]} elements and {list.nbytes/(1024**3):.1f} GB was created")
    print(list)
    start = time()
    sequential_sum(list)
    print("Time:", round((time()-start), 3), "seconds")
    start = time()
    parallel_sum(8, list)
    print("Time:", round((time()-start), 3), "seconds")
