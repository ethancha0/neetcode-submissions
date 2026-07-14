class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS = len(board)
        COLS = len(board[0])

        def dfs(r, c): 
            if(
                r < 0 or c < 0 or 
                r >= ROWS or c >= COLS or 

                board[r][c] == 'X' or 
                board[r][c] == 'T'
            ):
                return 

            board[r][c] = 'T'
            
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        
        # top/bottom rows 
        for c in range(COLS):
            dfs(0, c)
            dfs(ROWS-1, c)

        # left/right columns
        for r in range(ROWS): 
            dfs(r, 0)
            dfs(r, COLS-1)


        # change all T cells to safe 
        for r in range(ROWS): 
            for c in range(COLS): 
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'T':
                    board[r][c] = 'O'


        