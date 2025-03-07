def find_rounds(numbers):
    rounds = []
    n = len(numbers)
    next_needed = 1
    data = list(numbers)

    while next_needed <= n:
        round_list = []
        new_data = []
        for x in data:
            if x == next_needed:
                round_list.append(x)
                next_needed += 1
            else:
                new_data.append(x)
        rounds.append(round_list)
        data = new_data

    return rounds

print(find_rounds([2,1,4,7,5,3,6,8]))
