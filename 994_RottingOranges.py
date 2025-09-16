class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        fresh = 0

        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))
                elif grid[i][j] == 1:
                    fresh += 1

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        minutes = 0
        while queue:
            row, col, minutes = queue.popleft()
            
            for x, y in directions:
                n_row, n_col = row + x, col + y
                if not n_row in range(m) or not n_col in range(n):
                    continue
                if grid[n_row][n_col] == 1:
                    queue.append((n_row, n_col, minutes + 1))
                    grid[n_row][n_col] = 2
                    fresh -= 1
        if fresh > 0:
            return -1
        return minutes