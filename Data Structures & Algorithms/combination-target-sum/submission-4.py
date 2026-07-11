class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []

        def dfs(index, curr, total):
            if index == len(nums):
                return 
            if total == target: 
                ans.append(curr.copy())
                return 
            elif total > target: 
                return 

            #left inclusive 
            curr.append(nums[index])
            dfs(index, curr, total+nums[index])

            #right exclusive 
            curr.pop() 
            dfs(index+1, curr, total)

            return 

        dfs(0, [], 0)
        return ans
