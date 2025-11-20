import sys
import time
from searcher import Searcher

if __name__ == "__main__":
    start_time = time.perf_counter()
    data = open("tp2_paradigmas/apagar_e_ganhar/data.txt").read().splitlines()
    iterator = iter(data)
    while True:
        try:
            info = next(iterator)
            if info == "0 0":
                break
        except:
            break
        total_num, erase_num = list(map(int, info.split(" ")))
        searcher = Searcher(total_num, erase_num)
        number = int(next(iterator))

        sys.stdout.writelines(f"{searcher.find_best_numbers(number)}\n")
    end_time = time.perf_counter()
    print(f"Execution time: {end_time - start_time}")
