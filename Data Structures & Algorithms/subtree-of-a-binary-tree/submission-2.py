# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def sameTree(curr, sub):
            if not curr and not sub: 
                return True
            elif not curr or not sub: 
                return False 
            
            if curr.val != sub.val:
                return False
            
            left = sameTree(curr.left, sub.left)
            right = sameTree(curr.right, sub.right)

            if left and right: 
                return True 



        

        if not root: 
            return False
        
        left = self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot)

        return(
            sameTree(root, subRoot)
            or left
            or right
        )