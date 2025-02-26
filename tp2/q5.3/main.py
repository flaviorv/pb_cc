import numpy as np
from time import time, sleep
import parallel_merge_sort
import sequential_merge_sort

_range = 5
length = 3_000_000
print(f"Creating a list with {length} elements...")
start = time()
array = np.random.randint(0, _range+1, size=length)
copy = np.array(array)
checklist = np.array(array)
print("List created in {round((time() - start), 3)} seconds")

print(f"Sorting sequentially...")
start = time()
sequential_merge_sort.sort(array)
print(f"Sort time: {round((time() - start), 3)} seconds")


print(f"Sorting in parallel mode...")
start = time()
parallel_merge_sort.sort(copy)
print(f"Sort time: {round((time() - start), 3)} seconds")



print("Sorting the checklist...")
start = time()
checklist.sort()
print(f"Sort time: {round((time() - start), 3)} seconds")

print(array)
print(copy)
print(checklist)

for i in range(len(checklist)):
    if checklist[i] != copy[i]:
        print(f"Sequentila sorting error: {copy[i]} is at index {i} but the {checklist[i]} was expected")

    if checklist[i] != array[i]:
        print(f"Parallel sorting error: {array[i]} is at index {i} but the {checklist[i]} was expected")
    
