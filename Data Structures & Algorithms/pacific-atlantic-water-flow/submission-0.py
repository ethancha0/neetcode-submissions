class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])

        pacific = set()
        atlantic = set() 

        def dfs(r, c, visited, prevHeight):
            if(
                r < 0 or c < 0 or 
                r >= ROWS or c >= COLS or 
                heights[r][c] < prevHeight or 
                (r, c) in visited
            ):
                return 

            visited.add((r, c))

            dfs(r+1, c, visited, heights[r][c])
            dfs(r-1, c, visited, heights[r][c])
            dfs(r, c+1, visited, heights[r][c])
            dfs(r, c-1, visited, heights[r][c])
        
        #call top (pacific) and bottom (atlantic) rows 
        for c in range(COLS):
            dfs(0, c, pacific, 0)
            dfs(ROWS-1, c, atlantic, 0)

        # call left (pacific) and right (atlantic) col
        for r in range(ROWS):
            dfs(r, 0, pacific, 0)
            dfs(r, COLS-1, atlantic, heights[r][COLS-1])

        return list(pacific & atlantic)

        