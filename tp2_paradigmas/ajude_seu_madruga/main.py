import sys
import time
from cutter import PaperCutter

if __name__ == "__main__":
    start_time = time.perf_counter()
    data = open("tp2_paradigmas/ajude_seu_madruga/data.txt").read().splitlines()
    iterator = iter(data)
    while True:
        try:
            info = next(iterator)
            num_columns, target_area = list(map(int, info.split(" ")))
            if info == "0 0":
                break
            columns_width = list(map(int, next(iterator).strip().split(" ")))
        except Exception as e:
            print(e)
            break

        paper_cutter = PaperCutter(num_columns, columns_width, target_area)
        sys.stdout.writelines(f"{paper_cutter.find_height()}\n")
    end_time = time.perf_counter()
    print(f"Execution time: {end_time - start_time}")
