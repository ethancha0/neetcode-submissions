class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        ROWS = len(board)
        COLS = len(board[0])


        # 1) mark candies to be crushed (check if middle of two+)
        def mark():
            crushSet = set()
            #vertical check
            for c in range(COLS): 
                for r in range(1, ROWS-1):
                    if board[r][c] == 0: 
                        continue 
                    elif board[r][c] == board[r+1][c] and board[r][c] == board[r-1][c]:
                        crushSet.add((r,c))
                        crushSet.add((r+1, c))
                        crushSet.add((r-1, c))
                    
            #horizontal check 
            for r in range(ROWS): 
                for c in range(1, COLS-1):
                    if board[r][c] == 0:
                        continue
                    elif board[r][c] == board[r][c+1] and board[r][c] == board[r][c-1]:
                        crushSet.add((r,c))
                        crushSet.add((r,c+1))
                        crushSet.add((r, c-1))
            return crushSet
            


        # 2) crush all marked candies
        def crush(crushSet):
            for r, c in crushSet: 
                board[r][c] = 0


        # 3) simulate gravity
        def gravity():
            for c in range(COLS):
                dropZero = ROWS-1 #holds row index for next drop 
                for r in reversed(range(ROWS)): 
                    if board[r][c] > 0: 
                        board[dropZero][c] = board[r][c]
                        dropZero -= 1 

                #cleanup: zero everything above the drop zero
                for r in range(ROWS): 
                    if r <= dropZero: 
                        board[r][c] = 0
            



        # 4) repeat until 1 returns empty
        crushSet = mark()
        while crushSet:
            crush(crushSet)
            gravity()
            crushSet = mark()
        
        return board

