# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def valid(curr, sub) -> bool: 
            if not curr and not sub: 
                return True
            if not curr or not sub:
                return False 
            
            left = valid(curr.left, sub.left)
            right = valid(curr.right, sub.right)

            return left and right and curr.val == sub.val







        if not root: 
            return False

        left = self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot)

        return(left or right or valid(root, subRoot))