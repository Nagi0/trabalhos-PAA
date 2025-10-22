import sys
import time
from dijkstra import Graph


if __name__ == "__main__":
    start_time = time.perf_counter()
    data = open("tp1_grafos/final_mundial_de_2008/data.txt").read().splitlines()
    iterator = iter(data)
    instance_counter = 1

    while True:
        try:
            info = next(iterator)
            sys.stdout.write(f"Instancia {instance_counter}\n")
        except:
            break

        num_v, num_e = info.split(" ")
        graph = Graph(int(num_v))
        for edge_idx in range(int(num_e)):
            field_info = next(iterator)
            vertex_u, vertex_v, cost = list(map(int, field_info.split(" ")))
            if vertex_v not in graph.adj.get(vertex_u, []):
                graph.add_edge(vertex_u, vertex_v, cost)
            else:
                current_coast = graph.adj.get(vertex_u, {}).get(vertex_v, float("inf"))
                if cost < current_coast:
                    graph.add_edge(vertex_u, vertex_v, cost)

        eval_cases = int(next(iterator).strip())
        for eval_c in range(eval_cases):
            origin, destiny, t = next(iterator).split(" ")
            result = graph.run_dijkstra(int(origin), int(destiny), int(t))
            graph.reset_dijkstra()
            sys.stdout.write(f"{result}\n")

        sys.stdout.write("\n")
        instance_counter += 1

    end_time = time.perf_counter()
    print(f"Execution time: {end_time-start_time}")
