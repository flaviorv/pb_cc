# cython: boundscheck=False, wraparound=False, initializedcheck=False
# with boundscheck and the others, the sequential is faster than the parallel
from cython.parallel import prange
import numpy as np

cdef int get_max_value(int[:] arr):
    cdef unsigned long size = arr.shape[0]
    cdef unsigned long i
    cdef int[:] max = np.empty(1, dtype=np.int32)
    max[0] = arr[0]

    for i in prange(size, nogil=True, schedule="guided"):
        if max[0] < arr[i]:
            max[0] = arr[i]
    return max[0]
                       
def pget(int[:] arr):
    return get_max_value(arr)

def sget(int[:] arr):
    cdef unsigned long size = arr.shape[0]
    cdef unsigned long i
    cdef int max = arr[0]

    for i in range(size):
        if max < arr[i]:
            max = arr[i]
    return max


