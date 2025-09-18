# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        
        def find(node, clone):
            if not node:
                return None
            
            if node == target:
                return clone
            left = find(node.left, clone.left)
            right = find(node.right, clone.right)
            if left:
                return left
            if right:
                return right
            return None
        return find(original, cloned)