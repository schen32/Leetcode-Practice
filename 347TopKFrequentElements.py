class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        eleCount = defaultdict(int)
        for num in nums:
            eleCount[num] += 1
        
        # pop min element when len of minHeap greater than k
        minHeap = []
        for ele, count in eleCount.items():
            heapq.heappush(minHeap, [count, ele])
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        
        # minHeap contains k max elements
        res = []
        for count, ele in minHeap:
            res.append(ele)
        return res