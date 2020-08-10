class Solution:
    def zombiesInMatrix(self, rows: int, columns: int, zombies: List[List[int]]) -> int:
        
        if not zombies:
            return -1
        
        # 1.  Figure out how many humans are there and put zombies into a queue
        
        hcount, queue =  0, deque()
        
        for row in range(rows):
            for column in range(columns):
                
                if zombies[row][column] == 0:
                    hcount += 1
                    
                elif zombies[row][column] == 1:
                    queue.append((row, column))
                    
        # 2. if no zombie, return -1
        if not queue:
            return  -1
        
        # 3.  BFS on each zombie 
        hours = -1
        queue.append((-1, -1))
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        while queue:

            row, column = queue.popleft()
            
            if row == -1:
                hours += 1
                
                if queue:
                    queue.append((-1, -1))
                    
            else:
                
                for dir in directions:
                    next_row, next_column = row + dir[0] ,  column + dir[1]
                    
                    if 0<= next_row < rows and 0 <= next_column < columns:
                        if zombies[next_row][next_column] == 0:
                            zombies[next_row][next_column] = 1
                            hcount -= 1
                            queue.append((next_row, next_column))
                    
             
        return hours 
                    
