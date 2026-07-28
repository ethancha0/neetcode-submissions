class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # monotonic increasing (start, height)
        maxArea = 0

        for i in range(len(heights)):
            start = i
            while stack and stack[-1][1] > heights[i]:
                s, h = stack.pop() 
                maxArea = max(maxArea, h*(i-s))
                start = s
            
            stack.append((start, heights[i]))

        # some values in queue
        for s, h in stack:
            maxArea = max(maxArea,(h * (len(heights)- s )))


        return maxArea