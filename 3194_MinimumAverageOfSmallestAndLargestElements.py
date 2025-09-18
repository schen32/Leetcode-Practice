class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        averages = []
        left = 0
        right = len(nums) - 1
        while left < right:
            averages.append(nums[left] + nums[right])
            left += 1
            right -= 1
        return min(averages) / 2