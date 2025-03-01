#How to paint chairs in a way that the chairs cannot be the same color as the previous one?
#Return the number of the possible ways
def count_ways_to_paint_chairs(chairs, colors):   
    possibilities = 1

    for chair in range(chairs):
        if chair == chairs-1 or chair == 1:
            colors -= 1
        possibilities *= colors

    return f"There is {possibilities} possibilities" if possibilities > 0 else "It is not possible to paint all the chairs"

chairs = 4
colors = 5
print(count_ways_to_paint_chairs(chairs, colors))
#This algorithm is O(n) time complexity