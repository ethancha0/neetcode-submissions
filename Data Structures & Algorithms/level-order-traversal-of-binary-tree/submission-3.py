# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        ans = [] 
        queue = deque()

        if root: 
            queue.append(root)

        while queue: 
            line = []
            for i in range(len(queue)):
                curr = queue.popleft()
                line.append(curr.val)

                if curr.left:
                    queue.append(curr.left)
                if curr.right: 
                    queue.append(curr.right)
                    
            ans.append(line)
        
        return ans
            


