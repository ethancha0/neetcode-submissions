class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0 
        right = len(nums) - 1 

        while left < right: 
            mid = left + (right - left) // 2 

            #compare right against mid 
            if nums[right] < nums[mid]:
                left = mid +1 
            elif nums[right] > nums[mid]:
                right = mid
 


        return nums[left]