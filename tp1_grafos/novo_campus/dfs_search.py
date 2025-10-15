from collections import defaultdict
import heapq


class Graph:
    def __init__(self, num_v):
        self.num_v = num_v
        self.adj = defaultdict(lambda: defaultdict(int))
        self.key = {}
        self.out_cut = {}
        for vertex in range(num_v):
            self.out_cut[vertex + 1] = True
        self.queue = []

    def add_edge(self, u, v, w_u_v):
        if u not in self.adj.keys():
            self.key[u] = float("inf")
        if v not in self.adj.keys():
            self.key[v] = float("inf")
        self.adj[u][v] = w_u_v
        self.adj[v][u] = w_u_v

    def run_mst(self, start_vertex):
        self.key[start_vertex] = 0
        self.queue.append((self.key[start_vertex], start_vertex))
        self.out_cut[start_vertex] = False
        while self.queue:
            min_element = min(self.queue)
            _, current_vertex = min_element
            self.queue.remove(min_element)
            self.out_cut[current_vertex] = False
            neighbors_list = self.adj[current_vertex].keys()
            for neighbor in neighbors_list:
                neigh_cost = self.adj[current_vertex][neighbor]
                if self.out_cut[neighbor] and self.key[neighbor] > neigh_cost:
                    self.key[neighbor] = self.adj[current_vertex][neighbor]
                    self.queue.append((neigh_cost, neighbor))

        total_cost = sum(self.key.values())
        if True in self.out_cut.values():
            total_cost = "impossivel"
        return total_cost
