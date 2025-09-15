class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1_set = set(nums1)
        nums2_set = set(nums2)

        answer1 = set()
        for num in nums1:
            if not num in nums2_set:
                answer1.add(num)

        answer2 = set()
        for num in nums2:
            if not num in nums1_set:
                answer2.add(num)
        return [list(answer1), list(answer2)]