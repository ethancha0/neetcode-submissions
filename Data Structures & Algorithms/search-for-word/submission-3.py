class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        ROWS = len(board)
        COLS = len(board[0])

        visited = set()

        def dfs(index, r, c):
            if index == len(word):
                return True 
            if(
                r >= ROWS or c >= COLS or 
                r < 0 or c < 0 or 
                board[r][c] != word[index] or 
                (r, c) in visited
            ):
                return False

            visited.add((r, c))

            res = (
                dfs(index+1, r+1, c) or
                dfs(index+1, r-1, c) or 
                dfs(index+1, r, c+1) or 
                dfs(index+1, r, c-1)
            )

            visited.remove((r, c))

            return res

        
        for r in range(ROWS):
            for c in range(COLS): 
                if dfs(0, r, c):
                    return True 
        return False


        