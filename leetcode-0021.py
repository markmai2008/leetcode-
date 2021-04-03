# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        p = l1
        n = 0
        while p:
            n += 1
            p = p.next
        q = l2
        m = 0
        while q:
            m += 1
            q = q.next
        z = m + n


        a = l1
        b = l2
        x = ListNode()
        y = x
        for i in range(z):
            if a and not b:
                y.next = a
                break
            elif not a and b:
                y.next = b
                break
            elif a.val >= b.val:
                y.next = b
                b = b.next
                y = y.next
                y.next = None
            else:
                y.next = a
                a = a.next
                y = y.next
                y.next = None
        return x.next
