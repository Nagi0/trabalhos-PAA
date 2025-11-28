import sys


class CardsGame:
    def __init__(self, num: int, array: list):
        self.num = num
        self.array = array

    def compute_best_game(self):
        m_vector_prev = self.array
        for k in range(1, self.num):
            num_intervals = self.num - k
            m_vector = [None] * num_intervals
            for i in range(num_intervals):
                j = i + k
                if i == j:
                    break
                m_vector[i] = max(self.array[i] - m_vector_prev[i + 1], self.array[j] - m_vector_prev[i])

            m_vector_prev = m_vector

        return self._get_player1_score(m_vector_prev[0])

    def _get_player1_score(self, score_difference) -> int:
        total = sum(self.array)
        return (total + score_difference) // 2


if __name__ == "__main__":
    data = sys.stdin.read().splitlines()
    iterator = iter(data)
    while True:
        try:
            num = int(next(iterator))
        except:
            break
        array = list(map(int, next(iterator).split(" ")))
        game = CardsGame(num, array)

        sys.stdout.writelines(f"{game.compute_best_game()}\n")
