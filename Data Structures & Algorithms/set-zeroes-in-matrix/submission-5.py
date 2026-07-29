class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS = len(matrix)
        COLS = len(matrix[0]) 

        topZero = False # marks if top should be 0, [0][0] will represent the left col
        #first pass, top row marks columns, left col marks rows 

        for r in range(ROWS): 
            for c in range(COLS):
                if matrix[r][c] == 0 or matrix[r][c] == 0:
                    if r == 0: 
                        topZero = True 
                    else: 
                        matrix[0][c] = 0 
                        matrix[r][0] = 0
        

        # 1 start since we use as markers
        for r in range(1, ROWS):
            for c in range(1, COLS): 
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0
        
        # first cols
        if matrix[0][0] == 0:
            for r in range(ROWS): 
                matrix[r][0] = 0


        # first rows 
        if topZero:
            for c in range(COLS): 
                matrix[0][c] = 0 

        
        
        