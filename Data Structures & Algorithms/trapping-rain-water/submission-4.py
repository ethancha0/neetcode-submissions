class Solution:
    def trap(self, height: List[int]) -> int:
        front = 0 
        end = len(height)-1

        highestLeft = height[front]
        highestRight = height[end]
        water = 0 

        while front < end:
            if highestLeft < highestRight: 
                front += 1 
                highestLeft = max(highestLeft, height[front])
                water += highestLeft - height[front]
            else: 
                end -= 1 
                highestRight = max(highestRight, height[end])
                water += highestRight - height[end]

        return water