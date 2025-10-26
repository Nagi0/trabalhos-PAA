import sys
import time
from dfs_search import Graph

if __name__ == "__main__":
    start_time = time.perf_counter()
    data = open("tp1_grafos/chefe/data.txt").read().splitlines()
    iterator = iter(data)

    while True:
        try:
            info = next(iterator)
        except:
            break
        num_v, num_e, num_instructions = info.split(" ")
        ages_list = next(iterator).split(" ")
        graph = Graph(int(num_v), ages_list)
        for edge_idx in range(int(num_e)):
            manager, collaborator = list(map(int, next(iterator).split(" ")))
            graph.add_edge(manager, collaborator)

        for instruction in range(int(num_instructions)):
            instruction_info = next(iterator).split(" ")
            if len(instruction_info) == 3:
                instruction_type, collaborator_a, collaborator_b = instruction_info
                graph.switch_chain(int(collaborator_a), int(collaborator_b))
            else:
                instruction_type, collaborator_a = instruction_info
                sys.stdout.write(str(graph.yongest_manager(int(collaborator_a))) + "\n")

    end_time = time.perf_counter()
    print(f"Execution time: {end_time-start_time}")
