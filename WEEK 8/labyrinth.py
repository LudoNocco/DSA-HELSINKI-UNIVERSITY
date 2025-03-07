import heapq

def find_route(grid):
    R, C = len(grid), len(grid[0])
    start, goal = None, None
    for i in range(R):
        for j in range(C):
            if grid[i][j] == 'A':
                start = (i, j)
            elif grid[i][j] == 'B':
                goal = (i, j)
    if not start or not goal:
        return None
    distances = { (i, j): float('inf') for i in range(R) for j in range(C) }
    distances[start] = 0
    heap = [(0, start)]
    while heap:
        d, pos = heapq.heappop(heap)
        if pos == goal:
            return d
        if d > distances[pos]:
            continue
        for di, dj in [(1,0),(-1,0),(0,1),(0,-1)]:
            ni, nj = pos[0]+di, pos[1]+dj
            if 0 <= ni < R and 0 <= nj < C and grid[ni][nj] != '#':
                new_d = d + 1
                if new_d < distances[(ni, nj)]:
                    distances[(ni, nj)] = new_d
                    heapq.heappush(heap, (new_d, (ni, nj)))
    return None

if __name__ == "__main__":
    grid = ["########",
            "#B#...A#",
            "#.#.##.#",
            "#......#",
            "########"]
    print(find_route(grid))  # Expected output: 9
