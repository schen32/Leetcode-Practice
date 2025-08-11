class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n

        def reverseArr(arr, left, right):
            while left < right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1

        reverseArr(nums, 0, n - 1)
        reverseArr(nums, 0, k - 1)
        reverseArr(nums, k, n - 1)