class Graph:
    def __init__(self, num_v: int):
        self.num_v = num_v
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
