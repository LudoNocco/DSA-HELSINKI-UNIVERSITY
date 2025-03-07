def count_rooms(grid):
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    visited = [[False]*cols for _ in range(rows)]
    def neighbors(r, c):
        for nr, nc in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
            if 0 <= nr < rows and 0 <= nc < cols:
                yield nr, nc
    def bfs(sr, sc):
        queue = [(sr, sc)]
        visited[sr][sc] = True
        idx = 0
        while idx < len(queue):
            r, c = queue[idx]
            idx += 1
            for nr, nc in neighbors(r, c):
                if grid[nr][nc] == '.' and not visited[nr][nc]:
                    visited[nr][nc] = True
                    queue.append((nr, nc))
    room_count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '.' and not visited[r][c]:
                room_count += 1
                bfs(r, c)
    return room_count

if __name__ == "__main__":
    grid = ["########",
            "#.#..#.#",
            "#####..#",
            "#...#..#",
            "########"]
    print(count_rooms(grid)) # 4
    grid = ["########",
            "#......#",
            "#.####.#",
            "#......#",
            "########"]
    print(count_rooms(grid)) # 1
    grid = ["########",
            "######.#",
            "##.#####",
            "########",
            "########"]
    print(count_rooms(grid)) # 2
