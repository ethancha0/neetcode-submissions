class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # what if we turned each row / col into a set 

        # check row 
        for row in range(9):
            rowSet = set()
            for col in range(9):
                val = board[row][col]
            
                if val == '.': 
                    continue

                if val in rowSet:
                    return False 
                
                rowSet.add(val)

        
        # check col 
        for col in range(9):
            colSet = set()
            for row in range(9):
                val = board[row][col]

                if val == '.':
                    continue

                if val in colSet:
                    return False

                colSet.add(val)
        
        # check 3x3 grid. outer two loops check the big 3x3 grid
        for square in range(9):
            squareSet = set()
            for i in range(3):
                for j in range(3):
                    row = (square//3) * 3 + i 
                    col = (square % 3) * 3 + j
                    val = board[row][col]
                    if val == ".":
                        continue
                    if val in squareSet: 
                        return False
                    squareSet.add(board[row][col])
        
        return True