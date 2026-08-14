class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # area is limited by min of left/right height
        # monotonic inc stack. 
        # when order breaks, we recalculate area 


        stack = [] # (start, index)
        left = 0
        largestArea = 0

        for right in range(len(heights)):
            start = right
            while stack and heights[right] < stack[-1][0]:
                height, index = stack.pop()
                largestArea = max(largestArea, (height * (right-index)))
                start = index

            stack.append((heights[right], start))

        
        # there may be leftovers in the stack
        for h, i in stack:
            largestArea = max(largestArea, (h * (len(heights)-i)))
            
        
        return largestArea

