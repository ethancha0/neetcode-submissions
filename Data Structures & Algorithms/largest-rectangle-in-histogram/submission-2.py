class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stack = [] # pairs: startIndex, height
        #startIndex: the left boundary when computing window width (index by default)
        maxArea = 0

        for index, height in enumerate(heights):
            start = index
            while stack and stack[-1][1] > heights[index]:
                i, h = stack.pop() 
                maxArea = max(maxArea, h*(index-i))
                start = i
            
            stack.append((start, height))
        


        # clean up any leftovers. (these are valid till end of heights input arr) 
        for i, h in stack: 
            maxArea = max(maxArea, h*(len(heights)-i))


        return maxArea