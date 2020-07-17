class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # a valid sudoku need to ensure each row, column and box can only has 1 to 9
        
        row_dict = [collections.defaultdict(int) for i in range(9)]
        column_dict = [collections.defaultdict(int) for j in range(9)]
        box = [collections.defaultdict(int) for k in range(9)]
        
        
        for row in range(9):
            for column in range(9):
                box_index = int(row / 3) * 3 + int(column/3)
                
                if board[row][column] != '.':
                    num = board[row][column]
                    
                    row_dict[row][num] += 1
                    column_dict[column][num] += 1
                    box[box_index][num] += 1
                    
                    if row_dict[row][num] > 1 or column_dict[column][num] > 1 or box[box_index][num] > 1:
                        return False

        return True
