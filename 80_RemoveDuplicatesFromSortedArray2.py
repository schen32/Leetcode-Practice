class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)

        insertPos = 2
        for i in range(2, len(nums)):
            if nums[i] != nums[insertPos - 2]:
                nums[insertPos] = nums[i]
                insertPos += 1
        return insertPos