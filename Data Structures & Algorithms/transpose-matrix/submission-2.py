class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        
        ROWS = len(matrix)
        COLS = len(matrix[0])

        newMatrix = [[None] * ROWS for _ in range(COLS) ]

        for r in range(ROWS): 
            for c in range(COLS):
                newMatrix[c][r] = matrix[r][c]

        return newMatrix