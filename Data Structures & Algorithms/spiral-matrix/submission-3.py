class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # boundary walls
        left = 0
        top = 0
        right = len(matrix[0])
        bottom = len(matrix)

        ans = [] 

        while left < right and top < bottom:
            #left to right (top)
            for i in range(left, right):
                ans.append(matrix[top][i])
            top += 1 

            #top to bottom (right)
            for i in range(top, bottom):
                ans.append(matrix[i][right-1])
            right -= 1 

            if not left < right or not top < bottom:
                break

            #right to left(bottom) but reverse traversal
            for i in reversed(range(left, right)): 
                ans.append(matrix[bottom-1][i])
            bottom -= 1 

            #bottom to top (left) but reverse traversal 
            for i in reversed(range(top, bottom)):
                ans.append(matrix[i][left])
            left += 1 

        

        return ans
