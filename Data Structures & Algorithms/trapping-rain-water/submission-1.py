class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0 
        right = len(height)-1 

        highestLeft = height[left] 
        highestRight = height[right]
        
        water = 0 

        while left < right: 
            if highestLeft < highestRight:
                left += 1 
                highestLeft = max(highestLeft, height[left])
                water += highestLeft - height[left]
            else: 
                right -= 1 
                highestRight = max(highestRight, height[right])
                water += highestRight - height[right] 

        return water
