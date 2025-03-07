def find_sums(numbers, size):
    n = len(numbers)
    if size > n:
        return []

    current_sum = sum(numbers[:size])
    result = [current_sum]

    for i in range(size, n):
        current_sum = current_sum - numbers[i-size] + numbers[i]
        result.append(current_sum)

    return result

print(find_sums([1,2,3,4,5], 3))  # [6, 9, 12]
