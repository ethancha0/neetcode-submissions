# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #isSubtree will dfs through root looking for matching starting point
        def check(curr, sub) -> bool:
            # check will compare two trees for exact same structure
            if not curr and not sub: 
                return True
            if not curr or not sub:
                return False
            
            if curr.val != sub.val:
                return False
            
            return check(curr.left, sub.left) and check(curr.right, sub.right)



        # normal dfs, if a given node value is the same as subroot, we check 
        if not root: 
            return False

        left = self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot)

        return check(root, subRoot) or left or right