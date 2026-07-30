class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        ROWS = len(boxGrid)
        COLS = len(boxGrid[0])


        # simulate gravity first
        for r in range(ROWS): 
            drop = COLS-1
            for c in reversed(range(COLS)):
                if boxGrid[r][c] == '#':
                    boxGrid[r][c] = '.'
                    boxGrid[r][drop] = '#'
                    drop -= 1
                elif boxGrid[r][c] == '*':
                    drop = c-1 
                 
        # rotate 90degrees (reverse + transpose)
        boxGrid.reverse()

        ans = [[None] * ROWS for _ in range(COLS)]
        for r in range(ROWS): 
            for c in range(COLS): 
                ans[c][r] = boxGrid[r][c]

        return ans