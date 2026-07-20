class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()

        self.ans = []

        def dfs(index, curr, total):
            if total == target: 
                self.ans.append(curr.copy())
                return
            if index == len(candidates) or total > target:
                return 


            #left branch (inclusive)
            curr.append(candidates[index])
            dfs(index+1, curr, total+candidates[index])

            curr.pop() 
            #fast forward to skip duplicates
            while index+1 < len(candidates) and candidates[index] == candidates[index+1]:
                index += 1 
            #right branch (exclusive)
            dfs(index+1, curr, total)

        dfs(0, [], 0)

        return self.ans