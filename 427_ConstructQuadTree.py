"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        
        n = len(grid)

        def build(r0, c0, size):
            # Check if the current square is uniform
            first_val = grid[r0][c0]
            uniform = True
            for i in range(r0, r0 + size):
                for j in range(c0, c0 + size):
                    if grid[i][j] != first_val:
                        uniform = False
                        break
                if not uniform:
                    break

            if uniform:
                return Node(val=bool(first_val), isLeaf=True)

            # Split into quadrants
            half = size // 2
            return Node(
                val=True,  # value doesn't matter when isLeaf=False
                isLeaf=False,
                topLeft=build(r0, c0, half),
                topRight=build(r0, c0 + half, half),
                bottomLeft=build(r0 + half, c0, half),
                bottomRight=build(r0 + half, c0 + half, half)
            )

        return build(0, 0, n)