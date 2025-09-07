class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        numsIndex = dict()

        for i, num in enumerate(nums):
            if num in numsIndex:
                if abs(numsIndex[num] - i) <= k:
                    return True
            
            numsIndex[num] = i
    
        return False