class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        
        ROWS = len(boxGrid)
        COLS = len(boxGrid[0])

        #drop the stones in place 
        for r in range(ROWS):
            dropState = COLS - 1 # the right most elem 
            for c in reversed(range(COLS)):
                if boxGrid[r][c] == '*':
                    #move drop left of stationary
                    dropState = c-1
                elif boxGrid[r][c] == '#':
                    #drop stone to state
                    boxGrid[r][c] = '.'
                    boxGrid[r][dropState] = '#'
                    dropState -= 1

        #rotation 
        # reverse the row order
        boxGrid.reverse()

        # transpose into a new COLS x ROWS matrix
        ans = [[None] * ROWS for _ in range(COLS)]
        for r in range(ROWS):
            for c in range(COLS):
                ans[c][r] = boxGrid[r][c]

        return ans
