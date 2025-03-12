import multiprocessing
import math
from time import time

def is_prime(n):
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    end = int(math.sqrt(n)) + 1
    for i in range(5, end, 2):
        if n % i == 0:
            return False
    return True

def count_primes(start, end):
    return sum(1 for n in range(start, end) if is_prime(n))

def parallel_count_primes(start, end):
    processes = multiprocessing.cpu_count()
    chunk = (end - start) // processes
    ranges = [(start + i * chunk, start + (i + 1) * chunk) for i in range(processes)]
    ranges[-1] = (ranges[-1][0], end)

    with multiprocessing.Pool(processes=processes) as pool:
        partial_sum = pool.starmap(count_primes, ranges)

    return sum(partial_sum)

if __name__ == "__main__":
    start, end = 1, 100_000

    time_start = time()
    print(f"Primes between {start} and {end}:")
    total_primes = parallel_count_primes(start, end+1)

    print(f"Parallel Time: {round((time()-time_start),3)} seconds - Primes: {total_primes}")
    time_start = time()
    total_primes = count_primes(start, end)
    print(f"Sequential Time: {round((time()-time_start),3)} seconds - Primes: {total_primes}")
