class Scheduler:
    def __init__(self, num_tasks: int):
        self.num_tasks = num_tasks
        self.tasks = []

    def add_task(self, task: int, start_time: int, duration: int):
        self.tasks.append([task, start_time, duration, start_time + duration])

    def schedule(self):
        self.tasks = sorted(self.tasks, key=lambda x: x[1])
        current_time = 1
        for idx in range(len(self.tasks)):
            _, start_time, duration, _ = self.tasks[idx]
            if idx == 0:
                current_time = start_time
            elif current_time < start_time:
                current_time = start_time

            current_time += duration

        return current_time
