# maxflow.py
from collections import deque, defaultdict


class MaxFlowDict:

    def __init__(self, source_name, terminal_name):
        self.res = defaultdict(lambda: defaultdict(int))  # capacidade residual
        self.adj = defaultdict(set)
        self.source_node = source_name
        self.terminal_node = terminal_name

    def add_edge(self, u, v, c):
        if c < 0:
            raise ValueError("Capacidade não pode ser negativa.")
        if c == 0:
            return
        self.res[u][v] += c
        self.adj[u].add(v)
        self.adj[v].add(u)
        _ = self.res[v][u]

    def max_flow(self):
        flow = 0
        # BFS
        while True:
            parent = self._run_bfs()
            if self.terminal_node not in parent:
                break  # não há caminho aumentante

            increment = self._estimate_bottleneck(self.source_node, self.terminal_node, parent)

            self.augument_flow(self.source_node, self.terminal_node, parent, increment)

            flow += increment
        return flow

    def _run_bfs(self):
        parent = {self.source_node: None}
        q = deque([self.source_node])
        while q and self.terminal_node not in parent:
            u = q.popleft()
            for v in self.adj[u]:
                if v not in parent and self.res[u][v] > 0:
                    parent[v] = u
                    q.append(v)
                    if v == self.terminal_node:
                        break

        return parent

    def _estimate_bottleneck(self, src, term, parents_list):
        inc = float("inf")
        v = term
        while v != src:
            u = parents_list[v]
            inc = min(inc, self.res[u][v])
            v = u

        return inc

    def augument_flow(self, src, term, parents_list, inc):
        v = term
        while v != src:
            u = parents_list[v]
            self.res[u][v] -= inc
            self.res[v][u] += inc
            v = u
