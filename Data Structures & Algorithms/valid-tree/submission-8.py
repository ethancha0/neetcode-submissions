class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjList = [[] for _ in range(n)]
        for n1, n2 in edges: 
            adjList[n1].append(n2)
            adjList[n2].append(n1)

        visited = set() 
        def dfs(node, prevNode) -> bool:
            if node in visited: 
                return False 

            visited.add(node) 

            for neighbor in adjList[node]:
                if neighbor == prevNode: 
                    continue
                if not dfs(neighbor, node):
                    return False 
                
            return True #???



        if not dfs(0, -1):
            return False 

        if not len(visited) == n:
            return False
        
        return True 

            
