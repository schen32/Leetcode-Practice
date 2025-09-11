class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)

        for (a, b), val in zip(equations, values):
            graph[a].append((b, val))
            graph[b].append((a, 1 / val))

        def bfs(start, end):
            if not start in graph or not end in graph:
                return -1.0
            if start == end:
                return 1.0
            
            visited = set()
            queue = deque([(start, 1.0)])
            while queue:
                curr, val = queue.popleft()
                visited.add(curr)
                if curr == end:
                    return val
                
                for neighbor, n_val in graph[curr]:
                    if not neighbor in visited:
                        queue.append((neighbor, val * n_val))
            return -1.0
        
        return [bfs(c, d) for c, d in queries]
