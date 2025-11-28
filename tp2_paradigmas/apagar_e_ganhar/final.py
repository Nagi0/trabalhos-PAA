import sys


class Searcher:
    def __init__(self, num_n, num_d):
        self.num_n = num_n
        self.num_d = num_d

    def dynamic_solution(self, number):
        digits_list = [[None, -float("inf")]]
        positions_list = []
        m_vector = []
        for idx, digit in enumerate(str(number)):
            digits_list.append([idx, int(digit)])
            positions_list.append("")
        m_vector = [
            [[-float("inf"), 0] for _ in range((self.num_n - self.num_d) + 1)] for _ in range(len(digits_list))
        ]

        inseted_numbers = [[]] * len(digits_list)
        for idx in range(1, (self.num_n - self.num_d) + 1):
            inserted = []
            for s_idx in range(1, len(digits_list)):
                current_number = digits_list[s_idx]
                if current_number in inseted_numbers:
                    m_vector[s_idx][idx] = m_vector[s_idx - 1][idx]
                    continue
                current_pos = positions_list.copy()
                current_pos[current_number[0]] = current_number[1]
                new_number = int("".join(map(str, current_pos)))

                if s_idx > 1:
                    if new_number > m_vector[s_idx - 1][idx][1]:
                        m_vector[s_idx][idx] = [s_idx, new_number]
                        inserted = current_number
                    else:
                        m_vector[s_idx][idx] = m_vector[s_idx - 1][idx]
                else:
                    if new_number > m_vector[s_idx - 1][idx - 1][1]:
                        m_vector[s_idx][idx] = [s_idx, new_number]
                        inserted = current_number
                    else:
                        m_vector[s_idx][idx] = m_vector[s_idx - 1][idx]

            positions_list[inserted[0]] = inserted[1]
            inseted_numbers[idx] = inserted

        return m_vector[self.num_n][self.num_n - self.num_d][1]

    def greedy_solution(self, number):
        best_digits = []
        for digit in number:
            while self.num_d > 0 and len(best_digits) > 0 and digit > best_digits[-1]:
                best_digits.pop()
                self.num_d -= 1
            best_digits.append(digit)

        if self.num_d > 0:
            best_digits = best_digits[: -self.num_d]

        best_digits = "".join(best_digits)
        return best_digits


if __name__ == "__main__":
    data = sys.stdin.read().splitlines()
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
        number = next(iterator)

        sys.stdout.writelines(f"{searcher.greedy_solution(number)}\n")
