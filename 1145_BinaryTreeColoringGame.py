# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def btreeGameWinningMove(self, root: Optional[TreeNode], n: int, x: int) -> bool:
        def find(node):
            if not node:
                return None
            if node.val == x:
                return node
            
            left = find(node.left)
            right = find(node.right)
            if left:
                return left
            if right:
                return right
            return None
        
        x_node = find(root)

        def dfs(node):
            if not node:
                return 0
            
            return 1 + dfs(node.left) + dfs(node.right)
        
        left_len = dfs(x_node.left)
        right_len = dfs(x_node.right)
        rest_len = n - left_len - right_len - 1
        max_len = max(left_len, right_len, rest_len)

        return max_len > n // 2