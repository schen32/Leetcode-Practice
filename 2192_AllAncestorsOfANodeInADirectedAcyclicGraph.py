from collections import defaultdict, deque
from typing import List

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        indegree = [0] * n
        
        for u, v in edges:
            graph[u].append(v)
            indegree[v] += 1
        
        # Topological sort
        queue = deque([i for i in range(n) if indegree[i] == 0])
        ancestors = [set() for _ in range(n)]
        
        while queue:
            node = queue.popleft()
            for nxt in graph[node]:
                # Add node and its ancestors to nxt
                ancestors[nxt].add(node)
                ancestors[nxt].update(ancestors[node])
                
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    queue.append(nxt)
        
        # Convert sets to sorted lists
        return [sorted(list(a)) for a in ancestors]
