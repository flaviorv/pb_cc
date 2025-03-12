import multiprocessing
import math

def is_prime(n):
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    limit = int(math.sqrt(n)) + 1
    for i in range(5, limit, 2):
        if n % i == 0:
            return False
    return True

def count_primes_in_range(start, end):
    return sum(1 for n in range(start, end) if is_prime(n))

def parallel_prime_count(start, end):
    num_processes = multiprocessing.cpu_count()
    step = (end - start) // num_processes
    ranges = [(start + i * step, start + (i + 1) * step) for i in range(num_processes)]
    ranges[-1] = (ranges[-1][0], end)
    
    with multiprocessing.Pool(processes=num_processes) as pool:
        results = pool.starmap(count_primes_in_range, ranges)
    
    return sum(results)

if __name__ == "__main__":
    start, end = 1, 100_000
    total_primes = parallel_prime_count(start, end+1)
    print(f"Primes between {start} and {end}: {total_primes}")
