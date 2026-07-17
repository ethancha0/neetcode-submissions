class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        self.ans = []

        def dfs(curr, total, index): 
            if total == target: 
                self.ans.append(curr.copy())
                return
            elif total > target or index >= len(nums):
                return 

            
            # left path (inclusive) 
            curr.append(nums[index])
            dfs(curr, total+nums[index], index)

            # right path (exclusive)
            curr.pop()
            dfs(curr, total, index+1)

        

        dfs([], 0, 0)
        return self.ans
