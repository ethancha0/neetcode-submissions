class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        rows = len(matrix)
        cols = len(matrix[0])

        left = 0 
        right = (rows * cols) - 1

        while left <= right: 
            mid = left + (right-left) // 2 

            #find which subarry mid is in 
            r = mid // cols
            c = mid % cols

            if matrix[r][c] < target:
                left = mid +1
            elif matrix[r][c] > target:
                right = mid -1
            if matrix[r][c] == target:
                return True 

        return False



