# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.visited = 0 
        self.ans = 0 

        def dfs(root) -> int: 
            if not root: 
                return 0 
            
            left = dfs(root.left)

            self.visited += 1  # current
            if self.visited == k:
                self.ans = root.val

            right = dfs(root.right)
         
        dfs(root)
        return self.ans


        