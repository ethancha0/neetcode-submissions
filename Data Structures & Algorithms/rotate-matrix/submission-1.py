class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        #reverse 
        matrix.reverse()

        #traspose (swap rows,cols from upper diagonal)
        for r in range(len(matrix)):
            for c in range(r + 1, len(matrix)):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
