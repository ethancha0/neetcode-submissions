class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        ans = []

        def dfs(index, cur, total): 
            if index >= len(nums):
                return 
            if total == target:
                ans.append(cur.copy())
                return
            if total > target:
                return

            # left (inclusive)
            cur.append(nums[index])
            dfs(index, cur, total+nums[index])

            # right (exclusive)
            cur.pop()
            dfs(index+1, cur, total)


        dfs(0, [], 0) 

        return ans 
            
            