class Solution:
    def climbStairs(self, n: int) -> int:
        
        def dfs(n, memo):
            if n in memo:
                return memo[n]
            if n <= 1:
                return 1
            
            memo[n] = dfs(n - 1, memo) + dfs(n - 2, memo)
            return memo[n]
            
        return dfs(n, {})