class Solution:
    def trap(self, height: List[int]) -> int:
        
        left = 0 
        right = len(height)-1 

        maxLeftWall = height[left]
        maxRightWall = height[right] 

        water = 0 

        while left < right: 
            if maxLeftWall < maxRightWall: 
                left += 1 
                maxLeftWall = max(maxLeftWall, height[left])
                water += maxLeftWall - height[left]

            else: 
                right -= 1 
                maxRightWall = max(maxRightWall, height[right])
                water += maxRightWall - height[right]


        return water