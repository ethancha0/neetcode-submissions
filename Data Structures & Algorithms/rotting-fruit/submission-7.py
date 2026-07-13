class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        ROWS = len(grid)
        COLS = len(grid[0])
        queue = deque() 
        self.goodBananas = 0 

        def verify(r, c):
            if(
                r < 0 or c < 0 or 
                r >= ROWS or c >= COLS or 
                grid[r][c] != 1
            ):
                return 
            grid[r][c] = 2 #convert to bad 
            queue.append([r,c])
            self.goodBananas -= 1
        
        

        for r in range(ROWS):
            for c in range(COLS): 
                if grid[r][c] == 2:
                    queue.append([r,c])
                elif grid[r][c] == 1: 
                    self.goodBananas += 1 

        if self.goodBananas == 0:
            return 0

        minutes = -1 
        while queue: 
            for i in range(len(queue)): 
                r, c, = queue.popleft() 

                verify(r+1, c)
                verify(r-1, c)
                verify(r, c+1)
                verify(r, c-1)
            minutes +=1
        
        if self.goodBananas > 0:
            return -1 
        return minutes


