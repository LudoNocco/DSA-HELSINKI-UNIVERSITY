class WordFinder:
    def set_grid(self, grid):
        self.grid = grid
        self.height = len(grid)
        self.width = len(grid[0]) if self.height > 0 else 0

    def count(self, word):
        if len(word) == 1:
            return sum(row.count(word) for row in self.grid)
        word_reversed = word[::-1]
        word_set = {word, word_reversed}
        total_count = 0
        directions = [(1, 0), (0, 1), (1, 1), (1, -1)]
        def count_in_direction(dx, dy):
            c = 0
            for y in range(self.height):
                for x in range(self.width):
                    for w in word_set:
                        if self._matches(x, y, dx, dy, w):
                            c += 1
            return c
        for dx, dy in directions:
            total_count += count_in_direction(dx, dy)
        return total_count

    def _matches(self, x, y, dx, dy, word):
        for i, char in enumerate(word):
            nx = x + i * dx
            ny = y + i * dy
            if nx < 0 or ny < 0 or nx >= self.width or ny >= self.height:
                return False
            if self.grid[ny][nx] != char:
                return False
        return True

if __name__ == "__main__":
    grid = ["TIRATIRA","IRATIRAT","RATIRATI","ATIRATIR"]
    finder = WordFinder()
    finder.set_grid(grid)
    print(finder.count("TIRA"))
    print(finder.count("TA"))
    print(finder.count("RITARI"))
    print(finder.count("A"))
    print(finder.count("AA"))
    print(finder.count("RAITA"))
