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

            res = 1 if curr.val >= maxVal else 0
            maxVal = max(maxVal, curr.val)


            # amount of good nodes in left/right branches
            left = dfs(curr.left, maxVal)
            right = dfs(curr.right, maxVal)
            return res + left + right


        return dfs(root, root.val)
