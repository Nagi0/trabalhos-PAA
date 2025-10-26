import sys


class Graph:
    def __init__(self, num_v: int, ages_list: list):
        self.num_v = num_v
        self.adj = {}
        self.adj_revered = {}
        self.ages = {}
        self.charge = {}
        self.collab_charge = {}

        for idx, age in enumerate(ages_list):
            idx = idx + 1
            self.ages[idx] = int(age)
            self.charge[idx] = idx
            self.collab_charge[idx] = idx
            self.adj[idx] = set()
            self.adj_revered[idx] = set()

    def add_edge(self, u, v):
        if u in self.adj:
            self.adj[u].add(v)
        else:
            self.adj[u] = {v}
        if v not in self.adj:
            self.adj[v] = set()

        if v in self.adj_revered:
            self.adj_revered[v].add(u)
        else:
            self.adj_revered[v] = {u}
        if u not in self.adj_revered:
            self.adj_revered[u] = set()

    def switch_chain(self, collab_a, collab_b):
        a_charge, b_charge = self.collab_charge[collab_a], self.collab_charge[collab_b]
        self.charge[a_charge], self.charge[b_charge] = self.charge[b_charge], self.charge[a_charge]
        self.collab_charge[collab_a], self.collab_charge[collab_b] = b_charge, a_charge

    def yongest_manager(self, collaborator):
        youngest = self._reversed_breadth_first_search(collaborator)
        if youngest is None:
            return str("*")
        else:
            return int(youngest)

    def _reversed_breadth_first_search(self, start_vertex):
        visited = set()
        youngest = None
        start_vertex_charge = self.collab_charge[start_vertex]
        queue = [start_vertex_charge]

        while queue:
            current_vertex = queue.pop(0)
            neighbors_list = self.adj_revered[current_vertex]
            for neighbor in neighbors_list:
                if neighbor not in visited:

                    if youngest is None:
                        youngest = self.ages[self.charge[neighbor]]
                    if self.ages[self.charge[neighbor]] < youngest:
                        youngest = self.ages[self.charge[neighbor]]

                    queue.append(neighbor)
                    visited.add(neighbor)

        return youngest


if __name__ == "__main__":
    data = sys.stdin.read().splitlines()
    iterator = iter(data)

    while True:
        try:
            info = next(iterator)
        except:
            break
        num_v, num_e, num_instructions = info.split(" ")
        ages_list = next(iterator).split(" ")
        graph = Graph(int(num_v), ages_list)
        for edge_idx in range(int(num_e)):
            manager, collaborator = list(map(int, next(iterator).split(" ")))
            graph.add_edge(manager, collaborator)

        for instruction in range(int(num_instructions)):
            instruction_info = next(iterator).split(" ")
            if len(instruction_info) == 3:
                instruction_type, collaborator_a, collaborator_b = instruction_info
                graph.switch_chain(int(collaborator_a), int(collaborator_b))
            else:
                instruction_type, collaborator_a = instruction_info
                sys.stdout.write(str(graph.yongest_manager(int(collaborator_a))) + "\n")
