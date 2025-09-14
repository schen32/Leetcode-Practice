class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        memo = {}

        def dfs(row, col):
            if row >= m or col >= n:
                return float("inf")
            elif row == m - 1 and col == n - 1:
                return grid[row][col]
            elif (row, col) in memo:
                return memo[(row, col)]
            
            down = dfs(row + 1, col)
            right = dfs(row, col + 1)
            memo[(row, col)] = grid[row][col] + min(down, right)
            return memo[(row, col)]
        return dfs(0, 0)