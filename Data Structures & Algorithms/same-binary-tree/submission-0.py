# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def dfs(cur1, cur2) -> (bool):
            if not cur1 and not cur2:
                return True
            elif not cur1 and cur2:
                return False
            elif cur1 and not cur2:
                return False
            
            #both nodes exist below this comment

            left = dfs(cur1.left, cur2.left)
            right = dfs(cur1.right, cur2.right)

            return (cur1.val == cur2.val) and left and right

        
        return dfs(p, q)