class Graph:
    def __init__(self, num_v: int, num_e: int):
        self.num_v = num_v
        self.num_e = num_e
        self.vertex_degrees = [0] * (num_v + 1)

    def add_edge(self, u, v):
        self.vertex_degrees[u] += 1
        self.vertex_degrees[v] += 1

    def check_combinations(self):
        m_matrix = [False] * (self.num_e + 1)
        m_matrix[0] = True

        for vertex in range(1, self.num_v + 1):
            degree = self.vertex_degrees[vertex]
            for s in range(self.num_e, degree - 1, -1):
                if m_matrix[s - degree]:
                    m_matrix[s] = True

        if m_matrix[self.num_e]:
            return "S"
        else:
            return "N"
