import time
from dfs_search import Graph


if __name__ == "__main__":
    start_time = time.perf_counter()
    data = open("tp1_grafos/novo_campus/data.txt").read().splitlines()
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
        print(result)

    end_time = time.perf_counter()
    print(f"Execution time: {end_time-start_time}")
