import sys
import time
from sorter import Sorter

if __name__ == "__main__":
    start_time = time.perf_counter()
    data = open("tp2_paradigmas/calouro_vence_veterano/data.txt").read().splitlines()
    iterator = iter(data)
    while True:
        try:
            num = int(next(iterator))
        except:
            break
        students_list = []
        for student in range(num):
            student = next(iterator)
            students_list.append(student)

        sorter = Sorter(num)
        sorter.count_inversions(students_list)
        sys.stdout.writelines(f"{sorter.inv_counter}\n")
    end_time = time.perf_counter()
    print(f"Execution time: {end_time - start_time}")
