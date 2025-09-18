class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        stack = [source]
        visited = {source}
        while stack:
            curr = stack.pop()
            if curr == destination:
                return True
            
            for nei in graph[curr]:
                if not nei in visited:
                    stack.append(nei)
                    visited.add(nei)
        return False