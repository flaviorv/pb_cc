from random import randrange
import numpy as np
import time

def quick_select(array, low, high, k):
    if low == high:
        return array[low]
    
    pivot_index = _sorting_pivot(array, low, high)

    if k == pivot_index:
        return array[k]
    
    elif k < pivot_index:
        return quick_select(array, low, pivot_index -1 ,k)
    
    else:
        return quick_select(array, pivot_index +1, high, k)
    

def _sorting_pivot(array, low, high):
    pivot_index = (low+high)//2
    array[high], array[pivot_index] = array[pivot_index], array[high]
    pivot = array[high]
    i = low -1
    for j in range(low, high):
        if array[j] <= pivot:
            i+=1
            array[i], array[j] = array[j], array[i]

    array[i+1], array[high] = array[high], array[i+1]
    return i + 1



def main():
    length = 10_000
    
    random1 = np.random.randint(1, 1_001, size=length)
    random2 = np.random.randint(1, 1_001, size=length)
    random3 = np.random.randint(1, 1_001, size=length)
    random4 = np.random.randint(1, 1_001, size=length)
    random5 = np.random.randint(1, 1_001, size=length)
    random6 = np.random.randint(1, 1_001, size=length)
    random7 = np.random.randint(1, 1_001, size=length)
    random8 = np.random.randint(1, 1_001, size=length)
    ordered = np.arange(1, length+1)
    inverse = np.arange(length, 0, -1)
    
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


    ks = [
        randrange(1, length+1),
        randrange(1, length+1),
        randrange((length//2)),
        length,
        1,
    ]

    for name, array in lists.items():
        
        for k in ks:
            
            start = time.time()
            result = quick_select(array, 0, len(array) -1, k -1)
            end = time.time()
            sec = round(end-start, 3)

            abbreviation = ""
            _k = str(k)
            match(_k[len(_k)-1]):
                case "1":
                    abbreviation = "st"
                case "2":
                    abbreviation = "nd"
                case "3":
                    abbreviation = "rd"
                case _:
                    abbreviation = "th"

            print(f"\33[1m\33[32m{_k+abbreviation:>10} smaller: \33[0m{result:<10} \33[31mArray: \33[0m{name:<10} \33[30mTime: \33[0m{sec}s")

if __name__ == "__main__":
    main()