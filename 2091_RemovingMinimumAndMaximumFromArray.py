class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        min_index = nums.index(min(nums))
        max_index = nums.index(max(nums))
        n = len(nums)

        both_left = max(min_index, max_index) + 1
        both_right = n - min(min_index, max_index)
        left_right = (min_index + 1) + (n - max_index)
        right_left = (max_index + 1) + (n - min_index)

        return min(both_left, both_right, left_right, right_left)