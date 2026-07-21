# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def valid(root, sub):
            if not root and not sub: 
                return True 
            if not root or not sub: 
                return False 
            if root.val != sub.val: 
                return False 

            left = valid(root.left, sub.left) 
            right = valid(root.right, sub.right) 

            return left and right and root.val == sub.val



        if not root:
            return False 

        if valid(root, subRoot): 
            return True 

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


