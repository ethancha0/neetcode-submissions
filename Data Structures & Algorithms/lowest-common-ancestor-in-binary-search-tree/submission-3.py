# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        self.ans = TreeNode()

        def dfs(node):
            if p.val < node.val and q.val < node.val: 
                dfs(node.left)
            elif p.val > node.val and q.val > node.val: 
                dfs(node.right)
            else:
                self.ans = node

        dfs(root)
        return self.ans