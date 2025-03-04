import numpy as np

cdef merge(long long[:] arr, unsigned long first, unsigned long mid, unsigned long last):
    cdef unsigned long left_size = mid - first + 1  
    cdef unsigned long right_size = last - mid    

    cdef long long[:] left_arr = np.copy(np.asarray(arr[first:first + left_size])) 
    cdef long long[:] right_arr = np.copy(np.asarray(arr[mid + 1:mid + 1 + right_size])) 

    cdef unsigned long left_index = 0
    cdef unsigned long right_index = 0
    cdef unsigned long index = first

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

cdef merge_sort(long long[:] arr):
    
    cdef unsigned long arr_size = arr.shape[0]
    cdef unsigned long subs_size = 1
    cdef unsigned long middle_index
    cdef unsigned long last_index
    cdef unsigned long first_index

    while subs_size < arr_size:
        first_index = 0

        while first_index < arr_size - 1:
            middle_index = first_index + subs_size - 1
            if middle_index > arr_size - 1:
                middle_index = arr_size -1

            last_index = 2 * subs_size + first_index - 1
            if last_index > arr_size -1:
                last_index = arr_size -1

            merge(arr, first_index, middle_index, last_index)

            first_index += 2 * subs_size

        subs_size *= 2

def sort(long long[:] arr):
    merge_sort(arr)