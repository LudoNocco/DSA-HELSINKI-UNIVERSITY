from collections import deque

def find_order(n):
    dq = deque(range(1, n+1))
    removed_order = []
    while dq:
        dq.append(dq.popleft())
        removed_order.append(dq.popleft())
    return removed_order

print(find_order(7))  # [2, 4, 6, 1, 5, 3, 7]
