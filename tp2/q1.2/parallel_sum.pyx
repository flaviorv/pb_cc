#cython: boundscheck=False
#cython: wraparound=False
from cython.parallel import prange
import numpy as np
cimport numpy as np
import time

def sum(unsigned long size, unsigned long max_range):
    cdef unsigned long i
    cdef unsigned long result
    result = 0
    content = {}

    start = round(time.time(), 3)
    cdef long long[:] numbers = np.random.randint(1, max_range, size=size)
    end = round(time.time(), 3)
    sec = end-start
    name = "numpy-pyx"
    print(f"{name} took {sec} seconds (pyx file)")
    content[name] = sec


    start = round(time.time(), 3)
    with nogil:
        for i in prange(size, schedule="guided"):
            result += numbers[i]
    end = round(time.time(), 3)
    name = "sum-parallel"
    sec = end-start
    print(f"{name} took {sec} seconds and the result is {result} (pyx file)")
    content[name] = sec
    
    return content