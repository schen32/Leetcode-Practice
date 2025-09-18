class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        length = 1  # length of current alternating segment

        for i in range(1, n):
            if nums[i] != nums[i - 1]:
                length += 1
            else:
                res += length * (length + 1) // 2
                length = 1  # reset length

        res += length * (length + 1) // 2  # add last segment
        return res
