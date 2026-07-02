# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(curr) -> (int, bool): #returns height, and is balanced
            if not curr: 
                return(0, True)

            left = dfs(curr.left)
            right = dfs(curr.right)

            balanced = abs(left[0] -  right[0]) <= 1 

            if balanced and left[1] and right[1]:
                return (max(left[0], right[0]) + 1, True)
            else:
                return (99999, False)

        
        return dfs(root)[1]