class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        m = len(word1)
        n = len(word2)
        memo = {}
        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            if i == m:
                return n - j
            elif j == n:
                return m - i
            
            if word1[i] == word2[j]:
                memo[(i, j)] = dfs(i + 1, j + 1)
            else:
                insert = 1 + dfs(i, j + 1)
                delete = 1 + dfs(i + 1, j)
                replace = 1 + dfs(i + 1, j + 1)
                memo[(i, j)] = min(insert, delete, replace)
            return memo[(i, j)]
        return dfs(0, 0)