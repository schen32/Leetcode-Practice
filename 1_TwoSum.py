class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numIndex = dict()

        for i, num in enumerate(nums):
            diff = target - num

            if diff in numIndex:
                return [numIndex[diff], i]
            
            numIndex[num] = i
        
        return [-1, -1]