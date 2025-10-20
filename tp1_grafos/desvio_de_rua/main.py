import sys
import time
from operator import itemgetter
from kosaraju import Graph


def check_graph_scc(graph: Graph, remove_edge: tuple) -> str:
    graph.remove_edge(remove_edge[0], remove_edge[1], remove_edge[2])
    if check_single_scc(graph):
        return "-"
    else:
        graph.reset_search_states()
        graph.change2not_directed()
        if check_impossible(graph):
            return "*"
        else:
            graph.reset_search_states()
            return "2" if graph.depth_first_search(1) else "1"


def check_single_scc(graph: Graph) -> bool:
    for vertex in graph.graph:
        if graph.colors[vertex] == "white":
            graph.depth_first_search(vertex)
    terminate_time = sorted(graph.terminate_time.items(), key=itemgetter(1), reverse=True)
    for vertex, _ in terminate_time:
        if graph.colors_inv[vertex] == "white":
            graph.reversed_depth_first_search(vertex)
            if graph.scc_count > 1:
                return False

    return True


def check_impossible(graph: Graph) -> bool:
    for idx, vertex in enumerate(graph.graph):
        if graph.colors[vertex] == "white":
            if idx == 0:
                graph.depth_first_search(vertex)
            else:
                return True

    return False


if __name__ == "__main__":
    start_time = time.perf_counter()
    data = open("tp1_grafos/desvio_de_rua/data.txt").read().splitlines()
    iterator = iter(data)

    while True:
        try:
            info = next(iterator)
        except:
            break
        num_v, num_e = info.split(" ")
        graph = Graph()
        remove_edge = ()
        for edge_idx in range(int(num_e)):
            cross_a, cross_b, directions = list(map(int, next(iterator).split(" ")))
            if edge_idx == 0:
                remove_edge = (cross_a, cross_b, directions)
            graph.add_edge(cross_a, cross_b, directions)
            if directions == 2:
                graph.safe_double_edges.add(frozenset((cross_a, cross_b)))
        sys.stdout.write(f"{check_graph_scc(graph, remove_edge)}\n")

    end_time = time.perf_counter()
    print(f"Execution time: {end_time-start_time}")
