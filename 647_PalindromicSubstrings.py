class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        memo = {}
        
        def dfs(start, end):
            if start > end:
                return False
            if start == end:
                return True
            if start + 1 == end:
                return s[start] == s[end]
            if (start, end) in memo:
                return memo[(start, end)]
            memo[(start, end)] = s[start] == s[end] and dfs(start + 1, end - 1)
            return memo[(start, end)]
    
        count = 0
        for i in range(n):
            for j in range(i, n):
                if dfs(i, j):
                    count += 1
        return count
