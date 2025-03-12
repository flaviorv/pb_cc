from cython.parallel import prange, threadid
import numpy as np

cdef void merge(long long[:] arr, long long[:] left_arr, long long[:] right_arr, unsigned long first, unsigned long mid, unsigned long last) noexcept nogil:
    cdef unsigned long left_size = 0
    cdef unsigned long right_size = 0
    cdef unsigned long left_index = 0
    cdef unsigned long right_index = 0
    cdef unsigned long index = first
    
    with gil:
        for i in range(first, mid+1):
            left_arr[left_index] = arr[i]
            left_index += 1 
        
        for i in range(mid + 1, last +1):
            right_arr[right_index] = arr[i]
            right_index += 1

        left_size = left_index
        right_size = right_index
        left_index = 0
        right_index = 0

        while left_index < left_size and right_index < right_size:
            if left_arr[left_index] <= right_arr[right_index]:
            
                arr[index] = left_arr[left_index]
                left_index += 1
            else:
                arr[index] = right_arr[right_index]
                right_index += 1
            index += 1

        while left_index < left_size:   
            arr[index] = left_arr[left_index]
            left_index += 1
            index += 1

        while right_index < right_size:
            arr[index] = right_arr[right_index]
            right_index += 1
            index += 1
  

cdef void merge_sort(long long[:] arr, unsigned long low, unsigned long high, long long[:] left_arr, long long[:] right_arr) noexcept nogil:
    
    cdef unsigned long subs_size = 1
    cdef unsigned long middle_index
    cdef unsigned long last_index
    cdef unsigned long first_index
    
    while subs_size < (high - low +1):
        first_index = low

        while first_index < high:
            middle_index = first_index + subs_size - 1
            if middle_index > high:
                middle_index = high

            last_index = 2 * subs_size + first_index - 1
            if last_index > high:
                last_index = high
         
            merge(arr, left_arr, right_arr, first_index, middle_index, last_index)

            first_index += 2 * subs_size

        subs_size *= 2


cdef divide(long long[:] arr):
    cdef unsigned int threads = 2
    cdef unsigned int i
    cdef unsigned long size = arr.shape[0]
    cdef unsigned long chunk = size // threads
    cdef unsigned long low, high
    cdef long long[:] left_arr = np.empty(size, dtype=np.longlong) 
    cdef long long[:] right_arr = np.empty(size, dtype=np.longlong)

    with nogil:
        for i in prange(threads, num_threads=threads, schedule="static"):
            low = i*chunk
            high = low + chunk -1
            if threads-1 == i:
                high = size -1
            
            merge_sort(arr, low, high, left_arr, right_arr)

    merge(arr, left_arr, right_arr, 0, chunk-1, size-1)


def sort(long long[:] arr):
    divide(arr)