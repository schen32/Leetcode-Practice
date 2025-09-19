class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total = sum(nums)
        
        # Standard Kadane's for max subarray
        max_sum = cur_max = nums[0]
        for x in nums[1:]:
            cur_max = max(x, cur_max + x)
            max_sum = max(max_sum, cur_max)
        
        # Kadane's for min subarray
        min_sum = cur_min = nums[0]
        for x in nums[1:]:
            cur_min = min(x, cur_min + x)
            min_sum = min(min_sum, cur_min)
        
        if max_sum < 0:
            # all numbers negative
            return max_sum
        return max(max_sum, total - min_sum)
