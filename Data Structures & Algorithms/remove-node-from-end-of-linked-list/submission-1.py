# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next
        rem = length - n
        if rem == 0:
            return head.next
        cur = head
        i=1
        while i < rem:
            cur = cur.next
            i+=1
        cur.next = cur.next.next
        return head