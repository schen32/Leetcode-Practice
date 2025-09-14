class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        memo = {}

        def dfs(row, col):
            if row >= m or col >= n:
                return 0
            elif obstacleGrid[row][col] == 1:
                return 0
            elif row == m - 1 and col == n - 1:
                return 1
            elif (row, col) in memo:
                return memo[(row, col)]
            
            down = dfs(row + 1, col)
            right = dfs(row, col + 1)
            memo[(row, col)] = down + right
            return memo[(row, col)]
        return dfs(0, 0)