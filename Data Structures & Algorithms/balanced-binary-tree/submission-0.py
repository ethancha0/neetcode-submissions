# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def helper(curr) -> (h, b):
            if not curr: 
                return (0, True)

            left = helper(curr.left)
            right = helper(curr.right) 

            height = max(left[0], right[0]) + 1 
            isBalanced = abs(left[0] - right[0]) <= 1 and left[1] and right[1]

            return (height, isBalanced)

        ans = helper(root)
        return ans[1]

