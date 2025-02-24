import numpy as np
from parallel_bs import bs
from random import randrange
from time import time

start = 5
end = 80_000_005
time_s = time()
for _ in range(5):    
    print(f"\33[34mCreating an Array as a Binary Tree...\33[0m")
    arr = np.arange(start, end)
    arr_len =  arr.shape[0]
    print(f"\33[34mBinary Tree created in {round((time() - time_s), 3)} seconds. Length: {arr_len:_}. GB: {arr.nbytes/(1_024**3):.1f}\33[0m")
    end = end * 2 - start
    bs(arr, 5)
    bs(arr, arr_len)
    bs(arr, randrange(5, arr_len))
    bs(arr, randrange(5, arr_len))
    bs(arr, randrange(5, arr_len))
    bs(arr, 4)


def sequential_bs(arr, n):
    low = 0
    high = len(arr) -1
    middle = (low + high) // 2
    index = -1
    print(f"Searching for {n}")
    while (low <= high):
        if arr[middle] == n:
            index = middle
            return index
        elif arr[middle] < n:
            low = middle +1
            middle = (low + high) // 2
        else:
            high = middle -1
            middle =  (low + high) // 2
    return "Not found"

arr = np.arange(0, 80_000_000)

time_s = time()
print(sequential_bs(arr, randrange(0, len(arr)-1)))
print(sequential_bs(arr, 0))
print(f"seconds", round(round((time() - time_s), 3)))

#the sequential code took 0 seconds too
#maybe a binary tree class allows the input be greater
#with numpy the memory has already reached 9.5GB


