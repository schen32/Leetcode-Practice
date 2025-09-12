class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        def backtrack(path, used):
            if len(path) == len(nums):
                res.append(path.copy())
                return
            
            for i in range(len(nums)):
                if i in used:
                    continue

                used.add(i)
                path.append(nums[i])
                backtrack(path, used)
                used.remove(i)
                path.pop()
        backtrack([], set())
        return res