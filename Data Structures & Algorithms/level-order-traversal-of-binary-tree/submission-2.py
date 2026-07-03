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
                ans.append([root.val])


            while len(queue) > 0:
                levelNodes = []
                for i in range(len(queue)):
                    curr = queue.popleft()

                    if curr.left:
                        queue.append(curr.left)
                        levelNodes.append(curr.left.val)
                    if curr.right:
                        queue.append(curr.right)
                        levelNodes.append(curr.right.val)
                
                if levelNodes != []:
                    ans.append(levelNodes)
                
            
            return ans
        
        return bfs(root)



                