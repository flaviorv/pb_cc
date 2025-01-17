def linear_sum(vector, start=0, final=None):
    if final == None:
        final = len(vector)
    amount = 0
    for i in range(start, final, +1):
        amount += vector[i]
    return amount