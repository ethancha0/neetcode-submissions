# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(curr, lower, upper) -> bool:
            if not curr: 
                return True

            validLeft = dfs(curr.left, lower, curr.val)
            validRight = dfs(curr.right, curr.val, upper)

            if validLeft and validRight and curr.val > lower and curr.val < upper:
                return True 
            else:
                return False
        
        return dfs(root, float("-inf"), float("inf"))