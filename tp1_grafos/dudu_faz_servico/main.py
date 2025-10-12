import time
from dfs_search import Graph


def check_cycles_full_graph(graph: Graph):
    cycle_exists = "NAO"
    for v in graph.graph:
        if graph.colors[v] == "white":
            _, result = graph.depth_first_search(v)
            if result == "SIM":
                cycle_exists = "SIM"
                break
    print(cycle_exists)


if __name__ == "__main__":
    start_time = time.perf_counter()
    data = open("tp1_grafos/dudu_faz_servico/data.txt").read().split()
    iterator = iter(data)
    num_problems = int(next(iterator))

    for problem_idx in range(num_problems):
        num_v = int(next(iterator))
        num_e = int(next(iterator))
        graph = Graph()
        for edge_idx in range(num_e):
            vertex_u = int(next(iterator))
            vertex_v = int(next(iterator))
            graph.add_edge(vertex_u, vertex_v)

        check_cycles_full_graph(graph)

    end_time = time.perf_counter()
    print(f"Execution time: {end_time-start_time}")
