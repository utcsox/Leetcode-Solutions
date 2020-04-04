from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        matrix_dim = len(matrix)
        print(f'There are {matrix_dim} of rows and {matrix_dim} of columns')
        
        for row in range(matrix_dim//2):
            for col in range(row, matrix_dim-1 - row):
                tmp = matrix[row][col]
                matrix[row][col] = matrix[matrix_dim-1 - col][row]
                matrix[matrix_dim-1-col][row]= matrix[matrix_dim- 1-row][matrix_dim-1-col]
                matrix[matrix_dim-1-row][matrix_dim-1-col] = matrix[col][matrix_dim-1-row]  
                matrix[col][matrix_dim-1-row] = tmp
                
                print(row, col, tmp, matrix[row][col],matrix[matrix_dim-1-col][row], \
                      matrix[matrix_dim-1-row][matrix_dim-1-col] )

        """
        Do not return anything, modify matrix in-place instead.
from typing import List
class Solution2:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        matrix_dim = len(matrix)
        print(f'There are {matrix_dim} of rows and {matrix_dim} of columns')
        
        for row in range(matrix_dim):
            for col in range(row, matrix_dim):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]
        for i in range(matrix_dim):
            matrix[i].reverse()
        
        """
        Do not return anything, modify matrix in-place instead.
        """
