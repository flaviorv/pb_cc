def fib(n):
    if n <= 1:
        return n, 1
    
    fib1, it1 = fib(n - 1)
    fib2, it2 = fib(n - 2)
    
    return fib1 + fib2, it1 + it2 + 1

def memofib(n, memo):
    if n in memo:
        return memo[n], 1
    if n <= 1:
        return n, 1
    
    fib1, it1 = memofib(n - 1, memo)
    fib2, it2 = memofib(n - 2, memo)
    
    memo[n] = fib1 + fib2
    return memo[n], it1 + it2 + 1


memofib(5, {})