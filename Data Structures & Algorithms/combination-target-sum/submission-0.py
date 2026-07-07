class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        ans = [] 

        def dfs(i, cur, total):
            # base case #1: we found a match
            if total == target: 
                ans.append(cur.copy())
                return 
            # base case #2: we reached end 
            if i >= len(nums): 
                return
            # case case #3: total is too high
            if total > target: 
                return 

            # left branch (include) 
            cur.append(nums[i])
            dfs(i, cur, total+nums[i])

            # right branch (exclude)
            cur.pop()
            dfs(i+1, cur, total)


        dfs(0, [], 0)
        return ans