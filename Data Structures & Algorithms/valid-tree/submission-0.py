class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #build freqmap 
        nodeMap = [[] for _ in range(n)]
        for n1, n2 in edges: 
            nodeMap[n1].append(n2)
            nodeMap[n2].append(n1)

        visitSet = set() 
        def dfs(node, parent):
            if node in visitSet: 
                return False 

            visitSet.add(node) 
            
            for child in nodeMap[node]:
                if child == parent: 
                    continue 
                if not dfs(child, node):
                    return False 

            return True 

        
        if not dfs(0, -1) or n != len(visitSet):
            return False 
        
        return True 
                


