class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        
        res = 0
        consec = 0
        for num in nums:
            if num == 0:
                consec += 1
                res += consec
            else:
                consec = 0
        return res