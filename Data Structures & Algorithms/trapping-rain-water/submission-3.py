class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0 
        right = len(height) - 1 

        highestLeft = height[left]
        highestRight = height[right]
        water = 0 

        while left < right:
            if highestLeft < highestRight: 
                left += 1 
                highestLeft = max(highestLeft, height[left])
                # this equation works bc atp, we know that highestLeft is alr the smaller wall (limiting factor) 
                water += highestLeft - height[left]
            else: 
                right -= 1 
                highestRight = max(highestRight, height[right])
                water += highestRight - height[right]

        return water