# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.order = [float("-inf")]

        def build_order(node):
            if not node:
                return
            
            build_order(node.left)
            self.order.append(node.val)
            build_order(node.right)
        
        build_order(root)
        self.pointer = 0

    def next(self) -> int:
        self.pointer += 1
        return self.order[self.pointer]

    def hasNext(self) -> bool:
        if self.pointer + 1 < len(self.order):
            return True
        return False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()