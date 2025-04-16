# Solution 1: Brute Force BFS on every root node
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # bidirectional edges map
        edgesMap = defaultdict(list)
        for edge in edges:
            a, b = edge
            edgesMap[a].append(b)
            edgesMap[b].append(a)

        # bfs to get height of tree with a particular root node
        def bfs(i):
            queue = deque([i])
            visited = set([i])

            height = 0
            while queue:
                n = len(queue)
                for i in range(n):
                    cur = queue.popleft()

                    for nextNode in edgesMap[cur]:
                        if nextNode not in visited:
                            queue.append(nextNode)
                            visited.add(nextNode)
                height += 1
            return height
        
        # map root node to height of its tree
        rootHeight = dict()
        minHeight = n
        for i in range(n):
            height = bfs(i)
            rootHeight[i] = height
            minHeight = min(minHeight, height)

        # return all min height root node trees
        res = []
        for root, height in rootHeight.items():
            if height == minHeight:
                res.append(root)
        return res

# Solution 2
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        edgesMap = defaultdict(list)
        for a, b in edges:
            edgesMap[a].append(b)
            edgesMap[b].append(a)
        
        edgeCount = dict()
        leaves = deque()
        for src, nei in edgesMap.items():
            if len(nei) == 1:
                leaves.append(src)
            edgeCount[src] = len(nei)
        
        while leaves:
            if n <= 2:
                return list(leaves)
            for i in range(len(leaves)):
                node = leaves.popleft()
                n -= 1
                for nei in edgesMap[node]:
                    edgeCount[nei] -= 1
                    if edgeCount[nei] == 1:
                        leaves.append(nei)