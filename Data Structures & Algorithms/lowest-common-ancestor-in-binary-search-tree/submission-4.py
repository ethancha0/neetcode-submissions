# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # the LCA is the node that splits 

        def dfs(root):
            if not root: 
                return 
            
            #check if both left or right 
            if p.val > root.val and q.val > root.val: 
                return dfs(root.right)
            elif p.val < root.val and q.val < root.val: 
                return dfs(root.left) 
            else: 
                return root


        
        return dfs(root)