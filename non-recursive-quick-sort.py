def quick_sort_non_recursive(arr):
    if len(arr) <= 1:
        return arr

    stack = [(0, len(arr) - 1)]

    while stack:
        start, end = stack.pop()

        if start >= end:
            continue

        pivot_index = partition(arr, start, end)
        stack.append((start, pivot_index - 1))
        stack.append((pivot_index + 1, end))

    return arr


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


data = [10, 7, 8, 9, 1, 5]
sorted_data = quick_sort_non_recursive(data)
print("Sorted array:", sorted_data)
