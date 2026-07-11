class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        product = [1 for _ in range(len(nums))]

        # left to right pass 
        curr = 1 
        for i in range(len(nums)): 
            product[i] *= curr 
            curr *= nums[i]

        
        # right to left pass 
        curr = 1 
        for i in range(len(nums)-1, -1, -1): 
            product[i] *= curr
            curr *= nums[i]

        
        return product


        