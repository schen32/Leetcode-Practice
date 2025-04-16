class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # cumulative products in both directions
        prefix = [nums[0]]
        suffix = [nums[-1]]
        for num in nums[1:]:
            prefix.append(prefix[-1] * num)
        for i in range(len(nums) - 2, -1, -1):
            suffix.append(suffix[-1] * nums[i])
        suffix.reverse()
        
        answer = []
        for i, num in enumerate(nums):
            if i == 0:
                answer.append(suffix[1])
            elif i == len(nums) - 1:
                answer.append(prefix[-2])
            else:
                answer.append(prefix[i-1] * suffix[i+1])
        return answer