class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_edge(self, vertex1, vertex2, distance):
        if vertex1 not in self.adjacency_list:
            self.adjacency_list[vertex1] = []
        self.adjacency_list[vertex1].append((vertex2, distance))

    def dijkstra(self, origin, destination):
        unvisited = list(self.adjacency_list.keys())
        distances = {vertex: float("inf") for vertex in self.adjacency_list}
        distances[origin] = 0
        predecessors = {}
        while unvisited:
            current = min(unvisited, key=lambda vertex: distances[vertex])
            if distances[current] == float("inf"):
                break
            for neighbor in self.adjacency_list[current]:
                vertex, distance = neighbor[0], neighbor[1]
                new_distance = distances[current] + distance
                if new_distance < distances[vertex]:
                    distances[vertex] = new_distance
                    predecessors[vertex] = current
            unvisited.remove(current)
        path = []
        current = destination
        while current in predecessors.keys():
            path.insert(0, (current, distances[current]))
            current = predecessors[current]
        path.insert(0, (origin, 0))
        return path
    
    def show(self):
        for vertex in self.adjacency_list:
            print(vertex, self.adjacency_list[vertex])

    def min_path(self, origin, destination):
        path = self.dijkstra(origin, destination)
        for i in range(len(path)):
            if i != len(path)-1:
                print(path[i], end="=>")
            else:
                print(path[i], f"\nTotal distance: {path[i][1]}")

    def prim(self, origin):
        vertices = {}
        total_weight = 0
        for vertex in self.adjacency_list:
            vertices[vertex] = {}
            vertices[vertex]["selected"] = False
            vertices[vertex]["weight"] = float('inf')
            vertices[vertex]["parent"] = None

        vertices[origin]["weight"] = 0  
        for _ in range(len(self.adjacency_list)):
            print(vertices[origin]["selected"])
            minimum = float('inf')
            _selected = -1
            for vertex in self.adjacency_list:
                if not vertices[vertex]["selected"] and vertices[vertex]["weight"] < minimum:
                    minimum = vertices[vertex]["weight"]
                    _selected = vertex
            
            total_weight += minimum
            vertices[_selected]["selected"] = True

            for vertex, weight in self.adjacency_list[_selected]:
                if 0 < weight < vertices[vertex]["weight"] and not vertices[vertex]["selected"]:
                    vertices[vertex]["weight"] = weight
                    vertices[vertex]["parent"] = _selected

        for key in vertices:
            if key != origin:
                print(vertices[key]["parent"], "-", key, vertices[key]["weight"])
        print(vertices)
        

if __name__ == "__main__":
    print("Graph 1")
    g1 = Graph()
    e1 = [("A", "B", 1), ("A", "C", 4),
        ("B", "A", 1), ("B", "C", 2), ("B", "D", 5),
        ("C", "A", 4), ("C", "B", 2), ("C", "D", 1),
        ("D", "B", 5), ("D", "C", 1)]
    [g1.add_edge(ori, des, dis) for ori, des, dis in e1]
    g1.show()
    print("\nShortest Path - Dijkstra algorithm")
    g1.min_path("A", "D")
    
    print("\nGraph 2")
    g2 = Graph()
    e2 = [("A", "B", 2), ("A", "C", 3),
        ("B", "A", 2), ("B", "D", 4), ("B", "C", 1), 
        ("C", "A", 3), ("C", "D", 5) ,("C", "B", 1),
        ("D", "B", 4), ("D", "C", 5)]
    [g2.add_edge(ori, des, dis) for ori, des, dis in e2]
    g2.show()
    print("\nMinimum Spanning Tree - Prim algorithm")
    g2.prim("A")