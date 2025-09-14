class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m = len(s1)
        n = len(s2)
        if m + n != len(s3):
            return False
        
        memo = {}
        def dfs(i, j):
            if i == m and j == n:
                return True
            elif (i, j) in memo:
                return memo[(i, j)]

            k = i + j
            ans = False
            if i < m and s1[i] == s3[k] and dfs(i + 1, j):
                ans = True
            elif j < n and s2[j] == s3[k] and dfs(i, j + 1):
                ans = True
            memo[(i, j)] = ans
            return ans
        return dfs(0, 0)