class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = [[] for _ in range(n)]
        for n1, n2 in edges: 
            adjList[n1].append(n2)
            adjList[n2].append(n1)

        visited = set() 
        def dfs(node):
            if node in visited: 
                return 

            visited.add(node)

            for neighbor in adjList[node]:
                if neighbor not in visited: 
                    dfs(neighbor)


        graphs = 0 
        for i in range(n):
            if i not in visited:
                dfs(i)
                graphs += 1 

        return graphs

