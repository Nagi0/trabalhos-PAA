import sys


class Sorter:
    def __init__(self, num: int) -> None:
        self.num = num
        self.inv_counter = 0

    def count_inversions(self, array: list):
        if len(array) > 1:
            left_array = array[: len(array) // 2]
            right_array = array[len(array) // 2 :]
            sorted_left_array = self.count_inversions(left_array)
            sorted_right_array = self.count_inversions(right_array)

            return self._merge(sorted_left_array, sorted_right_array)
        else:
            return array

    def _merge(self, left_array, right_array):
        merged_array = []
        i = 0
        j = 0
        while i < len(left_array) and j < len(right_array):
            if left_array[i] <= right_array[j]:
                merged_array.append(left_array[i])
                i += 1
            else:
                merged_array.append(right_array[j])
                j += 1
                self.inv_counter += len(left_array) - i
        while i < len(left_array):
            merged_array.append(left_array[i])
            i += 1
        while j < len(right_array):
            merged_array.append(right_array[j])
            j += 1
        return merged_array


if __name__ == "__main__":
    data = sys.stdin.read().splitlines()
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
