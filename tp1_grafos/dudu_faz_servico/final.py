import sys


class Graph:
    def __init__(self):
        self.graph = {}
        self.colors = {}
        self.result = "NAO"

    def __repr__(self):
        result = ""
        for key in self.graph.keys():
            result += f"Vertex: '{key}'\n"
            for v in sorted(self.graph[key]):
                result += f"edge {key} --> {v} \n"
        return result

    def add_edge(self, u, v):
        if u in self.graph:
            self.graph[u].add(v)
        else:
            self.graph[u] = {v}
            self.colors[u] = "white"
        if v not in self.graph:
            self.graph[v] = set()
            self.colors[v] = "white"

    def depth_first_search(self, start_vertex):
        visited = []
        queue = [start_vertex]
        self.colors[start_vertex] = "gray"

        while queue:
            current_vertex = queue[-1]
            sorted_neighbors = sorted(self.graph[current_vertex])
            vertex_done = True
            for neighbor in sorted_neighbors:
                if self.colors[neighbor] == "gray":
                    self.result = "SIM"
                    return visited, self.result
                elif self.colors[neighbor] == "white":
                    self.colors[neighbor] = "gray"
                    queue.append(neighbor)
                    vertex_done = False
                    break
            if vertex_done:
                self.colors[current_vertex] = "black"
                visited.append(queue.pop())

        return visited, self.result


def check_cycles_full_graph(graph: Graph):
    cycle_exists = "NAO"
    for v in graph.graph:
        if graph.colors[v] == "white":
            _, result = graph.depth_first_search(v)
            if result == "SIM":
                cycle_exists = "SIM"
                break
    print(cycle_exists)


if __name__ == "__main__":
    data = sys.stdin.read().strip().split()
    iterator = iter(data)
    num_problems = int(next(iterator))

    for problem_idx in range(num_problems):
        num_v = int(next(iterator))
        num_e = int(next(iterator))
        graph = Graph()
        for edge_idx in range(num_e):
            vertex_u = int(next(iterator))
            vertex_v = int(next(iterator))
            graph.add_edge(vertex_u, vertex_v)

        check_cycles_full_graph(graph)
