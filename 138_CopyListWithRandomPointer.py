"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummy = curr = Node(0)
        originalToCopy = dict()

        while head:
            if not head in originalToCopy:
                originalToCopy[head] = Node(head.val)

            curr.next = originalToCopy[head]
            curr = curr.next

            if not head.random in originalToCopy:
                if head.random:
                    originalToCopy[head.random] = Node(head.random.val)
                else:
                    originalToCopy[head.random] = None

            curr.random = originalToCopy[head.random]

            head = head.next
        
        return dummy.next