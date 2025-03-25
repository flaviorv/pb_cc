class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_edge(self, vertex1, vertex2, distance):
        if vertex1 not in self.adjacency_list:
            self.adjacency_list[vertex1] = []
        if vertex2 not in self.adjacency_list:
            self.adjacency_list[vertex2] = []
        self.adjacency_list[vertex1].append((vertex2, distance))
        self.adjacency_list[vertex2].append((vertex1, distance))

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
        print("Shortest path:", end=" ")
        for i in range(len(path)):
            if i != len(path)-1:
                print(path[i], end="=>")
            else:
                print(path[i], f"\nTotal distance: {path[i][1]}")


if __name__ == "__main__":
    graph = Graph()
    edges = [("A", "B", 1), ("A", "C", 4),
        ("B", "A", 1), ("B", "C", 2), ("B", "D", 5),
        ("C", "A", 4), ("C", "B", 2), ("C", "D", 1),
        ("D", "B", 5), ("D", "C", 1)]
    [graph.add_edge(ori, des, dis) for ori, des, dis in edges]
    graph.show()
    graph.min_path("A", "D")