# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0 

        def getHeight(curr):
            if not curr: 
                return 0 
            
            left = getHeight(curr.left)
            right = getHeight(curr.right)

            self.ans = max(self.ans, left + right) 
            return max(left, right) + 1
        
        getHeight(root)
        return self.ans
