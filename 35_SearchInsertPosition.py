class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        def binarySearch(left, right):
            if left > right:
                return left

            middle = (left + right) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                return binarySearch(middle + 1, right)
            else:
                return binarySearch(left, middle - 1)
        
        return binarySearch(0, len(nums) - 1)