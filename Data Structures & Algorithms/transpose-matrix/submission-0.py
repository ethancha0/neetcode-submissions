class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ROWS = len(matrix)
        COLS = len(matrix[0])


        # no reverse needed

        # convert nxm to mxn
        ans = [[None] * ROWS for _ in range(COLS)]
        for r in range(ROWS): 
            for c in range(COLS): 
                ans[c][r] = matrix[r][c]

        
        return ans