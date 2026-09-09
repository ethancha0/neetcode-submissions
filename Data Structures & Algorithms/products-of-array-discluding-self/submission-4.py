class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #multiplication is communicative. for each num, multiple the left product by right product
        #achieve this with prefix sums 

        temp = 1
        ans = [1 for _ in range(len(nums))]
        for i in range(len(nums)):
            ans[i] *= temp 
            temp *= nums[i]

        temp = 1 
        for i in range(len(nums)-1, -1, -1):
            ans[i] *= temp
            temp *= nums[i]

        return ans
   



        