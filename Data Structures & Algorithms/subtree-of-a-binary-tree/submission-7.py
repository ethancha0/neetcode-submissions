# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if not root: 
            return False 

        # we check if the left/right subnodes of root is equal to the head of subRoot
        left = self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot) 

        #check the current node against sub
        return left or right or self.valid(root, subRoot)








    def valid(self, root, subRoot):
        if not root and not subRoot: 
            return True 
        elif not root or not subRoot: 
            return False 
        if root.val != subRoot.val: 
            return False 

        left = self.valid(root.left, subRoot.left)
        right = self.valid(root.right, subRoot.right)

        return left and right and root.val == subRoot.val