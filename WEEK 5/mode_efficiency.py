import random
import time

n = 10**7
numbers = [random.randint(1, 1000) for _ in range(n)]

def find_mode_dict(nums):
    count = {}
    mode = nums[0]
    for x in nums:
        if x not in count:
            count[x] = 0
        count[x] += 1
        if count[x] > count[mode]:
            mode = x
    return mode

def find_mode_sort(nums):
    nums.sort()
    mode = nums[0]
    current = nums[0]
    current_count = 1
    max_count = 1
    for i in range(1, len(nums)):
        if nums[i] == current:
            current_count += 1
        else:
            if current_count > max_count:
                max_count = current_count
                mode = current
            current = nums[i]
            current_count = 1
    if current_count > max_count:
        mode = current
    return mode

start = time.time()
m1 = find_mode_dict(numbers)
t1 = time.time() - start

start = time.time()
m2 = find_mode_sort(numbers)
t2 = time.time() - start

print(m1, t1)
print(m2, t2)
