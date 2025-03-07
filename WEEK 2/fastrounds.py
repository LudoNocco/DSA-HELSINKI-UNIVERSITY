def count_rounds(numbers):
    n = len(numbers)
    pos = [0]*(n+1)
    for i, val in enumerate(numbers):
        pos[val] = i

    rounds = 1
    for x in range(1, n):
        if pos[x+1] < pos[x]:
            rounds += 1
    return rounds

print(count_rounds([4,3,2,1]))  # 4
print(count_rounds([1,3,2,4]))  # 2
