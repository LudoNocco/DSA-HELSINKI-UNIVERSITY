import random
import time

def count_rounds_list(numbers):
    pos = [0] * (len(numbers) + 1)
    for i, x in enumerate(numbers):
        pos[x] = i

    rounds = 1
    for i in range(2, len(numbers) + 1):
        if pos[i] < pos[i - 1]:
            rounds += 1

    return rounds

def count_rounds_dict(numbers):
    pos = {x: i for i, x in enumerate(numbers)}

    rounds = 1
    for i in range(2, len(numbers) + 1):
        if pos[i] < pos[i - 1]:
            rounds += 1

    return rounds

numbers = list(range(1, 10**7 + 1))
random.shuffle(numbers)

start_time_list = time.time()
rounds_list = count_rounds_list(numbers)
time_taken_list = time.time() - start_time_list

start_time_dict = time.time()
rounds_dict = count_rounds_dict(numbers)
time_taken_dict = time.time() - start_time_dict

print(time_taken_list, time_taken_dict)
