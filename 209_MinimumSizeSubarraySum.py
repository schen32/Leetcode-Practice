class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        sum_window = 0
        left = 0
        min_size = float("inf")

        for right in range(len(nums)):
            sum_window += nums[right]

            while sum_window >= target:
                min_size = min(min_size, right - left + 1)
                sum_window -= nums[left]
                left += 1
        
        if min_size == float("inf"):
            return 0
        return min_size