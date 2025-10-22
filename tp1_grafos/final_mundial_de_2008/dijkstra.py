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
