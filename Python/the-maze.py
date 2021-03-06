class Solution1:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        
        # Define total rows, columns, visited points, and a queue      
        rows, columns, visited, stack = len(maze), len(maze[0]), set(), []
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        
        # Add the starting point
        visited.add((start[0], start[1]))
        stack.append(start)
    
        while stack:
            x, y = stack.pop()    
            for direction in directions:
                new_row, new_column = x, y
        
                while 0 <= new_row < rows and 0 <= new_column < columns and maze[new_row][new_column] != 1:
                    new_row = new_row + direction[0]
                    new_column= new_column + direction[1]                                                                             
                new_row -= direction[0] 
                new_column -= direction[1]

                if [new_row, new_column] == destination:
                    return True
                    
                if (new_row, new_column) not in visited:
                    stack.append((new_row, new_column))
                    visited.add((new_row, new_column))
                
        return False

    
class Solution2:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        
     # Define total rows, columns, visited points, and a queue      
        visited = set()
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        rows, columns = len(maze), len(maze[0])
        
        # Add the starting point
        visited.add((start[0], start[1]))
        queue = deque([start])
        
        while queue:
            
            x, y = queue.popleft()
            for direction in directions:
                nx = x + direction[0] 
                ny = y + direction[1]
                
                while 0 <= nx < rows and 0 <= ny < columns and maze[nx][ny] != 1:
                    nx += direction[0]
                    ny += direction[1]
                        
                # need to backtrack
                
                nx -= direction[0]
                ny -= direction[1]
                
                if [nx, ny] == destination:
                    return True
                
                if (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append((nx, ny))
                    
        return False
