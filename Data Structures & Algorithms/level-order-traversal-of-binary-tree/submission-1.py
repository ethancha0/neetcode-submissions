# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        

        def bfs(root):
            queue = deque()
            ans = []
            
            if root: 
                queue.append(root)


            while len(queue) > 0:
                levelNodes = []
                for i in range(len(queue)):
                    curr = queue.popleft()
                    levelNodes.append(curr.val)
                    if curr.left:
                        queue.append(curr.left)
                    if curr.right:
                        queue.append(curr.right)
                    
                ans.append(levelNodes)
                
            
            return ans
        
        return bfs(root)



                