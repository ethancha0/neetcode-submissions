class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        ans = [] 
        candidates.sort()

        def dfs(i, cur, total):
            if total == target: 
                ans.append(cur.copy())
                return 
            if total > target: 
                return 
            if i >= len(candidates):
                return 

            
            #left case: inclusive
            cur.append(candidates[i])
            dfs(i+1, cur, total+candidates[i])

            #right case: exclusive
            cur.pop()
            # skip all duplicates of candidates[i]
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i+1, cur, total)




        dfs(0, [], 0)

        return ans
