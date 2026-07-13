class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        def mold(r, c):
            if(
                r < 0 or c < 0 or 
                r >= ROWS or c >= COLS or 
                (r, c) in visited or 
                grid[r][c] != 1 
            ):
                return 
            queue.append([r, c])
            visited.add((r,c))
            self.goodBananas -= 1

        queue = deque()
        visited = set()
        self.goodBananas = 0


        # find the rotten fruit
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append([r,c])
                    visited.add((r,c))
                elif grid[r][c] == 1:
                    self.goodBananas += 1 
        if self.goodBananas == 0:
            return 0
        
        minutes = -1
        while queue: 
            for i in range(len(queue)):
                r, c = queue.popleft()

                mold(r+1,c)
                mold(r-1, c)
                mold(r, c+1)
                mold(r, c-1)
            minutes += 1 

        
        if self.goodBananas > 0:
            return -1
        return minutes
        

