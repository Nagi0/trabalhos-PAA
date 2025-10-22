import sys
import heapq
from collections import defaultdict


class Graph:
    def __init__(self, num_v):
        self.num_v = num_v
        self.adj = defaultdict(lambda: defaultdict(int))
        self.distances = {}
        self.unvisited = set()
        self.pi = {}
        self.queue = []

    def add_edge(self, u, v, w_u_v):
        if u not in self.adj:
            self.distances[u] = float("inf")
            self.unvisited.add(u)
        if v not in self.adj:
            self.distances[v] = float("inf")
            self.unvisited.add(v)

        self.adj[u][v] = w_u_v

    def reset_dijkstra(self):
        self.pi.clear()
        self.queue.clear()

    def run_dijkstra(self, origin, destiny, t_allowed):
        unvisited = self.unvisited.copy()
        distances = self.distances.copy()
        if origin == destiny:
            return 0
        elif t_allowed == 0:
            if destiny in self.adj.get(origin, []):
                direct_connection = self.adj[origin][destiny]
            else:
                direct_connection = -1

            return direct_connection

        distances[origin] = 0
        heapq.heappush(self.queue, (0, origin))
        distances[origin] = 0

        while self.queue:
            min_element = heapq.heappop(self.queue)
            if min_element[1] not in unvisited:
                continue
            current_vertex_coast, current_vertex = min_element
            unvisited.remove(current_vertex)

            if current_vertex == destiny:
                break

            neighbors_list = self.adj[current_vertex].keys()

            for neighbor in neighbors_list:
                if neighbor in unvisited and (neighbor <= t_allowed or neighbor == destiny):
                    neigh_cost = self.adj[current_vertex][neighbor]
                    neigh_total_coast = current_vertex_coast + neigh_cost
                    if neigh_total_coast < distances[neighbor]:
                        distances[neighbor] = neigh_total_coast
                        self.pi[neighbor] = current_vertex
                        heapq.heappush(self.queue, (neigh_total_coast, neighbor))

        if distances[destiny] == float("inf"):
            return -1
        else:
            return distances[destiny]


if __name__ == "__main__":
    data = sys.stdin.read().splitlines()
    iterator = iter(data)
    instance_counter = 1

    while True:
        try:
            info = next(iterator)
            sys.stdout.write(f"Instancia {instance_counter}\n")
        except:
            break

        num_v, num_e = info.split(" ")
        graph = Graph(int(num_v))
        for edge_idx in range(int(num_e)):
            field_info = next(iterator)
            vertex_u, vertex_v, cost = list(map(int, field_info.split(" ")))
            if vertex_v not in graph.adj.get(vertex_u, []):
                graph.add_edge(vertex_u, vertex_v, cost)
            else:
                current_coast = graph.adj.get(vertex_u, {}).get(vertex_v, float("inf"))
                if cost < current_coast:
                    graph.add_edge(vertex_u, vertex_v, cost)

        eval_cases = int(next(iterator).strip())
        for eval_c in range(eval_cases):
            origin, destiny, t = next(iterator).split(" ")
            result = graph.run_dijkstra(int(origin), int(destiny), int(t))
            graph.reset_dijkstra()
            sys.stdout.write(f"{result}\n")

        sys.stdout.write("\n")
        instance_counter += 1
