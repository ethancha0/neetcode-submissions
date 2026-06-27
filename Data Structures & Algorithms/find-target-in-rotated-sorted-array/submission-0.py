class Solution:
    def search(self, nums: List[int], target: int) -> int:
        

        # first pass (find split point)
        left = 0 
        right = len(nums) - 1 

        while left < right:
            mid = left + (right-left) // 2 

            if nums[mid] < nums[right]:
                right = mid 
            else:
                left = mid + 1 
       

        pivot = left 

       # second pass (search within half)

        left = 0 
        right = len(nums) - 1 

        if target >= nums[pivot] and target <= nums[right]:
            left = pivot
        else:
            right = pivot - 1 

        while left <= right: 
            mid = left + (right - left) // 2

            if nums[mid] < target:
                left = mid + 1 
            elif nums[mid] > target:
                right = mid -1
            else: 
                return mid
        
        return -1