class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        
        minHeap = [(0, k)]
        visited = set()
        res = 0  # <-- track maximum shortest distance
        
        while minHeap:
            curr_time, curr_node = heapq.heappop(minHeap)
            if curr_node in visited:
                continue
            visited.add(curr_node)
            res = max(res, curr_time)  # <-- ensure we capture the max
            
            for v, w in graph[curr_node]:
                if v not in visited:
                    heapq.heappush(minHeap, (curr_time + w, v))

        return res if len(visited) == n else -1