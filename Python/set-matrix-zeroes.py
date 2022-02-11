class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        rows, columns = len(matrix), len(matrix[0])
        
        row_set, column_set = set(), set()
        
        for row in range(rows):
            for column in range(columns):
                if matrix[row][column] == 0:
                    row_set.add(row)
                    column_set.add(column)
                    
                    
        for row in range(rows):
            for column in range(columns):
                if row in row_set or column in column_set:
                    matrix[row][column] = 0
