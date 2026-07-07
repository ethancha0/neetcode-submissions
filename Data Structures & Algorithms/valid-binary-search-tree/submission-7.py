# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def valid(curr, lower, upper) -> bool: 
            if not curr: 
                return True 
            
            left = valid(curr.left, lower, curr.val)
            right = valid(curr.right, curr.val, upper)

            if left and right and curr.val > lower and curr.val < upper: 
                return True 
            else:
                return False

        
        return valid(root, float("-inf"), float("inf"))