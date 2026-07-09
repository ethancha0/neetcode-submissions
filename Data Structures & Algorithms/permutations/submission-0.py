class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        ans = [] 

        def dfs(curr, visited):
            if len(curr) == len(nums): 
                ans.append(curr.copy())

            #adding elem
            for elem in nums: 
                if elem not in visited: 
                    visited.append(elem)
                    curr.append(elem)
                    dfs(curr, visited)

            #backtracking 
            if curr: 
                curr.pop()
            if visited:
                visited.pop()
        
        dfs([], [])
        return ans