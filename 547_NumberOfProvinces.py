class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        def dfs(city, visited):
            stack = [city]
            while stack:
                curr = stack.pop()
                if curr in visited:
                    continue
                visited.add(curr)

                for next_city, is_connected in enumerate(isConnected[curr]):
                    if not next_city in visited and is_connected:
                        stack.append(next_city)
        
        provinces = 0
        visited = set()
        for i in range(len(isConnected)):
            if not i in visited:
                dfs(i, visited)
                provinces += 1
        return provinces