class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        LEFT = 0
        RIGHT = len(matrix[0])
        TOP = 0
        BOTTOM = len(matrix)


        ans = []
        
        while LEFT < RIGHT and TOP < BOTTOM:
            #left to right 
            for i in range(LEFT, RIGHT):
                ans.append(matrix[TOP][i])
            TOP += 1
            
            #right to down
            for i in range(TOP, BOTTOM):
                ans.append(matrix[i][RIGHT-1])
            RIGHT -= 1

            if not (LEFT < RIGHT and TOP < BOTTOM):
                break

            #bottom right to left (reverse traversal) 
            for i in reversed(range(LEFT, RIGHT)):
                ans.append(matrix[BOTTOM-1][i])
            BOTTOM -= 1 
            
            #bottom left to top (reverse traversal)
            for i in reversed(range(TOP, BOTTOM)):
                ans.append(matrix[i][LEFT])
            LEFT += 1 


        return ans