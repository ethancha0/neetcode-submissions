class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        # monotonic increasing | pairs:(start, height)
        stack = []
        largest = 0 

        for i in range(len(heights)):
            start = i
            while stack and stack[-1][1] > heights[i]:
                s, h = stack.pop()
                largest = max(largest, h*(i-s))
                start = s

            stack.append((start, heights[i]))

        #there may be extras in stack 
        for s, h in stack:
            largest = max(largest, h*(len(heights)-s))

        return largest

                