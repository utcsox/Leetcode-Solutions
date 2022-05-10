class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        
        origin, new, encoding
           0     0      0
           1     0      1
           0     1      2
           1     1      3
        """
        
        rows, columns = len(board), len(board[0])
        
        def countNeighbors(r, c):
            
            neighbor = 0
            
            for row in range(r - 1, r + 2):
                for column in range( c - 1, c + 2):
                    if ((row == r and column == c) or row < 0 or column < 0 or row == rows or column == columns):
                        continue
                    if board[row][column] in [1, 3]:
                        neighbor += 1
                        
            return neighbor
        
        
        for row in range(rows):
            for column in range(columns):
                neighbors = countNeighbors(row, column)
                if board[row][column]:
                    if neighbors in [2, 3]:
                        board[row][column] = 3
                        
                else:
                    if neighbors == 3:
                        board[row][column] = 2
                        
        for row in range(rows):
            for column in range(columns):
                if board[row][column] == 1:
                    board[row][column] = 0
                    
                elif board[row][column] in [2, 3]:
                    board[row][column] = 1
