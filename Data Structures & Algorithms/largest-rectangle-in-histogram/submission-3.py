class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0 
        stack = [] # pair: (startIndex, height) | monotonic increasing order

        for i in range(len(heights)):
            start = i
            while stack and stack[-1][1] > heights[i]:
                index, h = stack.pop()
                maxArea = max(maxArea, h*(i-index))
                start = index
            stack.append((start, heights[i]))

        # check if any bars left in stack (these lasted till end) 
        for i, h in stack: 
            maxArea = max(maxArea, h*(len(heights) - i))
        

        return maxArea