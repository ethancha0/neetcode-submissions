class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        if grid == [[]]:
            return 


        ROWS = len(grid)
        COLS = len(grid[0])

        maxIsland = 0 
        visited = set() 

        def dfs(r, c) -> int:
            if(
                r < 0 or c < 0 or 
                r >= ROWS or c >= COLS or 
                grid[r][c] == 0 or 
                (r, c) in visited
            ):
                return 0

            visited.add((r,c))

            up = dfs(r, c+1)
            down = dfs(r, c-1)
            left = dfs(r-1, c)
            right = dfs(r+1, c)

            return up + down + left + right + 1

        
        for r in range(ROWS): 
            for c in range(COLS): 
                if grid[r][c] == 1 and (r,c) not in visited: 
                    maxIsland = max(maxIsland, dfs(r, c))
        return maxIsland