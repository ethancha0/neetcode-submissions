class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:

        ROWS = len(boxGrid) 
        COLS = len(boxGrid[0])

        # drop the stones. iterate right to left to compute drop spot 

        for r in range(ROWS):
            nextDrop = COLS - 1
            for c in reversed(range(COLS)):
                #update and move drop  
                if boxGrid[r][c] == '#':
                    boxGrid[r][c] = '.'
                    boxGrid[r][nextDrop] = '#'
                    nextDrop -= 1
                elif boxGrid[r][c] == '*':
                    nextDrop = c-1


        # rotate 90 : reverse then transpose
        boxGrid.reverse()

        ans = [[None] * ROWS for _ in range(COLS)]

        for r in range(ROWS): 
            for c in range(COLS): 
                ans[c][r] = boxGrid[r][c]


        return ans
