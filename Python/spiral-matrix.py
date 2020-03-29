from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
    #  check if input list of list exist, if not return empty list
        rows = len(matrix)
        if rows == 0:
            return []
    # check number of element in each list
        columns = len(matrix[0])
    # create an empty list to save the result and save the first list
        res  = []
        res.extend(matrix[0])
    # Cheeck if there are more than one list
        if rows > 1:
    # Add element from the last column(2nd row to the last row)
            for row in range(1, rows):
                res.append(matrix[row][columns-1])
    # Add element of the last row, (2nd to last column to 1st column)
            for col in range(columns-2, -1, -1):
                res.append(matrix[rows-1][col])
    
            if columns > 1:
                # Add element in the first column, (2nd to the last row to the second row)
                for row in range(rows-2, 0, -1):
                    res.append(matrix[row][0])
    # Create a new matrix for second rows to the 2nd to the last rows
        M = []
        for row in range(1, rows-1):
            M.append(matrix[row][1:-1])

        return res + self.spiralOrder(M)
