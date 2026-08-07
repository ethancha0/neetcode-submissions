class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        # we have to create a new arr w updated row and col count 
        ROWS = len(matrix)
        COLS = len(matrix[0])

        ans = [[None] * ROWS for _ in range(COLS)]

        for r in range(ROWS): 
            for c in range(COLS): 
                ans[c][r] = matrix[r][c]

        return ans