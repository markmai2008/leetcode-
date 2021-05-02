# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.eg(root.left, root.right)
    def eg(self, lnode, rnode):
        if not lnode and not rnode:
            return True
        if not lnode and rnode or lnode and not rnode:
            return False
        return lnode.val == rnode.val and self.eg(lnode.left, rnode.right) and self.eg(lnode.right, rnode.left)
