# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.good = 0

        def dfs(curr, maxSoFar) -> TreeNode:
            if not curr: 
                return None
            
            if curr.val >= maxSoFar:
                maxSoFar = curr.val
                self.good += 1 

            dfs(curr.left, maxSoFar)
            dfs(curr.right, maxSoFar)



            


        dfs(root, root.val)
        return self.good