class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        #boundary walls of unexplored regions
        left = 0
        right = len(matrix[0])
        top = 0 
        bottom = len(matrix)

        ans = []

        while left < right and top < bottom:
            #move left to right 
            for i in range(left, right):
                ans.append(matrix[top][i])
            top += 1
            
            #move top to bottom
            for i in range(top, bottom):
                ans.append(matrix[i][right-1])
            right -= 1 

            #stop early to avoid revisited cells
            if not (left < right and top < bottom):
                break

            
            #move right to left 
            for i in reversed(range(left, right)):
                ans.append(matrix[bottom-1][i])
            bottom -= 1 
            
            #move up 
            for i in reversed(range(top, bottom)):
                ans.append(matrix[i][left])
            left += 1



        return ans


