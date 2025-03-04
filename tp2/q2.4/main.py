import numpy as np
from random import randrange

def quick_select(array, low, high, k):
    pivot_index = _sorting_pivot(array, low, high)

    if k == pivot_index:
        return array[k] 
    elif k < pivot_index:
        return quick_select(array, low, pivot_index -1 ,k)
    else:
        return quick_select(array, pivot_index +1, high, k) 
            
    
def _sorting_pivot(array, low, high):
    pivot_index = randrange(low, high+1)
    array[high], array[pivot_index] = array[pivot_index], array[high]

    i = low -1
    for j in range(low, high):
        if array[j] <= array[high]:
            i+=1
            array[i], array[j] = array[j], array[i]
   
    array[i+1], array[high] = array[high], array[i+1]   
    return i+1


def median():
    
    random1 = np.random.randint(1, 1_001, size=1)
    random2 = np.random.randint(1, 1_001, size=2)
    random3 = np.random.randint(1, 1_001, size=3)
    random4 = np.random.randint(1, 1_001, size=4)
    random5 = np.random.randint(1, 1_001, size=5)
    random6 = np.random.randint(1, 1_001, size=6)
    random7 = np.random.randint(1, 1_001, size=10_000)
    random8 = np.random.randint(1, 1_001, size=10_001)
    ordered = np.arange(1, 11)
    inverse = np.arange(12, 0, -1)

    lists = {
        "random1": random1, 
        "random2": random2,  
        "random3": random3,
        "random4": random4,
        "random5": random5,
        "random6": random6,
        "random7": random7,
        "random8": random8,
        "ordered": ordered, 
        "inverse": inverse, 
    }

        
    for name, array in lists.items():   
        print("-----------------------------------------------")
        print(f"  Before: {array}")

        median = quick_select(array, 0, len(array) -1, len(array)//2)
        if len(array) % 2 == 0:
            second = quick_select(array, 0, len(array) -1, len(array)//2-1)
            median = (median + second) /2
        
        print(f"  After: {array}")
        print(f"\33[1m\33[32m  Median: \33[0m{median:<10} \33[31mArray: \33[0m{name:<10} \33[0m")

if __name__ == "__main__":
    median()