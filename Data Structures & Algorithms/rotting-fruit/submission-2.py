class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        ROWS = len(grid) 
        COLS = len(grid[0]) 

        visited = set()
        queue = deque() 
        self.freshFruit = 0

        def check(r, c):
            if(
                r < 0 or c < 0 or 
                r == ROWS or c == COLS or
                grid[r][c] != 1 or 
                (r, c) in visited
            ):
                return 
            visited.add((r, c))
            queue.append([r, c])
            self.freshFruit -= 1 

        
        #find rotten banana(s) -- keep track of fresh
        for r in range(ROWS): 
            for c in range(COLS): 
                if grid[r][c] == 2:
                    queue.append([r,c])
                    visited.add((r,c))
                elif grid[r][c] == 1: 
                    self.freshFruit += 1 

        if self.freshFruit == 0: return 0 #IMPORTANT

        #start spreading 
        minutes = -1
        while queue: 
            for i in range(len(queue)): 
                r, c = queue.popleft()

                check(r+1, c)
                check(r-1, c)
                check(r, c+1)
                check(r, c-1)
            minutes += 1 

        if self.freshFruit > 0:
            return -1 
        
        return minutes
             