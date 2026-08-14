class Solution:
    def trap(self, height: List[int]) -> int:
      # front/end two pointers - move smaller inwards
      # front: monotonic inc. int. if lower found, calculate width 

        left = 0 
        right = len(height)-1 

        largestLeft = height[left] # monotonically increasing
        largestRight = height[right] # monotonically decreasing 

        water = 0 

        while left < right: 
            if largestLeft < largestRight:
                #height bounded by maxWall
                left += 1 
                largestLeft = max(largestLeft, height[left])
                water += largestLeft - height[left]
                
            
            else: 
                right -= 1 
                largestRight = max(largestRight, height[right])
                water += largestRight - height[right]
                



        return water

            
