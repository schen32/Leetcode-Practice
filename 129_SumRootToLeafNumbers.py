# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        stack = []
        stack.append((root, str(root.val)))
        numbers = []

        while stack:
            curr, num = stack.pop()

            if not curr.left and not curr.right:
                numbers.append(int(num))
            if curr.left:
                stack.append((curr.left, num + str(curr.left.val)))
            if curr.right:
                stack.append((curr.right, num + str(curr.right.val)))
        
        return sum(numbers)