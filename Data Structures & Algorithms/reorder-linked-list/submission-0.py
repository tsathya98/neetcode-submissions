# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Brute force
        """
        lst = []
        cur = head
        while cur:
            lst.append(cur.val)
            cur = cur.next

        new_lst = []
        i, l, r = 0, 0, len(lst) - 1
        while i<len(lst) and l<len(lst) and r>=0:
            if i%2 == 0:
                new_lst.append(lst[l])
                l+=1
            else:
                new_lst.append(lst[r])
                r-=1
            i+=1
        cur = head
        for num in new_lst:
            cur.val = num
            cur = cur.next
