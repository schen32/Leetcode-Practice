class Solution:
    def minMoves(self, nums: List[int]) -> int:
        min_nums = min(nums)
        return sum(i - min_nums for i in nums)