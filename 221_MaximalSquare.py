class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        m, n = len(matrix), len(matrix[0])
        memo = {}

        def dfs(row, col):
            if row >= m or col >= n:
                return 0
            if (row, col) in memo:
                return memo[(row, col)]

            down = dfs(row + 1, col)
            right = dfs(row, col + 1)
            diag = dfs(row + 1, col + 1)

            if matrix[row][col] == "1":
                memo[(row, col)] = 1 + min(down, right, diag)
            else:
                memo[(row, col)] = 0
            return memo[(row, col)]

        max_side = 0
        for i in range(m):
            for j in range(n):
                max_side = max(max_side, dfs(i, j))

        return max_side * max_side