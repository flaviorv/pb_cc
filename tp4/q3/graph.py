class NonDirectionalGraph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, vertex1, vertex2):
        if vertex1 not in self.adjacency_list:
            self.add_vertex(vertex1)
        if vertex2 not in self.adjacency_list:
            self.add_vertex(vertex2)
        self.adjacency_list[vertex1].append(vertex2)
        self.adjacency_list[vertex2].append(vertex1)

    def _dfs(self, vertex, visited=None):
        if visited is None:
            visited = set()
        print(vertex, end=" ")
        visited.add(vertex)
        for neighbor in self.adjacency_list[vertex]:
            if neighbor not in visited:
                self._dfs(neighbor, visited)

    def dfs(self, vertex, visited=None):
        self._dfs(vertex, visited)
        print()

if __name__ == "__main__":
    edges = [("A", "B"), ("A", "C"), ("B", "D"), ("C", "D"), ("D", "E")]
    graph = NonDirectionalGraph()
    for edge in edges:
        graph.add_edge(edge[0], edge[1])
    # for key in graph.adjacency_list:
        # print(key, graph.adjacency_list[key])
    graph.dfs("A")
