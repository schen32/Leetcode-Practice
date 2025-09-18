class Solution:
    def clearStars(self, s: str) -> str:
        
        deleted = set()
        minHeap = []
        for i, char in enumerate(s):
            if char == "*":
                deleted_char, deleted_i = heapq.heappop(minHeap)
                deleted.add(-deleted_i)
                deleted.add(i)
            else:
                heapq.heappush(minHeap, (char, -i))
        
        res = []
        for i, char in enumerate(s):
            if i in deleted:
                continue
            
            res.append(char)
        return "".join(res)