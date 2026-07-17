class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = [[] for _ in range(n)]
        for n1, n2 in edges: 
            adjList[n1].append(n2)
            adjList[n2].append(n1)

        visitSet = set()
        def dfs(node) -> int: 
            if node in visitSet: 
                return 0 
            
            visitSet.add(node)

            for n in adjList[node]:
                dfs(n)


        ans = 0 
        for i in range(n): 
            if i not in visitSet:
                dfs(i)
                ans += 1 
        
        return ans


                