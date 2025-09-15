class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix_sum = [0]
        postfix_sum = [0]
        for num in nums:
            prefix_sum.append(prefix_sum[-1] + num)
        for num in nums[::-1]:
            postfix_sum.append(postfix_sum[-1] + num)
        
        for i in range(len(nums)):
            if prefix_sum[i] == postfix_sum[len(nums) - 1 - i]:
                return i
        return -1