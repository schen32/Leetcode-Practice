# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def validate(node, lower, upper):
            if not node:
                return True
            if not (lower < node.val < upper):
                return False
            
            return validate(node.left, lower, node.val) and validate(node.right, node.val, upper)
        
        return validate(root, float("-inf"), float("inf"))