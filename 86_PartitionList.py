# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy_less = less = ListNode()
        dummy_greater = greater = ListNode()

        while head:
            if head.val < x:
                less.next = ListNode(head.val)
                less = less.next
            else:
                greater.next = ListNode(head.val)
                greater = greater.next

            head = head.next
        
        less.next = dummy_greater.next
        return dummy_less.next