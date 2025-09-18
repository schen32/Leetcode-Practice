class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        n = len(arr)
        left = 0
        right = 0
        window_sum = 0
        while right < k:
            window_sum += arr[right]
            right += 1
        
        res = 0
        if window_sum >= k * threshold:
            res += 1

        while right < n:
            window_sum += arr[right]
            window_sum -= arr[left]
            left += 1
            right += 1
            if window_sum >= k * threshold:
                res += 1
        return res