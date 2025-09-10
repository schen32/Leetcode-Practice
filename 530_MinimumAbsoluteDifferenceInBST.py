# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        order = []

        def dfs(node):
            if not node:
                return

            dfs(node.left)
            order.append(node.val)
            dfs(node.right)
        dfs(root)
        
        min_diff = float("inf")
        for i in range(1, len(order)):
            diff = order[i] - order[i - 1]
            min_diff = min(min_diff, diff)
        return min_diff