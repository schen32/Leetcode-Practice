class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        direction = defaultdict(list)
        for a, b in connections:
            direction[a].append((b, 1))
            direction[b].append((a, 0))
        
        stack = [0]
        changes = 0
        visited = {0}
        while stack:
            city = stack.pop()

            for next_city, dir in direction[city]:
                if not next_city in visited:
                    visited.add(city)
                    stack.append(next_city)
                    changes += dir
        return changes