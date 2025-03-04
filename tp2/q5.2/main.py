import numpy as np
from parallel_bs import bs
from seq_binary_search import sequential_bs
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

    print("\33[33mSingle Thread")
    time_s = time()
    print(sequential_bs(arr, randrange(0, len(arr)-1)))
    print(sequential_bs(arr, 0))
    print(f"seconds", round(round((time() - time_s), 3)), "\33[0m")


#the sequential code took 0 seconds too
#maybe a binary tree class allows the input be greater
#with numpy the memory has already reached 9.5GB


