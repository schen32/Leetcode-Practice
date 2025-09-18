# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        
        self.total_tilt = 0
        def dfs(node):
            if not node:
                return 0
            
            sum_left = dfs(node.left)
            sum_right = dfs(node.right)
            self.total_tilt += abs(sum_left - sum_right)
            return node.val + sum_left + sum_right
        dfs(root)

        return self.total_tilt