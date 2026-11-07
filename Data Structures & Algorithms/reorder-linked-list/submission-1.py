# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def _print(self, head: Optional[ListNode], ref: Optional[str]) -> None:
        cur = head
        if ref:
            print(ref, end=":")
        while cur:
            print(cur.val, end=" ")
            cur = cur.next
        print('\n')
        
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        - tortoise hare approach
        - reverse 2nd half
        - iterate through original LL and append original list and then reversed LL in this order
        """
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        slow.next = None
        prev = None
        while second:
            nn = second.next
            second.next = prev
            prev = second
            second = nn
        # Now prev has the head of the reversed LL
        first = head
        second = prev
        while second:
            tmp1 = first.next
            tmp2 = second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2
        
