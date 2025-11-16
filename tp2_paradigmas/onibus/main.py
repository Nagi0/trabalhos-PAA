import sys
import time
from line import Line

if __name__ == "__main__":
    start_time = time.perf_counter()
    data = open("tp2_paradigmas/onibus/data.txt").read().splitlines()
    iterator = iter(data)
    while True:
        try:
            info = next(iterator)
        except:
            break
        length, m_bus_colors, bus_colors = list(map(int, info.split(" ")))
        line = Line(length, m_bus_colors, bus_colors, 5, 10)

        sys.stdout.writelines(f"{line.compute_combinations()}\n")
    end_time = time.perf_counter()
    print(f"Execution time: {end_time - start_time}")
