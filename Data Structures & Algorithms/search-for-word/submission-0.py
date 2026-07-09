class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        COLS = len(board[0])
        ROWS = len(board)


        visited = set() 

        def dfs(r, c, i):
            #word found 
            if i == len(word):
                return True
            # out of bounds, invalid letter, letter in visited 
            if( r >= ROWS or c >= COLS or 
                r < 0 or c < 0 or 
                word[i] != board[r][c] or 
                (r, c) in visited
            ):
                return False



            visited.add((r, c))

            # recursive (i+1 to check next letter in word)
            res =   (dfs(r-1, c, i+1) or  # left
                    dfs(r+1, c, i+1) or # right
                    dfs(r, c+1, i+1) or # up
                    dfs(r, c-1, i+1)) # down

            # backtracking 
            visited.remove((r, c))

            return res

        #call on every cell 
        for r in range(ROWS): 
            for c in range(COLS):
                if  dfs(r, c, 0):
                    return True
        
        return False




