class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # ex: mid = 11
        # what row is 11 in?:  11//4 =2
        # what col is 11 in?: 11 % 3 =2


        ROWS = len(matrix)
        COLS = len(matrix[0])

        #do binary search. treat matrix as flattened arr 
        left = 0 
        right = (ROWS * COLS) - 1 

        while left <= right:
            mid = left + (right-left)//2

            r = mid // COLS
            c = mid % COLS

            if matrix[r][c] < target:
                left = mid +1
            elif matrix[r][c] > target:
                right = mid -1
            else:
                return True
        return False