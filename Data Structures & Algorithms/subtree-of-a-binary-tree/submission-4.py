# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def dfs(root, subroot):
            if not root and not subroot: 
                return True 
            elif not root or not subroot or root.val != subroot.val: 
                return False 

            left = dfs(root.left, subroot.left)
            right = dfs(root.right, subroot.right)

            return left and right


        if not root: 
            return False 

        if dfs(root, subRoot):
            return True
            
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)