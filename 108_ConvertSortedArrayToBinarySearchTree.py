# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def divide(left, right):
            if left > right:
                return None
            
            middle = (left + right) // 2
            node = TreeNode(nums[middle])
            node.left = divide(left, middle - 1)
            node.right = divide(middle + 1, right)
            return node
        
        return divide(0, len(nums) - 1)