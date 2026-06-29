class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        ans = [1] * len(nums) 

        # left pass 
        prev = 1
        for i in range(len(nums)):
            ans[i] *= prev
            prev *= nums[i]


        # right pass 
        prev = 1 
        for i in range(len(nums)-1, -1, -1):
            ans[i] *= prev
            prev *= nums[i]

        return ans

