import time

def task2_solution(n=10**5):
    data = []
    start_add = time.time()
    for i in range(1, n+1):
        data.append(i)
    end_add = time.time()

    start_del = time.time()
    for _ in range(n):
        data.pop(0)  # Very inefficient
    end_del = time.time()

    time_for_additions = end_add - start_add
    time_for_deletions = end_del - start_del
    print("Approach A (List append + pop(0)):")
    print(f"Time for additions: {time_for_additions:.5f} s")
    print(f"Time for deletions: {time_for_deletions:.5f} s")

task2_solution()
