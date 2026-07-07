# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        ans = [] 
        queue = deque()

        if root: 
            queue.append(root)

        while queue:
            row = []
            for i in range(len(queue)):
                
                curr = queue.popleft()
                row.append(curr.val)

                if curr.right: 
                    queue.append(curr.right)
                if curr.left:
                    queue.append(curr.left)
            
            ans.append(row[0])

        return ans
