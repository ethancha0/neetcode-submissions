class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = [] 

        def dfs(i, cur, total): 
            if total == target: 
                ans.append(cur.copy())
                return
            if total > target: 
                return 
            if i >= len(nums):
                return 


            #left case: inclusive, keep adding same num
            cur.append(nums[i])
            dfs(i, cur, total+nums[i])

            #right case: exclusive, move onto next num
            cur.pop() 
            dfs(i+1, cur, total)

        
        dfs(0, [], 0)

        return ans
