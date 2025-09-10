# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = deque([root])
        res = []

        forward = True
        while queue:
            n = len(queue)
            level_vals = []

            for i in range(n):
                node = queue.popleft()
                level_vals.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if forward:
                res.append(level_vals)
            else:
                res.append(level_vals[::-1])
            forward = not forward

        return res