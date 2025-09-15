class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        num_zeros = 0
        max_len = 0
        
        for right in range(len(nums)):
            if nums[right] == 0:
                num_zeros += 1
            
            while num_zeros > 1:
                if nums[left] == 0:
                    num_zeros -= 1
                left += 1
            
            max_len = max(max_len, right - left)
        return max_len