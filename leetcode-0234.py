# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        a = []
        b = []
        def fun(p):
            if not p:
                return
            a.append(p.val)
            fun(p.next)
            b.append(p.val)
        fun(head)
        return a==b

