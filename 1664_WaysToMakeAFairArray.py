class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        
        even_total = sum(nums[i] for i in range(0, len(nums), 2))
        odd_total = sum(nums[i] for i in range(1, len(nums), 2))

        res = 0
        even_left = odd_left = 0

        for i, x in enumerate(nums):
            if i % 2 == 0:  # even index
                even_total -= x
                new_even = even_left + odd_total
                new_odd = odd_left + even_total
                if new_even == new_odd:
                    res += 1
                even_left += x
            else:           # odd index
                odd_total -= x
                new_even = even_left + odd_total
                new_odd = odd_left + even_total
                if new_even == new_odd:
                    res += 1
                odd_left += x

        return res