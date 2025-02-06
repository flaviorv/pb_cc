from random import randrange, shuffle
from rw_files import save
from samples_average import generate_average_time
import numpy as np
import time, copy
from chart import generate_chart
  
def quick_sort (arr, pivot_type):
    if len(arr) <= 1:
        return arr
    
    stack = [(0, len(arr)-1)]

    while stack:
        start, end = stack.pop()
        if start >= end:
            continue
        
        pivot_index = __choosing_pivot(start, end, pivot_type)
        pivot_index = __sorting_pivot(arr, start, end, pivot_index)

        stack.append((start, pivot_index-1))
        stack.append((pivot_index+1, end))

    return arr


def __choosing_pivot(start, end, pivot_type):
    match(pivot_type):
        case "start":
            return start
        case "middle":
            index = (start + end) // 2
            return index
        case "end":
            return end
        case "random":
            return randrange(start, end+1)

    
def __sorting_pivot(arr, start, end, pivot_index):
    if pivot_index != end:
        arr[pivot_index], arr[end] = arr[end], arr[pivot_index]
        pivot_index = end
    pivot = arr[pivot_index]
    
    i = start-1

    for j in range(start, end):
        if arr[j] <= pivot:
            i+=1
            arr[i], arr[j] = arr[j], arr[i]
    
    new_pivot_index = i+1
    arr[new_pivot_index], arr[pivot_index] = arr[pivot_index], arr[new_pivot_index]
    return new_pivot_index

def get_time(func, arr, pivot_type):
    start = time.time()
    func(arr, pivot_type)
    end = time.time()
    sec = round(end-start, 4)
    return sec


def main():
    pivot_types = ["start", "middle", "end", "random"]
    shuffle(pivot_types)

    data = []
    samples = 3

    num_len = 5_000
    
    unordered = np.random.randint(1, 1_001, num_len)
    ordered = np.arange(1, num_len+1)
    inverse = np.arange(num_len, 0, -1)

    arr_types = {"unordered": unordered, "ordered": ordered, "inverse": inverse}
    
    for _ in range(samples):
        for arr_type, arr in arr_types.items():
            for pivot_type in pivot_types:
                numbers = copy.deepcopy(arr)
                sec = get_time(quick_sort, numbers, pivot_type)
                result = {"arr_type": arr_type, "pivot_type": pivot_type, "sec": sec}
                data.append(result)
                
                if result["sec"] >= 1.5:
                    print(f"\033[1m \033[31m {result}")
                else:
                    print(f"\033[1m \033[32m {result}")

    

    save(data, "quick_sort_times.json")
    generate_average_time(samples)
    

if __name__ == "__main__":
    main()
    generate_chart()