class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjList = [[] for _ in range(n)]
        for n1, n2 in edges: 
            adjList[n1].append(n2)
            adjList[n2].append(n1)

        visited = set()
        def dfs(node, prev):
            if node in visited: 
                return False 
            
            visited.add(node)

            for child in adjList[node]:
                if child == prev:
                    continue
                if not dfs(child, node):
                    return False

            return True 

        if not dfs(0, -1) or len(visited) != n:
            return False
        return True 