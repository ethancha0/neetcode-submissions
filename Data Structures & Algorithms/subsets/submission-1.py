class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        subsets = []

        def dfs(i):
            # base case (reach end of a path)
            if i >= len(nums):
                ans.append(subsets.copy())
                return

            # left case (inclusive)
            subsets.append(nums[i])
            dfs(i+1)

            # right case (exclusive)
            subsets.pop()
            dfs(i+1)


        dfs(0)
        return ans 