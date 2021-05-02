# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        self.ans = []
        self.dfs(root)
        return self.ans

    def dfs(self, node, depth = 0):
        if not node:
            return
        while len(self.ans) < depth + 1:
            self.ans.append([])
        self.ans[depth].append(node.val)
        self.dfs(node.left, depth + 1)
        self.dfs(node.right, depth + 1)
