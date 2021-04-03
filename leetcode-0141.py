# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle1(self, head: ListNode) -> bool:
        a = []
        b = head
        while b:
            if b in a:
                return True
            a.append(b)
            b = b.next
        return False
    def hasCycle(self, head: ListNode) -> bool:
        a = head
        b = head
        while a:
            if not a.next:
                return False
            a = a.next.next
            b = b.next
            if a == b:
                return True
        return False
