import sys
import time
from game import CardsGame

if __name__ == "__main__":
    start_time = time.perf_counter()
    data = open("tp2_paradigmas/cartoes/data.txt").read().splitlines()
    iterator = iter(data)
    while True:
        try:
            num = int(next(iterator))
        except:
            break
        array = list(map(int, next(iterator).split(" ")))
        game = CardsGame(num, array)

        sys.stdout.writelines(f"{game.compute_best_game()}\n")
    end_time = time.perf_counter()
    print(f"Execution time: {end_time - start_time}")
