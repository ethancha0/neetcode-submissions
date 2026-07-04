# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(curr, maxVal) -> int:
            if not curr: 
                return 0
            
            if curr.val >= maxVal:
                maxVal = curr.val
                a = 1
            else:
                a = 0 
            
            left = dfs(curr.left, maxVal)
            right = dfs(curr.right, maxVal)

            return a + left + right
        
        return dfs(root, root.val)