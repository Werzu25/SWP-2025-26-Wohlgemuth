import random
import numpy as np

def lotto(num_draws, num_count):
    draw_numbers = np.arange(1, num_count+1)
    for i in range(0, num_draws+1):
        random_num = random.randint(1, draw_numbers.size-i)
        number_drawn = draw_numbers[-(i+1)]
        draw_numbers[-(i+1)] = draw_numbers[random_num-1]
        draw_numbers[random_num-1] = number_drawn
    return draw_numbers[-num_draws:]

def __main__():
    stat_result = np.zeros(45)
    for i in range(0, 100001):
        result = lotto(6, 45)
        for j in range(0, 6):
            stat_result[result[j]-1] += 1
    print(stat_result)

if __name__ == "__main__":
    __main__()