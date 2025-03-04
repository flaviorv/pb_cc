
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