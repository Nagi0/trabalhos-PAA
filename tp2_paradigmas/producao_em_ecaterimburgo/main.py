import sys
import time
from interval import Scheduler

if __name__ == "__main__":
    start_time = time.perf_counter()
    data = open("tp2_paradigmas/produção_em_ecaterimburgo/data.txt").read().splitlines()
    iterator = iter(data)
    while True:
        try:
            info = next(iterator)
        except:
            break
        num_tasks = int(info)
        scheduler = Scheduler(num_tasks)
        for task_idx in range(num_tasks):
            task, duration = list(map(int, next(iterator).split(" ")))
            scheduler.add_task(task_idx, task, duration)

        sys.stdout.writelines(f"{scheduler.schedule()}\n")
    end_time = time.perf_counter()
    print(f"Execution time: {end_time - start_time}")
