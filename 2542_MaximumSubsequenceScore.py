class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pairs = sorted(zip(nums2, nums1), reverse=True)  # sort by nums2 descending
        
        heap = []
        heap_sum = 0
        result = 0
        
        for n2, n1 in pairs:
            heapq.heappush(heap, n1)
            heap_sum += n1
            
            if len(heap) > k:
                heap_sum -= heapq.heappop(heap)
            
            if len(heap) == k:
                result = max(result, heap_sum * n2)
        
        return result