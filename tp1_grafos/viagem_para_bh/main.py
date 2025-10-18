import time
from dijkstra import Graph

if __name__ == "__main__":
    start_time = time.perf_counter()
    data = open("tp1_grafos/viagem_para_bh/data.txt").read().splitlines()
    iterator = iter(data)

    while True:
        try:
            info = next(iterator)
        except:
            break
        num_v, num_e = info.split(" ")
        graph_bus = Graph(int(num_v))
        graph_plane = Graph(int(num_v))
        for edge_idx in range(int(num_e)):
            city_a, city_b, plane, coast = next(iterator).split(" ")
            if int(plane):
                graph_plane.add_edge(int(city_a), int(city_b), int(coast))
            else:
                graph_bus.add_edge(int(city_a), int(city_b), int(coast))

        if len(graph_plane.adj.keys()) > 0:
            plane_coast = graph_plane.run_dijkstra()
        else:
            plane_coast = float("inf")
        if len(graph_bus.adj.keys()) > 0:
            bus_coast = graph_bus.run_dijkstra()
        else:
            bus_coast = float("inf")

        print(min(plane_coast, bus_coast))

    end_time = time.perf_counter()
    print(f"Execution time: {end_time-start_time}")
