class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:

        ROWS = len(board)
        COLS = len(board[0])


        #1)find 
        def find():
            crushSet = set()

            #vertical
            for r in range(1, ROWS-1): 
                for c in range(COLS):
                    if board[r][c] == 0: 
                        continue
                    if board[r][c] == board[r+1][c] and board[r][c] == board[r-1][c]:
                        crushSet.add((r,c))
                        crushSet.add((r+1, c))
                        crushSet.add((r-1, c))
            #horizontal 
            for r in range(ROWS):
                for c in range(1, COLS-1):
                    if board[r][c] == 0: 
                        continue
                    if board[r][c] == board[r][c+1] and board[r][c] == board[r][c-1]:
                        crushSet.add((r,c))
                        crushSet.add((r,c+1))
                        crushSet.add((r,c-1))

            return crushSet
                    
        #2)crush
        def crush(crushSet):
            for r in range(ROWS): 
                for c in range(COLS): 
                    if (r, c) in crushSet:
                        board[r][c] = 0 

        #3)gravity
        def gravity():
            for c in range(COLS):
                dropZero = ROWS-1 #holds row index for cell to fall on 
                for r in reversed(range(ROWS)):
                    if board[r][c] > 0: 
                        board[dropZero][c] = board[r][c]
                        dropZero -= 1 
            
                #cleanup: all cells above dropzero should be 0
                for r in range(ROWS):
                    if r <= dropZero: 
                        board[r][c] = 0



        #4)repeat until #1 returns empty
        crushSet = find()
        while crushSet: 
            crush(crushSet)
            gravity()
            crushSet = find() 

        return board


