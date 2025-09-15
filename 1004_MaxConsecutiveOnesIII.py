class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        num_zeros = 0
        max_len = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                num_zeros += 1

            while num_zeros > k:  # shrink window
                if nums[left] == 0:
                    num_zeros -= 1
                left += 1

            # window [left, right] is valid
            max_len = max(max_len, right - left + 1)

        return max_len