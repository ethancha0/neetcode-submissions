class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS = len(matrix)
        COLS = len(matrix[0])

        rowZero = False # tracks if the first row should be zero bc [0][0] conflict

        #first pass: mark first row/col if '0' found 
        for r in range(ROWS):
            for c in range(COLS): 
                if matrix[r][c] == 0:
                    #put markers
                    matrix[0][c] = 0
                    if r > 0: 
                        matrix[r][0] = 0
                    else:
                        rowZero = True 
        
        # second pass: if 0, mark entire row/col 
        for r in range(1, ROWS): 
            for c in range(1, COLS): 
                if matrix[r][0] == 0 or matrix[0][c] == 0: # set 0 if initial markers say its ok
                    matrix[r][c] = 0 

        #what is this 
        if matrix[0][0] == 0: 
            for r in range(ROWS): 
                matrix[r][0] = 0

        if rowZero: 
            for c in range(COLS): 
                matrix[0][c] = 0

                    


        