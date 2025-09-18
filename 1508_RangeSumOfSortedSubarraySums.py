class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        MOD = 10 ** 9 + 7
        
        subarray_sums = []
        for i in range(n):
            sub_sum = 0
            for j in range(i, n):
                sub_sum += nums[j]
                subarray_sums.append(sub_sum)
        
        subarray_sums.sort()
        return sum(subarray_sums[left - 1: right]) % MOD