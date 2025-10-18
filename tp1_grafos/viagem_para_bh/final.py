import sys
import heapq
from collections import defaultdict


class Graph:
    def __init__(self, num_v):
        self.num_v = num_v
        self.origin = float("inf")
        self.adj = defaultdict(lambda: defaultdict(int))
        self.distances = {}
        self.unvisited = set()
        self.pi = {}
        self.queue = []

    def add_edge(self, u, v, w_u_v):
        if u < self.origin:
            self.origin = u
        if v < self.origin:
            self.origin = v

        if u not in self.adj.keys():
            self.distances[u] = float("inf")
            self.pi[u] = None
            self.unvisited.add(u)
        if v not in self.adj.keys():
            self.distances[v] = float("inf")
            self.pi[v] = None
            self.unvisited.add(v)

        self.adj[u][v] = w_u_v

    def run_dijkstra(self):
        self.distances[self.origin] = 0
        heapq.heappush(self.queue, (0, self.origin))
        self.distances[self.origin] = 0

        while self.queue:
            min_element = heapq.heappop(self.queue)
            if min_element[1] not in self.unvisited:
                continue
            current_vertex_coast, current_vertex = min_element
            self.unvisited.remove(current_vertex)

            if current_vertex == self.num_v:
                break

            neighbors_list = self.adj[current_vertex].keys()

            for neighbor in neighbors_list:
                if neighbor in self.unvisited:
                    neigh_cost = self.adj[current_vertex][neighbor]
                    neigh_total_coast = current_vertex_coast + neigh_cost
                    if neigh_total_coast < self.distances[neighbor]:
                        self.distances[neighbor] = neigh_total_coast
                        self.pi[neighbor] = current_vertex
                        heapq.heappush(self.queue, (neigh_total_coast, neighbor))

        return self.distances[self.num_v]


if __name__ == "__main__":
    data = sys.stdin.read().splitlines()
    iterator = iter(data)

    while True:
        try:
            info = next(iterator)
        except:
            break
        num_v, num_e = info.split(" ")
        graph_bus = Graph(int(num_v))
        graph_plane = Graph(int(num_v))
        for edge_idx in range(int(num_e)):
            city_a, city_b, plane, coast = next(iterator).split(" ")
            if int(plane):
                graph_plane.add_edge(int(city_a), int(city_b), int(coast))
            else:
                graph_bus.add_edge(int(city_a), int(city_b), int(coast))

        if len(graph_plane.adj.keys()) > 0:
            plane_coast = graph_plane.run_dijkstra()
        else:
            plane_coast = float("inf")
        if len(graph_bus.adj.keys()) > 0:
            bus_coast = graph_bus.run_dijkstra()
        else:
            bus_coast = float("inf")

        print(min(plane_coast, bus_coast))
