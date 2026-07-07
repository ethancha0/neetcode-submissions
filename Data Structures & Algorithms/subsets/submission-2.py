class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        ans = []
        subsets = []

        def dfs(index):
            if index >= len(nums):
                ans.append(subsets.copy())
                return

            # left case: (inclusive)
            subsets.append(nums[index])
            dfs(index+1)


            # right case: (exclusive)
            subsets.pop()
            dfs(index+1)


        dfs(0)
        return ans