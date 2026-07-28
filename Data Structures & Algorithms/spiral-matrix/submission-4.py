class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # wall boundaries 
        top = 0 
        bottom = len(matrix) 
        left = 0 
        right = len(matrix[0])

        ans = []

        #create while loop at end
        while top < bottom and left < right: 
            #left to right:
            for i in range(left, right):
                ans.append(matrix[top][i])
            top += 1 

            #top to bottom (right wall)
            for i in range(top, bottom):
                ans.append(matrix[i][right-1])
            right -= 1 

            if not top < bottom or not left < right: 
                break

            #right to left (bottom)
            for i in reversed(range(left, right)): 
                ans.append(matrix[bottom-1][i])
            bottom -= 1 

            #bottom to top (left wall)
            for i in reversed(range(top, bottom)):
                ans.append(matrix[i][left])
            left += 1 



        return ans