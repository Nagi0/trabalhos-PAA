import sys
from operator import itemgetter


class Graph:
    def __init__(self):
        self.graph = {}
        self.graph_inv = {}
        self.colors = {}
        self.colors_inv = {}
        self.pi = {}
        self.discovery_time = {}
        self.component_discovery_time = {}
        self.terminate_time = {}
        self.timer = 1
        self.scc_count = 0
        self.safe_double_edges = set()

    def add_edge(self, u, v, directions):
        if directions == 1:
            self._add_single_direction(u, v)
            self._add_inv_single_direction(v, u)
        else:
            self._add_double_direction(u, v)
            self._add_inv_double_direction(v, u)

    def remove_edge(self, u, v, directions):
        if directions == 1:
            self._remove_single_direction(u, v)
            self._remove_inv_single_direction(v, u)
        else:
            self._remove_double_direction(u, v)
            self._remove_inv_double_direction(v, u)

        return self

    def depth_first_search(self, start_vertex: int):
        has_bridge = False
        queue = [start_vertex]
        self.colors[start_vertex] = "gray"
        self.pi[start_vertex] = None

        while queue:
            current_vertex = queue[-1]
            neighbors_list = self.graph[current_vertex]
            vertex_done = True
            if current_vertex not in self.discovery_time:
                self.discovery_time[current_vertex] = self.timer
                self.component_discovery_time[current_vertex] = self.discovery_time[current_vertex]
                self.timer += 1
            for neighbor in neighbors_list:
                if self.colors[neighbor] == "white":
                    self.colors[neighbor] = "gray"
                    self.pi[neighbor] = current_vertex
                    queue.append(neighbor)
                    vertex_done = False
                    break
                else:
                    if neighbor != self.pi[current_vertex] and neighbor in self.discovery_time:
                        self.component_discovery_time[current_vertex] = min(
                            self.component_discovery_time[current_vertex], self.discovery_time[neighbor]
                        )
            if vertex_done:
                self.terminate_time[current_vertex] = self.timer
                self.timer += 1
                self.colors[current_vertex] = "black"
                queue.pop()
                if self.pi[current_vertex] is not None:
                    parent = self.pi[current_vertex]
                    self.component_discovery_time[parent] = min(
                        self.component_discovery_time[parent], self.component_discovery_time[current_vertex]
                    )
                    edge = frozenset((current_vertex, parent))

                    if (
                        self.component_discovery_time[current_vertex] > self.discovery_time[parent]
                        and edge not in self.safe_double_edges
                    ):
                        has_bridge = True

        return has_bridge

    def reversed_depth_first_search(self, start_vertex):
        queue = [start_vertex]
        self.colors_inv[start_vertex] = "gray"

        while queue:
            current_vertex = queue[-1]
            sorted_neighbors = sorted(self.graph_inv[current_vertex])
            vertex_done = True
            for neighbor in sorted_neighbors:
                if self.colors_inv[neighbor] == "white":
                    self.colors_inv[neighbor] = "gray"
                    queue.append(neighbor)
                    vertex_done = False
                    break
            if vertex_done:
                self.colors_inv[current_vertex] = "black"
                queue.pop()

        self.scc_count += 1

    def reset_search_states(self):
        self.timer = 1
        self.scc_count = 0
        self.discovery_time.clear()
        self.terminate_time.clear()
        for vertex, neighboors in self.graph.items():
            self.colors[vertex] = "white"
            self.colors_inv[vertex] = "white"
            for neigh in neighboors:
                self.colors[neigh] = "white"
                self.colors_inv[neigh] = "white"

    def change2not_directed(self):
        for vertex, neighboors in self.graph.items():
            for neigh in neighboors:
                if vertex not in self.graph[neigh]:
                    self.graph[neigh].add(vertex)

    def _add_single_direction(self, u, v):
        if u in self.graph:
            self.graph[u].add(v)
        else:
            self.graph[u] = {v}
            self.colors[u] = "white"
        if v not in self.graph:
            self.graph[v] = set()
            self.colors[v] = "white"

    def _add_double_direction(self, u, v):
        if u in self.graph:
            self.graph[u].add(v)
        if v in self.graph:
            self.graph[v].add(u)
        if u not in self.graph:
            self.graph[u] = {v}
            self.colors[u] = "white"
        if v not in self.graph:
            self.graph[v] = {u}
            self.colors[v] = "white"

    def _add_inv_single_direction(self, u, v):
        if u in self.graph_inv:
            self.graph_inv[u].add(v)
        else:
            self.graph_inv[u] = {v}
            self.colors_inv[u] = "white"
        if v not in self.graph_inv:
            self.graph_inv[v] = set()
            self.colors_inv[v] = "white"

    def _add_inv_double_direction(self, u, v):
        if u in self.graph_inv:
            self.graph_inv[u].add(v)
        if v in self.graph_inv:
            self.graph_inv[v].add(u)
        if u not in self.graph_inv:
            self.graph_inv[u] = {v}
            self.colors_inv[u] = "white"
        if v not in self.graph_inv:
            self.graph_inv[v] = {u}
            self.colors_inv[v] = "white"

    def _remove_single_direction(self, u, v):
        self.graph[u].remove(v)

    def _remove_double_direction(self, u, v):
        self.graph[u].remove(v)
        if u != v:
            self.graph[v].remove(u)

    def _remove_inv_single_direction(self, u, v):
        self.graph_inv[u].remove(v)

    def _remove_inv_double_direction(self, u, v):
        self.graph_inv[u].remove(v)
        if u != v:
            self.graph_inv[v].remove(u)


def check_graph_scc(graph: Graph, remove_edge: tuple) -> str:
    graph.remove_edge(remove_edge[0], remove_edge[1], remove_edge[2])
    if check_single_scc(graph):
        return "-"
    else:
        graph.reset_search_states()
        graph.change2not_directed()
        if check_impossible(graph):
            return "*"
        else:
            graph.reset_search_states()
            return "2" if graph.depth_first_search(1) else "1"


def check_single_scc(graph: Graph) -> bool:
    for vertex in graph.graph:
        if graph.colors[vertex] == "white":
            graph.depth_first_search(vertex)
    terminate_time = sorted(graph.terminate_time.items(), key=itemgetter(1), reverse=True)
    for vertex, _ in terminate_time:
        if graph.colors_inv[vertex] == "white":
            graph.reversed_depth_first_search(vertex)
            if graph.scc_count > 1:
                return False

    return True


def check_impossible(graph: Graph) -> bool:
    for idx, vertex in enumerate(graph.graph):
        if graph.colors[vertex] == "white":
            if idx == 0:
                graph.depth_first_search(vertex)
            else:
                return True

    return False


if __name__ == "__main__":
    data = sys.stdin.read().splitlines()
    iterator = iter(data)

    while True:
        try:
            info = next(iterator)
        except:
            break
        num_v, num_e = info.split(" ")
        graph = Graph()
        remove_edge = ()
        for edge_idx in range(int(num_e)):
            cross_a, cross_b, directions = list(map(int, next(iterator).split(" ")))
            if edge_idx == 0:
                remove_edge = (cross_a, cross_b, directions)
            graph.add_edge(cross_a, cross_b, directions)
            if directions == 2:
                graph.safe_double_edges.add(frozenset((cross_a, cross_b)))
        sys.stdout.write(f"{check_graph_scc(graph, remove_edge)}\n")
