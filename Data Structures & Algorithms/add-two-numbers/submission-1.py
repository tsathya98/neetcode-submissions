# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur1 = l1
        cur2 = l2
        dummy = ListNode(0, cur1)
        ptr = dummy
        carry = 0
        while cur1 or cur2 or carry:
            v1 = cur1.val if cur1 else 0
            v2 = cur2.val if cur2 else 0
            tot = v1+v2+carry
            carry = tot // 10
            tot %= 10
            ptr.next = ListNode(tot)
            cur1 = cur1.next if cur1 else None
            cur2 = cur2.next if cur2 else None
            ptr = ptr.next
        ptr.next = cur1 if cur1 else cur2
        return dummy.next