class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []

        def dfs(index, curr, total):
            if target == total: 
                ans.append(curr.copy())
                return
            elif total > target: 
                return 
            if index >= len(candidates):
                return 

            # left 
            curr.append(candidates[index])
            dfs(index+1, curr, total+candidates[index])

            curr.pop() 
            while index+1 < len(candidates) and candidates[index] == candidates[index+1]:
                index += 1 
            
            # right 
            dfs(index+1, curr, total)

        dfs(0, [], 0)
        return ans

