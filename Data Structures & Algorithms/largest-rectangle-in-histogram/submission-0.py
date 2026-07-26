class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0 
        stack = [] # pair: (start index, height). start index is left boundary this height can  

        for index, height in enumerate(heights): 
            start = index # assume this bar's boundary is itself
            while stack and stack[-1][1] > height:
                poppedIndex, poppedHeight = stack.pop()
                #right boundary = curr index, left boundary = poppedIndex
                maxArea = max(maxArea, poppedHeight *(index - poppedIndex))
                start = poppedIndex #this bar can extend as far left as the one we absorbed
            
            stack.append((start, height))

        #cleanup: anything left in stack never got shorter so stretches to end
        n = len(heights)
        for start, height in stack:
            maxArea = max(maxArea, height * (n-start))

        return maxArea

