from concurrent_and_linear_vector_sum.concurrent_vector_sum import CustomThread
from concurrent_and_linear_vector_sum.linear_vector_sum import linear_sum
from random import randrange
import time
import numpy as np

# large_array = np.arange(200_000_000, dtype=np.int32)
_range = 100_000_000
vector = [i for i in range(_range)]
vector2 = [i for i in range(20)]

chunk = _range//4



t1 = CustomThread(target=linear_sum, args=(vector,0,chunk))
t2 = CustomThread(target=linear_sum, args=(vector,chunk,chunk*2))
t3 = CustomThread(target=linear_sum, args=(vector,chunk*2,chunk*3))
t4 = CustomThread(target=linear_sum, args=(vector,chunk*3,chunk*4))

start = time.time()


#sequential------
print("Starting sequential sum...")
print(linear_sum(vector))
execution_time = time.time() - start
print(f"Sequential sum took {execution_time} seconds")

## with concurrent threads----
print("Starting with concurrent sum...")
t1.start()
t2.start()
t3.start()
t4.start()
print("Another things may occur before result")
r1 = t1.join()
r2 = t2.join()
r3 = t3.join()
r4 = t4.join()
print(r1+r2+r3+r4)
execution_time = time.time() - start
print(f"Concurrent sum took {execution_time} seconds")

# With concurrency:
# The execution time is  in majority times greater than sequential, because there is no idle time.
# However, the screen is free to execute other operations while waiting for result.
# Just one thread would be enough. In this case, four was be created with no reason.
# In other cases as requests to network, the result may take less time to return the result.
# While wait from the response, its call the other requests, making it return the result faster.
# With sequential:
# In this case is faster.
# The screen is freeze while we wating for the result.