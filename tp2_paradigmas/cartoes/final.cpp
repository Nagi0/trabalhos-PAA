// O Código foi baseado em uma implementação feita em Python.
// Como a execução no Python estava demorando mais do que aceito pela plataforma, foi feita uma tradução para C++.
// A lógica do algoritmo permanece a mesma, a única mudança foi a linguagem implementada, aparentemente o Python não conseguiu comportar o limite.

// import sys


// class CardsGame:
//     def __init__(self, num: int, array: list):
//         self.num = num
//         self.array = array

//     def compute_best_game(self):
//         m_vector_prev = self.array
//         for k in range(1, self.num):
//             num_intervals = self.num - k
//             m_vector = [None] * num_intervals
//             for i in range(num_intervals):
//                 j = i + k
//                 if i == j:
//                     break
//                 m_vector[i] = max(self.array[i] - m_vector_prev[i + 1], self.array[j] - m_vector_prev[i])

//             m_vector_prev = m_vector

//         return self._get_player1_score(m_vector_prev[0])

//     def _get_player1_score(self, score_difference) -> int:
//         total = sum(self.array)
//         return (total + score_difference) // 2


// if __name__ == "__main__":
//     data = sys.stdin.read().splitlines()
//     iterator = iter(data)
//     while True:
//         try:
//             num = int(next(iterator))
//         except:
//             break
//         array = list(map(int, next(iterator).split(" ")))
//         game = CardsGame(num, array)

//         sys.stdout.writelines(f"{game.compute_best_game()}\n")

#include <bits/stdc++.h>
using namespace std;

class CardsGame {
public:
    int num;
    vector<long long> array;

    CardsGame(int num, const vector<long long>& array) {
        this->num = num;
        this->array = array;
    }

    long long compute_best_game() {
        vector<long long> m_vector_prev = array;

        for (int k = 1; k < num; ++k) {
            int num_intervals = num - k;
            vector<long long> m_vector(num_intervals);

            for (int i = 0; i < num_intervals; ++i) {
                int j = i + k;
                long long pega_i = array[i] - m_vector_prev[i + 1];
                long long pega_j = array[j] - m_vector_prev[i];
                m_vector[i] = max(pega_i, pega_j);
            }

            m_vector_prev.swap(m_vector);
        }

        long long score_difference = m_vector_prev[0];
        return _get_player1_score(score_difference);
    }

private:
    long long _get_player1_score(long long score_difference) {
        long long total = 0;
        for (int i = 0; i < num; ++i) {
            total += array[i];
        }
        return (total + score_difference) / 2;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int num;
    while (cin >> num) {
        vector<long long> array(num);
        for (int i = 0; i < num; ++i) {
            cin >> array[i];
        }

        CardsGame game(num, array);
        cout << game.compute_best_game() << '\n';
    }

    return 0;
}
