class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        ans = [] 

        def dfs(index, curr, total):
            if total == target: 
                ans.append(curr.copy())
                return 
            elif total > target: 
                return 
            if index >= len(nums):
                return 

            # left 
            curr.append(nums[index])
            dfs(index, curr, total+nums[index])

            # right 
            curr.pop()
            dfs(index+1, curr, total)
        
        dfs(0, [], 0)
        return ans

            