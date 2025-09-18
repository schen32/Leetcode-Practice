class Solution:
    def minOperations(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        
        ops = 0
        for count in freq.values():
            if count <= 1:
                return -1
            
            if count % 3 == 0:
                ops += count // 3
            elif count % 3 == 1:
                ops += (count - 4) // 3 + 2
            elif count % 3 == 2:
                ops += count // 3 + 1
        return ops