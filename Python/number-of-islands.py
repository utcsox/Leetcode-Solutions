class Solution1:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        if not grid:
            return 0

        def helper(grid, row, column):
            
            # for each grid u travel turn it to 0
            grid[row][column] = '0'
            
            # u can continue traverse left, right, up and down
            directions = [(1,0), (-1,0), (0,1), (0,-1)]
            
            for x, y in directions:
                new_row = row + x
                new_column = column + y
                
                # check boundary, new row and new column have to be inside the boundary
                
                if new_row >= 0 and new_row < total_rows and new_column >=0 and new_column < total_columns and grid[new_row][new_column] == '1':
                    helper(grid, new_row, new_column)
                    
            return 
        
        
        # get the height and width of the rectangles
        total_rows = len(grid)
        total_columns = len(grid[0])
        
        count = 0
        for r in range(total_rows):
            for c in range(total_columns):
                if grid[r][c] == '1':
                    count += 1
                    helper(grid, r, c)
        return count
                    
class Solution2:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        if not grid:
            return 0
        
        rows, columns = len(grid), len(grid[0])
        islands = 0
        visited = set()
        directions=[(0, 1), (1, 0), (-1, 0), (0, -1)]
        
        def bfs(r, c):
            queue = collections.deque()
            visited.add((r, c))
            queue.append((r, c))
            
            while queue:
                row, column = queue.popleft()
                for dr, dc in directions:
                    if (row + dr in range(rows) and
                       column +dc in range(columns) and 
                       grid[row + dr][column + dc] == '1' and
                       (row + dr, column +dc) not in visited):
                        queue.append((row + dr, column +dc))
                        visited.add((row+dr, column+dc))
                    
                
        
        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == '1' and (r, c) not in visited:
                    bfs(r, c)
                    islands += 1
                    
        return islands        
