class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1 for _ in range(len(nums))] 

        # left to right 
        temp = 1
        for i in range(len(nums)): 
            ans[i] *= temp
            temp *= nums[i]

        # right to left 
        temp = 1 
        for i in reversed(range(len(nums))): 
            ans[i] *= temp 
            temp *= nums[i]




        return ans 