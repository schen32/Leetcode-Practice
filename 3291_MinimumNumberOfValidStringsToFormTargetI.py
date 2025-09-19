class Solution:
    def minValidStrings(self, words: List[str], target: str) -> int:
        prefixes = set()
        for w in words:
            for i in range(1, len(w) + 1):
                prefixes.add(w[:i])
        
        memo = {}
        n = len(target)
        def dfs(i):
            if i >= n:
                return 0
            if i in memo:
                return memo[i]
            
            ans = float("inf")
            for j in range(i + 1, n + 1):
                if target[i:j] in prefixes:
                    ans = min(ans, 1 + dfs(j))
            memo[i] = ans
            return ans
        res = dfs(0)
        if res == float("inf"):
            return -1
        return res