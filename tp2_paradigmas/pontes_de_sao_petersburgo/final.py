import sys


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


if __name__ == "__main__":
    data = sys.stdin.read().splitlines()
    iterator = iter(data)
    while True:
        try:
            info = next(iterator)
        except:
            break
        num_v, num_e = info.split(" ")
        graph = Graph(int(num_v), int(num_e))
        for edge_idx in range(int(num_e)):
            region_a, region_b = list(map(int, next(iterator).split(" ")))
            graph.add_edge(region_a, region_b)

        sys.stdout.writelines(f"{graph.check_combinations()}\n")
