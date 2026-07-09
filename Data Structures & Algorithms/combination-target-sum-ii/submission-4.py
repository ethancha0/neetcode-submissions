class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
            candidates.sort() 
            ans = []

            def dfs(index, curr, total):
                if total == target: 
                    ans.append(curr.copy())
                    return 
                elif total > target: 
                    return 
                if index >= len(candidates): 
                    return 

                
                #left (inclusive) 
                curr.append(candidates[index])
                dfs(index+1, curr, total+candidates[index])


                #right (move onto next number)
                curr.pop()
                #before moving onto next elem, we should skip 
                while index+1 < len(candidates) and candidates[index] == candidates[index+1]:
                    index += 1
                dfs(index+1, curr, total)


            dfs(0, [], 0)
            return ans