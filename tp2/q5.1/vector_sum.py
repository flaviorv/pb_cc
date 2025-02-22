import parallel_sum, time, chart
import numpy as np
from save_file import save

def comparing_methods():

    vector_len = 10_000
    max_range = 100_001
    content = {}

    for _ in range(5):
        
        content[vector_len] = {}
        
        print(f"-----x-----x-----x-----x LEN OF ARRAY = {vector_len} -----x-----x-----x-----x")

        start = round(time.time(),3)
        numbers = np.random.randint(1, max_range, size=vector_len)
        end = round(time.time(), 3)
        sec = end-start
        name = "numpy-py"
        print(f"{name} took {sec} seconds")
        content[vector_len][name] = sec

        start = round(time.time(),3)
        result = sum(numbers)
        end = round(time.time(), 3)
        sec = end-start
        name = "sum-sequential"
        print(f"{name} took {sec} seconds and the result is {result}")
        content[vector_len][name] = sec
        
        result = parallel_sum.sum(vector_len, max_range)
        for key, val in result.items():
            content[vector_len][key] = val
        
        save(content)
        vector_len *= 10

if __name__ == "__main__":
    comparing_methods()
    chart.generate_chart()