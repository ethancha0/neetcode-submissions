class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        # can we use a dfs on the (sr, sc) coord. BC same val
        # we can do a two pass, mark in visited set, then change 
    
        ROWS = len(image) 
        COLS = len(image[0])
        old_color = image[sr][sc]

        visited = set() 

        def dfs(r, c):
            if(
                r < 0 or c < 0 or 
                r >= ROWS or c >= COLS or 
                (r, c) in visited or 
                image[r][c] != old_color
            ):
                return
            #add to set
            visited.add((r, c))

            image[r][c] = color

            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        
        dfs(sr, sc)


        
        return image
