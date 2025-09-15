# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        n = 0
        curr = head
        while curr:
            n += 1
            curr = curr.next
        
        twins = dict()
        max_sum = float("-inf")
        i = 0
        while head:
            if (n - i - 1) in twins:
                twins[n - i - 1] += head.val
                max_sum = max(max_sum, twins[n - i - 1])
            else:
                twins[i] = head.val
            i += 1
            head = head.next
        return max_sum