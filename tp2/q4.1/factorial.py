def factorial(num):
    if num < 0:
        return "Number must be 0 or greater", 1
    if num <= 1:
        return 1, 1
    f, i = factorial(num-1)
    f = f * num
    
    return f, i+1