class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        ROWS = len(heights)
        COLS = len(heights[0])


        pacificSet = set() 
        atlanticSet = set() 

        def dfs(r, c, visitSet, prevHeight):
            if(
                r < 0 or c < 0 or 
                r >= ROWS or c >= COLS or 
                (r, c) in visitSet or 
                heights[r][c] < prevHeight
            ):
                return 

            visitSet.add((r, c))

            dfs(r+1, c, visitSet, heights[r][c])
            dfs(r-1, c, visitSet, heights[r][c])
            dfs(r, c+1, visitSet, heights[r][c])
            dfs(r, c-1, visitSet, heights[r][c])


        #call on pacific (left/top) 
        for r in range(ROWS): 
            dfs(r, 0, pacificSet, 0)
        for c in range(COLS): 
            dfs(0, c, pacificSet, 0)
        
        #call on atlantic (right/bottom)
        for r in range(ROWS): 
            dfs(r, COLS-1, atlanticSet, 0)
        for c in range(COLS):
            dfs(ROWS-1, c, atlanticSet, 0)

        return list(pacificSet & atlanticSet)
        