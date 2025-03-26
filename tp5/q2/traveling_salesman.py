import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0]-city2[0])**2 + (city1[1]-city2[1])**2)

def traveling_salesman(cities):
    path = []
    city = list(cities.keys())[0]
    while cities:
        min_distance = float('inf')
        path.append(city)
        chosen_neighbor = None
        for neighbor in cities:
            if neighbor != city:
                distance = calculate_distance(cities[city], cities[neighbor])
                if distance < min_distance:
                    min_distance = distance
                    chosen_neighbor = neighbor
        cities.pop(city)
        city = chosen_neighbor
    path.append(path[0])
    return path

if __name__ == "__main__":
    cities = {"A": (0, 0), "B": (1, 5), "C": (5, 2), "D": (6, 6), "E": (8, 3)}
    print("Traveling Salesman Problem")
    print("Cities coordinates:", cities)
    print("Path:", end=" ")
    path = traveling_salesman(cities)
    [print(path[i], end=" -> ") if i != len(path)-1 else print(path[i]) for i in range(len(path)) ]

