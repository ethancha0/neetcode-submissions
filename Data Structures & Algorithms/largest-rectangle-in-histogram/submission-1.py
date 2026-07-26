class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0 
        stack = [] # pair: (startIndex, height)
        # startIndex is defaulted to its normal index.
        # but updates to last popped if a decreasing was found 


        for index, height in enumerate(heights):
            start = index
            while stack and stack[-1][1] > height: 
                i, h = stack.pop() 
                
                maxArea = max(maxArea, h * (index-i))
                start = i
            stack.append((start, height))


        #there still may be bars in the stack. need to flush out 
        for i, h in stack: 
            maxArea = max(maxArea, h * (len(heights) -i))


        return maxArea