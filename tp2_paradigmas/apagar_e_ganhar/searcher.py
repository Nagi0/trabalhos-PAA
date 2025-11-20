class Searcher:
    def __init__(self, num_n, num_d):
        self.num_n = num_n
        self.num_d = num_d

    def find_best_numbers(self, number):
        digits_list = []
        positions_list = []
        for idx, digit in enumerate(str(number)):
            digits_list.append([idx, int(digit)])
            positions_list.append("")
        sorted_digits = sorted(digits_list, reverse=True, key=lambda x: x[1])
        best_digits = sorted(sorted_digits[: self.num_n - self.num_d], key=lambda x: x[0])
        remaining_digits = sorted(sorted_digits[self.num_n - self.num_d :], key=lambda x: x[0])

        for item in best_digits:
            positions_list[item[0]] = item[1]
        current_digit = int("".join(map(str, positions_list)))

        m_vector = [(current_digit, best_digits[-1])]
        for idx, item in enumerate(remaining_digits):
            replaced_item = positions_list.copy()
            replaced_item[m_vector[-1][1][0]] = ""
            replaced_item[item[0]] = item[1]
            replaced_item = int("".join(map(str, replaced_item)))
            if current_digit < replaced_item:
                print()
        print(best_digits)
