import sys
import time
from graph import Graph

if __name__ == "__main__":
    start_time = time.perf_counter()
    data = open("tp2_paradigmas/pontes_de_sao_petersburgo/data.txt").read().splitlines()
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
    end_time = time.perf_counter()
    print(f"Execution time: {end_time - start_time}")
