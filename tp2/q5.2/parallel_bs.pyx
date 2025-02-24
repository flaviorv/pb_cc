# cython: boundscheck=False, wraparound=False, initializedcheck=False
cimport numpy as np
import numpy as np
from cython.parallel import prange, threadid
cimport cython
from time import time

cdef c_bs(long long[:] btree, long long n):
    cdef unsigned long i
    cdef Py_ssize_t size = btree.shape[0] -1
    cdef Py_ssize_t middle = size // 2
    cdef unsigned long threads = 4
    cdef unsigned long chunck = size // threads
    cdef Py_ssize_t high = size
    cdef Py_ssize_t low = 0
    cdef long long index
    print(f"Searching for {n}...")
    start = time()
    cdef int cpu
    with nogil:
        for i in prange(threads, num_threads=threads, schedule="static"):
            low = i*chunck
            high = low + chunck
            middle = (low + high) // 2
            index = -1
            while (low <= high):
                if btree[middle] == n:
                    with gil:
                        index = middle
                        return 
                elif btree[middle] < n:
                    low = middle +1
                    middle = (low + high) // 2
                else:
                    high = middle -1
                    middle =  (low + high) // 2
    print("Not found" if index == -1 else f"Found at index \33[31m{index}\33[0m")
    print("Time:\33[31m", round((time() - start), 3), "\33[0mseconds")
    
    

def bs(long long[:] b_tree, long long n):
    return c_bs(b_tree, n)