"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        queue = deque([node])
        nodeToClone = { node: Node(node.val) }
        
        while queue:
            curr = queue.popleft()

            for neighbor in curr.neighbors:
                if not neighbor in nodeToClone:
                    nodeToClone[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)

                nodeToClone[curr].neighbors.append(nodeToClone[neighbor])
        
        return nodeToClone[node]
    
    """
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        nodeToClone = dict()
        def dfs(curr):
            if curr in nodeToClone:
                return nodeToClone[curr]
            
            clone = Node(curr.val)
            nodeToClone[curr] = clone
            for neighbor in curr.neighbors:
                clone.neighbors.append(dfs(neighbor))
            
            return clone
        
        return dfs(node)