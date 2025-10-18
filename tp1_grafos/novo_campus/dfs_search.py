from collections import defaultdict
import heapq


class Graph:
    def __init__(self, num_v):
        self.num_v = num_v
        self.adj = defaultdict(lambda: defaultdict(int))
        self.key = {}
        self.out_cut = {}
        self.queue = []

    def add_edge(self, u, v, w_u_v):
        if u not in self.adj.keys():
            self.key[u] = float("inf")
        if v not in self.adj.keys():
            self.key[v] = float("inf")
        self.adj[u][v] = w_u_v
        self.adj[v][u] = w_u_v
        self.out_cut[u] = True
        self.out_cut[v] = True

    def run_mst(self, start_vertex):
        total_cost = 0
        num_visited_v = 0

        self.key[start_vertex] = 0
        heapq.heappush(self.queue, (0, start_vertex))
        self.key[start_vertex] = 0
        self.out_cut[start_vertex] = False

        while self.queue:
            min_element = heapq.heappop(self.queue)
            current_vertex_coast, current_vertex = min_element
            total_cost += current_vertex_coast
            num_visited_v += 1

            self.out_cut[current_vertex] = False
            neighbors_list = self.adj[current_vertex].keys()

            for neighbor in neighbors_list:
                neigh_cost = self.adj[current_vertex][neighbor]
                if self.out_cut[neighbor] and self.key[neighbor] > neigh_cost:
                    self.key[neighbor] = self.adj[current_vertex][neighbor]
                    heapq.heappush(self.queue, (neigh_cost, neighbor))

        if True in self.out_cut.values() or num_visited_v < self.num_v:
            total_cost = "impossivel"
        return total_cost
