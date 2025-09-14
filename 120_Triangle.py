class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        memo = {}
        def dfs(row, i):
            if row >= len(triangle):
                return 0
            elif (row, i) in memo:
                return memo[(row, i)]
            
            left = triangle[row][i] + dfs(row + 1, i)
            right = triangle[row][i] + dfs(row + 1, i + 1)
            memo[(row, i)] = min(left, right)
            return memo[(row, i)]
            
        return dfs(0, 0)