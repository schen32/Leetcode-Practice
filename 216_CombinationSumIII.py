class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        res = []
        def backtrack(start, path, total):
            if total > n:
                return
            if len(path) == k and total == n:
                res.append(path.copy())
                return
                
            for i in range(start, 10):
                path.append(i)
                backtrack(i + 1, path, total + i)
                path.pop()
            return
        backtrack(1, [], 0)
        return res