def count_patterns(grid):
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    visited = [[False]*cols for _ in range(rows)]
    def neighbors8(r, c):
        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):
                if dr == 0 and dc == 0:
                    continue
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    yield nr, nc
    def bfs_collect(r, c):
        stars = []
        queue = [(r, c)]
        visited[r][c] = True
        idx = 0
        while idx < len(queue):
            cr, cc = queue[idx]
            idx += 1
            stars.append((cr, cc))
            for nr, nc in neighbors8(cr, cc):
                if grid[nr][nc] == '*' and not visited[nr][nc]:
                    visited[nr][nc] = True
                    queue.append((nr, nc))
        return stars
    def normalize(coords):
        min_r = min(r for r, c in coords)
        min_c = min(c for r, c in coords)
        shifted = [(r - min_r, c - min_c) for (r, c) in coords]
        return frozenset(shifted)
    unique_shapes = set()
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '*' and not visited[r][c]:
                shape_coords = bfs_collect(r, c)
                shape_key = normalize(shape_coords)
                unique_shapes.add(shape_key)
    return len(unique_shapes)

if __name__ == "__main__":
    grid = ["..*..*..",
            "**.....*",
            ".....**.",
            "...*....",
            ".**....*"]
    print(count_patterns(grid)) # 2
    grid = ["....*..*",
            "*.......",
            "......*.",
            "..*.....",
            "......*."]
    print(count_patterns(grid)) # 1
    grid = ["***.*.**",
            ".*..*..*",
            ".*.***..",
            ".......*",
            "......**"]
    print(count_patterns(grid)) # 4
    grid = ["***.***.",
            "..*...*.",
            "**..**..",
            "..*...*.",
            "**..**.."]
    print(count_patterns(grid)) # 1
