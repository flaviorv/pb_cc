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

    def _dfs(self, start, end, visited, path, _start=None):
        if visited is None:
            _start = start
            visited = set()
        print(start, end=" ")
        if end == start:
            print(f"- A path between {_start} and {end} exists.", end="")
            path = True
            return path
        visited.add(start)
        for neighbor in self.adjacency_list[start]:
            if neighbor not in visited:
                return self._dfs(neighbor, end, visited, path, _start)

    def dfs(self, start, end=None, visited=None):
        print("DFS:", end=" ")
        path = self._dfs(start, end, visited, path=False)
        print(f"- No path between {start} and {end}") if not path and end != None else print()

    def bfs(self, start, end=None):
        print("BFS:", end=" ")
        visited = set()
        queue = [start]
        while queue:
            vertex = queue.pop(0)
            if vertex not in visited:
                print(vertex, end=" ")
                if vertex == end:
                    print(f"- A path between {start} and {end} exists.")
                    return
                visited.add(vertex)
                queue.extend(self.adjacency_list[vertex])
        if end != None:
            print(f"- No path between {start} and {end}")
            return
        print()

if __name__ == "__main__":
    edges = [("A", "B"), ("A", "C"), ("B", "D"), ("C", "D"), ("D", "E")]
    graph = NonDirectionalGraph()
    for edge in edges:
        graph.add_edge(edge[0], edge[1])
    for key in graph.adjacency_list:
        print(key, graph.adjacency_list[key])
    graph.dfs("A")
    graph.bfs("A")
    graph.dfs("A", "D")
    graph.bfs("A", "D")
    graph.add_vertex("F")
    graph.dfs("A", "F")
    graph.bfs("A", "F")
