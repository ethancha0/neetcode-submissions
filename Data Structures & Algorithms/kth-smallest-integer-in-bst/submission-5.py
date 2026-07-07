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
        
        
        # use an in order traversal (left -> curr -> right)
        def dfs(curr) -> TreeNode:
            if not curr: 
                return None
            
            

            dfs(curr.left)

            self.visited += 1 
            if self.visited == k: 
                self.ans = curr.val


            dfs(curr.right)

        dfs(root)
        return self.ans


            