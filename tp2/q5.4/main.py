from max import pget, sget
from time import time
import numpy as np



size = 1_200_000_000
print(f"Creating an array with {size} elements")
start = time()
arr = np.random.randint(0, 10_000, size=size, dtype=np.int32)
print(f"Array with {arr.nbytes/(1_024**3):.1f} GB was created in {round((time()-start), 3)} seconds")

start = time()
print(f"\33[33mParallel method - Maximum value: {pget(arr)}. Time: {round((time()-start), 3)} seconds")

_start = time()
print(f"\33[34mSequential method - Maximum value: {sget(arr)}. Time: {round((time()-_start), 3)} seconds")
print(f"\33[32m{arr}")

