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
                index > len(word) or 
                (r, c) in visited or
                board[r][c] != word[index]
            ):
                return False

            
            visited.add((r, c))

            ans = (
                dfs(index+1, r+1, c) or 
                dfs(index+1, r-1, c) or 
                dfs(index+1, r, c+1) or 
                dfs(index+1, r, c-1) 
            )

            visited.remove((r,c))

            return ans


        for r in range(ROWS):
            for c in range(COLS):
                if dfs(0, r, c):
                    return True 

        return False
