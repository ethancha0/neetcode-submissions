# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def matches(curr, sub) -> bool:
            if not curr and not sub: 
                return True 
            elif not curr or not sub: 
                return False
            
            left = matches(curr.left, sub.left)
            right = matches(curr.right, sub.right)


            if curr.val == sub.val and left and right:
                return True
            else: 
                return False 



        if not root or not subRoot: 
            return False 
        
        return(
            matches(root, subRoot) or 
            self.isSubtree(root.left, subRoot) or 
            self.isSubtree(root.right, subRoot)
        )