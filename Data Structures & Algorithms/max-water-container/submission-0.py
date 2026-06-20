class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        largest = 0 

        front = 0 
        back = len(heights) - 1

        while front < back: 
            height = min(heights[front], heights[back])
            width = back - front

            largest = max(largest, height * width)
        
            # we should move the smaller ptr
            if heights[front] <= heights[back]:
                front += 1 
            else:
                back -= 1



        return largest