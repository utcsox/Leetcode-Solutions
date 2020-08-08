class Solution1:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        
        # base condition
        if not rooms:
            return
        
        rows, columns = len(rooms), len(rooms[0])
        
        queue = deque([])
        
        # add all gates into the queue
        for row in range(rows):
            for col in range(columns):
                if rooms[row][col] == 0:
                    queue.append((row, col))
                                                       
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        
        distance = 0
        
        while queue:
            
            queue_size = len(queue)
            distance += 1
            
            for index in range(queue_size):
                curr_gate = queue.popleft()
                
                # get the next possible position of the grid
                for dir in directions:
                    nextposition = (curr_gate[0] + dir[0], curr_gate[1] + dir[1])
                    
                    # check     
                    # a) if next possible position: row is positive but less than total number                           of rows available
                    # b) if next possible position: column is positive but less than total number of columns available
                    # c) if value is 2147483647
                    #   if a) b) c) all meet, we assign its value to distance + add into queeue
                    if nextposition[0] >=0 and nextposition[0] < rows \
                    and nextposition[1] >=0 and nextposition[1] < columns \
                    and rooms[nextposition[0]][nextposition[1]] == 2147483647:
                        rooms[nextposition[0]][nextposition[1]] = distance
                        
                        queue.append((nextposition))
                        
class Solution2:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        
        if not rooms:
            return
        
        rows, columns = len(rooms), len(rooms[0])
        
        for row in range(rows):
            for column in range(columns):
                if rooms[row][column] == 0:
                    self.helper(rooms, row, column, 0)
                    
    def helper(self, rooms, x, y, dist):
        rows, columns = len(rooms), len(rooms[0])
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        if x < 0 or x >= rows or y < 0 or y >= columns or rooms[x][y] < dist:
            return

        rooms[x][y] = dist

        for dir in directions:
            self.helper(rooms, x + dir[0], y +dir[1], dist+1)
                
