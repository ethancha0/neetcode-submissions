# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        #returns tuple [height, balanced]
        def dfs(root):
            if not root: 
                return [0, True]
            
            left = dfs(root.left)
            right = dfs(root.right)

            if left[1] == False or right[1] == False or abs(left[0] - right[0]) > 1:
                return [-1, False]
            
            return [max(left[0], right[0])+1, True]

        return dfs(root)[1]