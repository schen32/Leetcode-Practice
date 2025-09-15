class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        left, right = 0, len(nums) - 1
        operations = 0
        while left < right:
            sum = nums[left] + nums[right]
            if sum == k:
                operations += 1
                left += 1
                right -= 1
            elif sum < k:
                left += 1
            else:
                right -= 1
        return operations