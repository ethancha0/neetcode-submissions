class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        #inverse 
        matrix.reverse() 
        #transpose 
        for r in range(len(matrix)): 
            for c in range(r+1, len(matrix)): 
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]