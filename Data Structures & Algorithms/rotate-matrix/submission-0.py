class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:

        #reverse
        matrix.reverse()

        #transpose matrix (swap only with upper triangle)
        for i in range(len(matrix)):
            for j in range(i+1, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


