class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()

        def dfs(index, curr):
            if index >= len(nums):
                ans.append(curr.copy())
                return
            
            # left (inclusive)
            curr.append(nums[index])
            dfs(index+1, curr)


            # right (exclusive)
            curr.pop()
            # skip for duplicates
            while index+1 < len(nums) and nums[index] == nums[index+1]:
                index += 1 
            
            dfs(index+1, curr)

        
        dfs(0, [])
        return ans