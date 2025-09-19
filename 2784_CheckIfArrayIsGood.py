class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = len(nums) - 1
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        
        if freq[n] != 2:
            return False
        
        for i in range(1, n):
            if freq[i] != 1:
                return False
        
        return len(freq) == n