import time

def task1_solution(n=10**5):
    data = []
    start_add = time.time()
    for i in range(1, n+1):
        data.append(i)  # append at the end
    end_add = time.time()

    start_del = time.time()
    for _ in range(n):
        data.pop()      # pop from the end
    end_del = time.time()

    time_for_additions = end_add - start_add
    time_for_deletions = end_del - start_del
    print("Approach A (List append/pop):")
    print(f"Time for additions: {time_for_additions:.5f} s")
    print(f"Time for deletions: {time_for_deletions:.5f} s")

task1_solution()
