class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        # can we use a dfs on the (sr, sc) coord. BC same val
        # we can do a two pass, mark in visited set, then change 
    
        ROWS = len(image) 
        COLS = len(image[0])

        visited = set() 

        def dfs(r, c):
            if(
                r < 0 or c < 0 or 
                r >= ROWS or c >= COLS or 
                (r, c) in visited or 
                image[r][c] != image[sr][sc]
            ):
                return
            #add to set
            visited.add((r, c))

            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        
        dfs(sr, sc)

        #change all in visited to new num
        for r in range(ROWS): 
            for c in range(COLS): 
                if (r, c) in visited: 
                    image[r][c] = color
        
        return image
