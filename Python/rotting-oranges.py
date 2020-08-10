class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        rows, columns, fresh_orange, queue = len(grid), len(grid[0]), 0, deque()
        
        # 1.  a).  Figure out how many fresh oranges there are
        #     b).  Add  rotten orange into queue
        
        for row in range(rows):
            for column in range(columns):
                if grid[row][column] == 1:
                    fresh_orange += 1
                    
                elif grid[row][column] == 2:
                    queue.append((row, column))
                    
                    
        # 2. BFS from each of the rotten orange
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        minutes = -1
        queue.append((-1, -1))
        while queue:
            r, c = queue.popleft()
            if r == -1:
                minutes += 1
                
                if queue:
                    queue.append((-1, -1))
                    
            else:    
                for dir in directions:
                    next_row, next_column = r + dir[0], c+dir[1]

                    if 0 <= next_row < rows and 0 <= next_column < columns:
                        if grid[next_row][next_column] == 1:
                            grid[next_row][next_column] = 2
                            fresh_orange -= 1
                            queue.append((next_row, next_column))
                            
        return minutes if fresh_orange==0 else -1
                
