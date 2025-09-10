# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float("-inf")

        def dfs(curr):
            if not curr:
                return 0

            left_max_sum = max(0, dfs(curr.left))
            right_max_sum = max(0, dfs(curr.right))

            curr_max_sum = curr.val + left_max_sum + right_max_sum
            self.max_sum = max(self.max_sum, curr_max_sum)

            return curr.val + max(left_max_sum, right_max_sum)
        
        dfs(root)
        return self.max_sum