# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(curr):
            if not curr: 
                return (True, 0)

            left = dfs(curr.left)
            right = dfs(curr.right)

            validHeight = abs(left[1] - right[1]) <= 1

            if left[0] and right[0] and validHeight:
                return(True, max(left[1], right[1]) + 1 )
            else:
                return(False, 999999 )

        return dfs(root)[0]