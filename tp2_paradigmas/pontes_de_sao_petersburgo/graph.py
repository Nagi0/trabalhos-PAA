class Graph:
    def __init__(self, num_v: int, num_e: int):
        self.num_v = num_v
        self.num_e = num_e
        self.adj = {}

    def add_edge(self, u, v):
        if u in self.adj:
            self.adj[u].add(v)
        else:
            self.adj[u] = {v}
        if v in self.adj:
            self.adj[v].add(u)
        else:
            self.adj[v] = {u}

    def check_combinations(self):
        m_matrix = [False] * (self.num_e + 1)
        m_matrix[0] = True
        degrees_dict = {}

        for vertex, neighbors in self.adj.items():
            degrees_dict[vertex] = len(neighbors)

        for vertex in range(1, self.num_v + 1):
            degree = degrees_dict.get(vertex, 0)
            for s in range(self.num_e, degree - 1, -1):
                if m_matrix[s - degree]:
                    m_matrix[s] = True

        return m_matrix[self.num_e]
