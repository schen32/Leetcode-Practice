class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        # Convert each row and column to a tuple
        rows = [tuple(row) for row in grid]
        cols = [tuple(grid[i][j] for i in range(n)) for j in range(n)]
        
        res = 0
        # Compare tuples directly
        for row in rows:
            for col in cols:
                if row == col:
                    res += 1
        return res
