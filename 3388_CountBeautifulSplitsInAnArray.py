class Solution:
    def beautifulSplits(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0

        for i in range(1, n - 1):         # split after nums1
            for j in range(i + 1, n):     # split after nums2
                nums1 = nums[:i]
                nums2 = nums[i:j]
                nums3 = nums[j:]

                # condition 1: nums1 is prefix of nums2
                if len(nums1) <= len(nums2) and nums1 == nums2[:i]:
                    count += 1
                # condition 2: nums2 is prefix of nums3
                elif len(nums2) <= len(nums3) and nums2 == nums3[:j]:
                    count += 1

        return count