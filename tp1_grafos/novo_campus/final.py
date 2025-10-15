import sys
from collections import defaultdict


class MinHeap:
    def __init__(self):
        self.elements = []

    def pop(self):
        if len(self.elements) == 0:
            return [None, None]

        if len(self.elements) == 1:
            return self.elements.pop()

        root_value = self.elements[0]
        self.elements[0] = self.elements.pop()
        self.bubble_down(0)

        return root_value

    def bubble_down(self, index):
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2
        min_index = index

        if left_child_index < len(self.elements) and self.elements[left_child_index][0] < self.elements[min_index][0]:
            min_index = left_child_index

        if (
            right_child_index < len(self.elements)
            and self.elements[right_child_index][0] < self.elements[min_index][0]
        ):
            min_index = right_child_index

        if min_index != index:
            self.elements[index], self.elements[min_index] = (
                self.elements[min_index],
                self.elements[index],
            )
            self.bubble_down(min_index)

    def push(self, priority, value):
        self.elements.append((priority, value))
        self.bubble_up(len(self.elements) - 1)

    def bubble_up(self, index):
        if index == 0:
            return

        parent_index = (index - 1) // 2
        parent_priority = self.elements[parent_index][0]
        current_priority = self.elements[index][0]

        if parent_priority > current_priority:
            self.elements[parent_index], self.elements[index] = (
                self.elements[index],
                self.elements[parent_index],
            )
            self.bubble_up(parent_index)

    def peek(self):
        if len(self.elements) == 0:
            return None

        return self.elements[0][1]


class Graph:
    def __init__(self, num_v):
        self.num_v = num_v
        self.adj = defaultdict(lambda: defaultdict(int))
        self.key = {}
        self.out_cut = {}
        for vertex in range(num_v):
            self.out_cut[vertex + 1] = True
        self.queue = MinHeap()

    def add_edge(self, u, v, w_u_v):
        if u not in self.adj.keys():
            self.key[u] = float("inf")
        if v not in self.adj.keys():
            self.key[v] = float("inf")
        self.adj[u][v] = w_u_v
        self.adj[v][u] = w_u_v

    def run_mst(self, start_vertex):
        self.key[start_vertex] = 0
        self.queue.push(0, start_vertex)
        self.out_cut[start_vertex] = False
        while self.queue.elements:
            _, current_vertex = self.queue.pop()
            self.out_cut[current_vertex] = False
            neighbors_list = self.adj[current_vertex].keys()
            for neighbor in neighbors_list:
                neigh_cost = self.adj[current_vertex][neighbor]
                if self.out_cut[neighbor] and self.key[neighbor] > neigh_cost:
                    self.key[neighbor] = self.adj[current_vertex][neighbor]
                    self.queue.push(neigh_cost, neighbor)

        total_cost = sum(self.key.values())
        if True in self.out_cut.values():
            total_cost = "impossivel"
        return total_cost


if __name__ == "__main__":
    data = sys.stdin.read().splitlines()
    iterator = iter(data)

    while True:
        try:
            info = next(iterator)
        except:
            break

        num_v, num_e = info.split(" ")
        graph = Graph(int(num_v))
        for edge_idx in range(int(num_e)):
            field_info = next(iterator)
            vertex_u, vertex_v, cost = field_info.split(" ")
            graph.add_edge(int(vertex_u), int(vertex_v), int(cost))

        result = graph.run_mst(1)
        sys.stdout.write(str(result))
