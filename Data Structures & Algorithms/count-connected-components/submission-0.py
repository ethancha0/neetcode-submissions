class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = [[] for _ in range(n)]
        for n1, n2 in edges: 
            adjList[n1].append(n2)
            adjList[n2].append(n1)

        visitSet = set()
        def dfs(node, prev) -> int: 
            if node in visitSet: 
                return 0 
            
            visitSet.add(node)

            for n in adjList[node]:
                dfs(n, node)

            return len(visitSet) + 1 


        ans = 0 
        for i in range(n): 
            if i not in visitSet:
                dfs(i, -1)
                ans += 1 
        
        return ans


                