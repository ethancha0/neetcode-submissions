class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        ROWS = len(board)
        COLS = len(board[0])

        #searches each cell to see if in between vertically and horizontally.
        def find():
            findSet = set() 
            #vertical check 
            for r in range(1, ROWS-1): 
                for c in range(COLS):
                    if board[r][c] == 0: 
                        continue
                    if board[r][c] == board[r+1][c] and board[r][c] == board[r-1][c]:
                        findSet.add((r, c))
                        findSet.add((r+1, c))
                        findSet.add((r-1, c))
            #horizontal check 
            for r in range(ROWS): 
                for c in range(1, COLS-1): 
                    if board[r][c] == 0:
                        continue
                    if board[r][c] == board[r][c+1] and board[r][c] == board[r][c-1]:
                        findSet.add((r, c))
                        findSet.add((r, c+1))
                        findSet.add((r, c-1))
            
            return findSet 

        #set all values to be crushed to be 0 
        def crush(crushSet):
            for r, c in crushSet:
                board[r][c] = 0 

        
        def drop():
            for c in range(COLS):
                lowestEmpty = ROWS - 1
                for r in reversed(range(ROWS)):
                    if board[r][c] > 0:
                        board[lowestEmpty][c] = board[r][c]
                        lowestEmpty -= 1
                for r in reversed(range(lowestEmpty + 1)):
                    board[r][c] = 0

        #continue with steps until no more crushable candies
        crushedSet = find() 
        while crushedSet: 
            crush(crushedSet)
            drop()
            crushedSet = find()
        
        return board
