class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set() 
        self.maxArea = 0

        def dfs(r, c) -> int: # check on this 
            if(
                r >= ROWS or c >= COLS or 
                r < 0 or c < 0 or 
                (r, c) in visited or 
                grid[r][c] == 0
            ):
                return 0

            
            visited.add((r,c))


            
            right = dfs(r+1, c)
            left = dfs(r-1, c)
            top = dfs(r, c+1)
            bottom = dfs(r, c-1)

            self.maxArea = max(self.maxArea, right + left + top + bottom + 1)

            return(right + left + top + bottom) + 1


        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in visited and grid[r][c] == 1:
                    dfs(r, c)
        
        return self.maxArea
            
