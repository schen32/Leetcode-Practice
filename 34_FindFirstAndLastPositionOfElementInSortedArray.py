class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def search(left, right):
            if left > right:
                return -1
            
            middle = (left + right) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                return search(middle + 1, right)
            else:
                return search(left, middle - 1)
        
        index = search(0, len(nums) - 1)
        if index == -1:
            return [-1, -1]
        
        left = right = index
        while left - 1 >= 0 and nums[left - 1] == nums[index]:
            left -= 1
        while right + 1 < len(nums) and nums[right + 1] == nums[index]:
            right += 1
        return [left, right]