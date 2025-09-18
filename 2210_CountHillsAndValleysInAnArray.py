class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        
        n = len(nums)
        i = 1
        res = 0
        while i < n:
            left = i - 1
            right = i + 1

            while left >= 0 and nums[left] == nums[i]:
                left -= 1
            while right < n and nums[right] == nums[i]:
                right += 1
            
            if left < 0 or right >= n:
                i = right
                continue
            if nums[left] < nums[i] > nums[right]:
                res += 1
            if nums[left] > nums[i] < nums[right]:
                res += 1
            i = right
        return res