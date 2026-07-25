# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
    
        return self.valid(root, float("-inf"), float("inf"))





    def valid(self, root, lower, upper):
        if not root: 
            return True 

        left = self.valid(root.left, lower, root.val)
        right = self.valid(root.right, root.val, upper)

        return left and right and root.val > lower and root.val < upper

