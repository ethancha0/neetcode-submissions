# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        queue = deque()
        ans = []

        if root: 
            queue.append(root)
        
        while len(queue) > 0:
            rowVals = []
            for i in range(len(queue)):
                curr = queue.popleft()
                rowVals.append(curr.val)

                if curr.right: 
                    queue.append(curr.right)
                if curr.left:
                    queue.append(curr.left)

            ans.append(rowVals[0])
        
        return ans



        