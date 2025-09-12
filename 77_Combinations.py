class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        all_paths = []
        def backtrack(i, path):
            if len(path) == k:
                all_paths.append(path.copy())
                return
            
            for j in range(i, n + 1):
                path.append(j)
                backtrack(j + 1, path)
                path.pop()
        
        backtrack(1, [])
        return all_paths